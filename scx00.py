
"""SCx00.py 

   Python module for reading and writing data from/to Eaton Power SC200 and SC300 Controllers.
   I don't know whether it also works with the SC100 model as I don't have access to one.

   The module implements a simple wrapper for the Eaton SCx00 XMLRPC interface. The SCx00 class
   provides dictionary style access to all data items.

   No error checking is done and all XMLRPC errors are passed on to the caller.

   Status: Works for me ;-)

   Markus Juenemann

   Big thanks to 'The-Godfather' for having figured out how to make xmlrpc calls with
   cookies and 'GermainZ' for having asked the question on Stackoverflow. 
   The (Safe)CookieTransport implementations below are based on their code.

"""

__author__ = 'Markus Juenemann <markus@juenemann.net>'
__version__ = '0.1.0'
__license__ = 'BSD 2-Clause'


# Things that are needed somewhere else.
#
import urllib.parse
import xmlrpc.client
import ssl

DEBUG = False
TIMEOUT = 10


# The Eaton SCx00 Controller wants authenication credentials sent as cookies.
# As the default transports do not support this we have to create custom ones.
#
class SafeCookieTransport(xmlrpc.client.SafeTransport):
    def __init__(self, context=None, username='', password='', **kwargs):
        self.username = username
        self.password = password
        super().__init__(context=context, **kwargs)

    def send_headers(self, connection ,headers):
        cookie = 'delimiter=%2C'
        if self.username and self.password:
            cookie  = f'name={self.username}; pwd={self.password}; ' + cookie
        connection.putheader('Cookie', cookie)
        connection.timeout = TIMEOUT
        super().send_headers(connection, headers)


class CookieTransport(xmlrpc.client.Transport):
    def __init__(self, username='', password='', **kwargs):
        self.username = username
        self.password = password
        super().__init__(**kwargs)

    def send_headers(self, connection ,headers):
        cookie = 'delimiter=%2C'
        if self.username and self.password:
            cookie  = f'name={self.username}; pwd={self.password}; ' + cookie
        connection.putheader('Cookie', cookie)
        connection.timeout = TIMEOUT
        super().send_headers(connection, headers)



