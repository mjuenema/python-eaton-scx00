# python-eaton-scx00

SCX00.py is a module for reading and writing data from/to Eaton Power SC200 and SC300 Controllers.
I don't know whether it also works with the SC100 model as I don't have access to one.

The module implements a simple wrapper for the Eaton SCx00 XMLRPC interface.

No error checking is done and all XMLRPC errors are passed on to the caller.

**Status**: Works for me ;-)

Big thanks to 'The-Godfather' for having figured out how to make xmlrpc calls with cookies and 'GermainZ' for having asked the question on Stackoverflow. The (Safe)CookieTransport implementations below are based on their code.

The ``SCx00`` class provides dictionary style access to all data items.
```python
def __init__(self, controller, proto=None, port=0, username='', password=''):
    """
    
    Arguments:
    controller -- Hostname or IP Address of the controller.

    Keyword Arguments:
    username -- Username for authentication.
    password -- Password for authentication.
    port -- The port the controller listens on. Defaults to 443.
    proto -- Either 'http' or 'https'. Defaults to 'https'.
```


```python
>>> import scx00
>>> client = scx00.SCx00('10.1.2.3', proto='http')
```
Instances provides dictionary-style access to the data items of the controller.

```python
>>> client['Site-Name']
'Site-2'
```

Write access probbaly requires to authenticate first. Either provide username and password as keywork arguments when creating an instance or call the ``.login()`` method.

```python
>>> client.login('myusername', 'mypassword')
>>> client['Site-Name'] = 'Site-1'
>>> client['Site-Name']
Site-1
```

Returned values may have to be cast into their appropriate type.

The example below shows how to convert an integer into an IPv4 address. This actually works as IPv4 addresses area really just 32 bit integers.

```python
>>> client['IP-Address']
171017663
>>> import ipaddress
>>> ipaddress.IPv4Address(client['IP-Address'])
IPv4Address('10.49.133.191')
```

Enumerations are returned as their integer value. 

The example queries what SNMP version is enabled on the controller. The return value of 1 means that all supported SNMP versions are enabled.

```python
>>> client['SNMP-Access']
1
```

Boolean values are enumerations (0=Disabled, 1=Enabled) which fortunately can be directly converted into 
the proper Python type and value. 

```python
>>> client['HTTPS-Access']
1
>>> bool(client['HTTPS-Access'])
True
```

Date/time values are easy to convert, too.

```python
>>> client['Next-Battery-Test-Start-Time']
2147483647
>>> import datetime
>>> datetime.datetime.fromtimestamp(client['Next-Battery-Test-Start-Time'])
datetime.datetime(2038, 1, 19, 14, 14, 7)
```

Tabular can be accessed through a special slicing notation.

```python
>>> client['DI-Name:1-8']
['Digital Input 1',
 'Digital Input 2',
 'Digital Input 3',
 'Digital Input 4',
 'Digital Input 5',
 'Batt Fail',
 'Load Fuse Fail',
 'Battery Fuse Fail']
```

It is up to the user to provide valid values for the lower and upper bounds of a slice as these are passed varbatim to the controller's XMLRPC interface.

Some table indexes start with 0, others with 1. For example, 'DI-Name' is indexed starting with 1 and using the wrong slicing will raise an exception.

Individual entries can be accessed directly which is the only way to update an item in a table.

```python
>>> client['DI-Name:6']
Batt Fail
>>> client['DI-Name:6'] = 'Battery Fail'
>>> client['DI-Name:6']
Battery Fail
```