class SCx00:
    """Represents a connection to an Eaton Powerware SCx00 Controller.

       >>> client = SCx00('10.1.2.3')

       Instances provides dictionary-style access to the data items of the conroller.

       >>> client['Site-Name']
       Site-12345

       Write access probbaly requires to authenticate first. Either provide username
       and password as keywork arguments when creating an instance or call the 
       ``SCx00.login()`` method.

       >>> client.login('myusername', 'mypassword')

       >>> client['Site-Name']
       Site-12345

       >>> client['Site-Name'] = 'Site-98765'
       >>> client['Site-Name']
       Site-98765

       Returned values may have to be cast into their appropriate type. Converting
       an integer into an IPv4 address actually works as IPv4 addresses area really
       just 32 bit integers.

       >>> client['IP-Address']
       167838211

       >>> import ipaddress
       >>> ipaddress.IPv4Address(client['IP-Address'])
       IPv4Address('10.1.2.3')

       Enumerations are returned as their integer value (1=Disable, 1=All, 2=Read Only, 3=V3 Only).

       >>> client['SNMP-Access']
       3

       Boolean values are enumerations (0=Disabled, 1=Enabled) which fortunately can be directly
       converted into the proper Python type and value.

       >>> client['HTTPS-Access']
       1
       >>> bool(client['HTTPS-Access'])
       True

       >>> client['HTTP-Access']
       0
       >>> bool(client['HTTP-Access'])
       False

       Date/time values are easy to convert, too.

       >>> client['Next-Battery-Test-Start-Time']
       1639261885

       >>> import datetime
       >>> datetime.datetime.fromtimestamp(client['Next-Battery-Test-Start-Time'])
       datetime.datetime(2021, 12, 12, 9, 31, 25)

       Tabular can be accessed through a special slicing notation.

       >>> client['DI-Name:1-8']
       ['Surge Diverter Fault', 'Surge Filter Fault', 'UPS Fault', 'Battery Isolated',
        'Panel Temp High', 'Door Alarm', 'UPS Mains Power Fail', 'Battery Fuse Fail']

       It is up to the user to provide valid values for the lower and upper bounds of
       a slice as these are passed varbatim to the controller's XMLRPC interface.
       Please note that some  tables index data starting with 0, others with 1. For
       example, 'DI-Name' is indexed starting with 1.

       >>> client['DI-Name:0-8']
       Traceback (most recent call last):
         File "scx00.py", line 331, in <module>
           print(client['DI-Name:0-10'])
         File "scx00.py", line 291, in __getitem__
           raise KeyError(f"{item} -> {resp}")
       KeyError: "DI-Name:0-10 -> [[{'faultCode': 4, 'faultString': 'Exception: Index out of range on access to item DI-Name'}]]"

       Individual entries can be accessed directly which is the only way to update an
       item in a table.

       >>> client['DI-Name:6']
       Door Alarm

       >>> client['DI-Name:6'] = 'Door Open Alarm'
       >>> client['DI-Name:6']
       Door Open Alarm
       
       Unknown items will raise a KeyError exception.

       >>> client['No-Such-Item']
       Traceback (most recent call last):
         File "scx00.py", line 334, in <module>
           print(client['No-Such-Item'])
         File "scx00.py", line 256, in __getitem__
           raise KeyError(f"{item} -> {resp}")
       KeyError: "No-Such-Item -> [{'faultCode': 3, 'faultString': 'Unknown Item'}]"


       Arguments:
       controller -- Hostname or IP Address of the controller.

       Keyword Arguments:
       username -- Username for authentication.
       password -- Password for authentication.
       port -- The port the controller listens on. Defaults to 443.
       proto -- Either 'http' or 'https'. Defaults to 'https'.

       If 'username' and 'password' are not given, communications with the
       SCx000 controller will be unauthenticated. Depending on the 
       configuration of the SCx00 controller this may be limited to
       read-only access or no access at all.

       """


    def __init__(self, controller, proto=None, port=0, username='', password=''):
        assert isinstance(port, int)
        assert proto in ("http", "https", None)

        self.controller = controller
        self.login(username, password)

        if port == 80 and proto is None:
            self.port = port
            self.proto = 'http'
        elif port == 443 and proto is None:
            self.port = port
            self.proto = 'https'
        elif proto == 'https' and port is 0:
            self.port = 443
            self.proto = proto
        elif proto == 'http' and port is 0:
            self.port = 80
            self.proto = proto
        else:
            self.port = 443
            self.proto = 'https'


    def login(self, username, password):
        """Store username and password for later(!) authentication."""
        self.username = username
        self.password = password


    @property
    def url(self):
        return urllib.parse.urlunparse((self.proto, f"{self.controller}:{self.port}", "xmlrpc", None, None, None))


    @property
    def transport(self):
        if self.proto == 'https':
            return SafeCookieTransport(context=ssl._create_unverified_context(), username=self.username, password=self.password)
        else:
            return CookieTransport(username=self.username, password=self.password)


    def __getitem__(self, item):
        """Read data item(s) from the controller.

        """

        assert isinstance(item ,str)


        with xmlrpc.client.ServerProxy(self.url, transport=self.transport, verbose=DEBUG) as proxy:

            resp = proxy.db.get([item])
            """The response will always be a list. Examples:

               Single items:

                 [171027852] 
                 ['CTRL-12345']

               List of items, possible with "repeat" markers.

                 [['Door Alarm', 'Cabinet Fan Active', 'Surge Filter Alarm', 'Surge Diverter Alarm', 'Digital Input 5']]
                 [[0, {'repeatLast': 4}]]

               Single items or lists contain fault messages.

                 [['Low Float', ..., 'Normal Charge', {'faultCode': 4, 'faultString': 'Exception: Index out of range on access to item Alarm-Name'}]]

                 [{'faultCode': 3, 'faultString': 'Unknown Item'}]

            """

          
            # I don't know what an empty response could mean. Does the controller ever return
            # an empty response?
            #
            if not resp:
                raise KeyError(f"{item} -> {resp}")


            # Ensure that the resopnse is a list.
            #
            if not isinstance(resp, list):
                raise KeyError(f"{item} -> {resp}")


            # Extract the first item from the list as it contains the value.
            #
            value = resp[0]


            # The server returned an error if the first item in the list is a dictionary.
            #
            if isinstance(value, dict):
                raise KeyError(f"{item} -> {resp}")

            # Return elementary types
            #
            elif isinstance(value, str):
                return value
            elif isinstance(value, int):
                return value
            elif isinstance(value, float):
                return value

            # The result may be a list. If so, every lement of the list must be
            # checked for fault messages and repeat markers.
            #
            elif isinstance(value, list):
                value2 = []
                last = None

                for v in value:

                    # Dictionaries are special messages returned by the controller but everything
                    # else are regular values.
                    #
                    if not isinstance(v, dict):
                        value2.append(v)
                        last = v

                    # Handle {'repeatLast': 58}
                    #
                    elif 'repeatLast' in v:
                        value2 += [last] * v['repeatLast']

                    # Any faults cause a KeyError.
                    # {'faultCode': 4, 'faultString': 'Exception: Index out of range on access to item ...'}
                    #
                    elif 'faultCode' in v:
                        raise KeyError(f"{item} -> {resp}")

                    # Any other error.
                    #
                    else:
                        raise KeyError(f"{item} -> {resp}")
                   

            # Return the result list if it has not been done yet.
            #
            return value2
                



    def __setitem__(self, item, value):
        with xmlrpc.client.ServerProxy(self.url, transport=self.transport, verbose=DEBUG) as proxy:
            resp = proxy.db.set({item: value})
            if not isinstance(resp, dict):
                raise KeyError(f"{item} -> {resp}")
            elif resp.get('resultString', '') != 'OK':
                raise KeyError(f"{item} -> {resp}")


    def get(self, item, default=None):
        # WARNING: It is the caller's responsibility to set `default` correclt for tables:
        #          client.get('Di-Name:1-10', [None]*10)
        try:
            return self[item[0]]
        except KeyError:
            return default


# Aliases
#
SCX00 = SC200 = SC300 = SCx00
