## Communications


## Ports


## Ethernet


| Item | Type | SC200 | SC300 |
| ---- | ---- | ----- | ----- |
| IP&#x2011;Address | int (IPAddress) | yes | yes |
| Subnet&#x2011;Mask | int (IPAddress) | yes | yes |
| Gateway&#x2011;Address | int (IPAddress) | yes | yes |
| Host&#x2011;Name | str | yes | yes |

## Front Panel


| Item | Type |
| ---- | ---- |
| UI&#x2011;Access | (0)&#160;Unprotected</br>(1)&#160;Read&#160;Only</br>(2)&#160;PIN&#160;Protected |
| UI&#x2011;Access&#x2011;PIN | int (Unsigned16) |
| UI&#x2011;Language | str |
| Buzzer&#x2011;Tone | (0)&#160;None</br>(1)&#160;Startup</br>(2)&#160;Invalid&#160;Keypress</br>(3)&#160;Minor&#160;Alarm</br>(4)&#160;Major&#160;Alarm</br>(5)&#160;Urgent&#160;Popup |
| Current&#x2011;Keypress&#x2011;State | (0)&#160;None</br>(1)&#160;Up</br>(2)&#160;Down</br>(3)&#160;Esc</br>(4)&#160;Enter</br>(5)&#160;Info</br>(6)&#160;Left</br>(7)&#160;Right</br>(8)&#160;UpDown |
| Keypress&#x2011;State | (0)&#160;None</br>(1)&#160;Up</br>(2)&#160;Down</br>(3)&#160;Esc</br>(4)&#160;Enter</br>(5)&#160;Info</br>(6)&#160;Left</br>(7)&#160;Right</br>(8)&#160;UpDown |
| Current&#x2011;UI&#x2011;Selection | str |
| Display&#x2011;Contrast | int (Unsigned8) |
| Display&#x2011;Orientation | (0)&#160;Vertical</br>(1)&#160;Left</br>(2)&#160;Right |
| Main&#x2011;Screen&#x2011;Layout | (0)&#160;Two&#160;Large</br>(1)&#160;Three&#160;Small |
| Main&#x2011;Screen&#x2011;Item&#x2011;1 | (0)&#160;Bus&#160;Voltage</br>(1)&#160;Rectifier&#160;Current</br>(2)&#160;Load&#160;Current</br>(3)&#160;Battery&#160;Current</br>(4)&#160;Battery&#160;Temperature</br>(5)&#160;Load&#160;Power</br>(6)&#160;System&#160;Power</br>(7)&#160;Analog&#160;Input</br>(8)&#160;Ah&#160;Discharged |
| Main&#x2011;Screen&#x2011;Item&#x2011;1&#x2011;Index | int (Unsigned8) |
| Main&#x2011;Screen&#x2011;Item&#x2011;Value&#x2011;1&#x2011;Units | (0)&#160;No&#160;Units</br>(1)&#160;With&#160;Value</br>(2)&#160;With&#160;Label |
| Main&#x2011;Screen&#x2011;Item&#x2011;2 | (0)&#160;Bus&#160;Voltage</br>(1)&#160;Rectifier&#160;Current</br>(2)&#160;Load&#160;Current</br>(3)&#160;Battery&#160;Current</br>(4)&#160;Battery&#160;Temperature</br>(5)&#160;Load&#160;Power</br>(6)&#160;System&#160;Power</br>(7)&#160;Analog&#160;Input</br>(8)&#160;Ah&#160;Discharged |
| Main&#x2011;Screen&#x2011;Item&#x2011;2&#x2011;Index | int (Unsigned8) |
| Main&#x2011;Screen&#x2011;Item&#x2011;Value&#x2011;2&#x2011;Units | (0)&#160;No&#160;Units</br>(1)&#160;With&#160;Value</br>(2)&#160;With&#160;Label |
| Main&#x2011;Screen&#x2011;Item&#x2011;3 | (0)&#160;Bus&#160;Voltage</br>(1)&#160;Rectifier&#160;Current</br>(2)&#160;Load&#160;Current</br>(3)&#160;Battery&#160;Current</br>(4)&#160;Battery&#160;Temperature</br>(5)&#160;Load&#160;Power</br>(6)&#160;System&#160;Power</br>(7)&#160;Analog&#160;Input</br>(8)&#160;Ah&#160;Discharged |
| Main&#x2011;Screen&#x2011;Item&#x2011;3&#x2011;Index | int (Unsigned8) |
| Main&#x2011;Screen&#x2011;Item&#x2011;Value&#x2011;3&#x2011;Units | (0)&#160;No&#160;Units</br>(1)&#160;With&#160;Value</br>(2)&#160;With&#160;Label |

## Serial


| Item | Type |
| ---- | ---- |
| Enable&#x2011;Modem | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Modem&#x2011;Power&#x2011;Reset | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Modem&#x2011;Set&#x2011;Up&#x2011;String | str |
| Modem&#x2011;Auto&#x2011;Answer&#x2011;Rings | int (Unsigned8) |

## Callback


| Item | Type |
| ---- | ---- |
| Modem&#x2011;Maximum&#x2011;Retries | int (Unsigned8) |
| Modem&#x2011;Retry&#x2011;Interval | int (TimeIntervalInSeconds) |
| Alarm&#x2011;Report | (0)&#160;None</br>(1)&#160;Warnings&#160;And&#160;Above</br>(2)&#160;Minor&#160;And&#160;Above</br>(3)&#160;Major&#160;And&#160;Above</br>(4)&#160;Critical&#160;Only |
| Alarms&#x2011;Read | bool |

### Dial Out Number Table


| Item | Index | Type |
| ---- | ----- | ---- |
| Dial&#x2011;Out&#x2011;Number | 1-10 | str |

## SMS Notifications


### SMS Notification Table


| Item | Index | Type |
| ---- | ----- | ---- |
| SMS&#x2011;Phone&#x2011;Name | 1-8 | str |
| SMS&#x2011;Level | 1-8 | (1)&#160;Warnings&#160;And&#160;Above</br>(2)&#160;Minor&#160;And&#160;Above</br>(3)&#160;Major&#160;And&#160;Above</br>(4)&#160;None</br>(5)&#160;Critical&#160;Only |
| SMS&#x2011;Phone&#x2011;Number | 1-8 | str |
| SMS&#x2011;Prefix | 1-8 | str |

## Port Settings


| Item | Type |
| ---- | ---- |
| Baud&#x2011;Rate | (8)&#160;2400</br>(9)&#160;4800</br>(10)&#160;9600</br>(11)&#160;19200 |
| Parity | (0)&#160;None</br>(1)&#160;Odd</br>(2)&#160;Even |
| Stop&#x2011;Bits | (1)&#160;One</br>(2)&#160;Two |

## Protocols


## S3P


| Item | Type |
| ---- | ---- |
| S3P&#x2011;Access | (0)&#160;Disabled</br>(1)&#160;Enabled |
| S3P&#x2011;Address | int (Unsigned16) |
| S3P&#x2011;Write&#x2011;Access&#x2011;Password | str |
| Remote&#x2011;Access&#x2011;Level | (80)&#160;Read&#160;Only</br>(81)&#160;Read&#160;Write |
| Remote&#x2011;Access&#x2011;Login | str |

## MII


| Item | Type |
| ---- | ---- |
| MII&#x2011;Address | int (Unsigned8) |

## HTTP


| Item | Type |
| ---- | ---- |
| HTTP&#x2011;Access | (0)&#160;Disabled</br>(1)&#160;Enabled |
| HTTPS&#x2011;Access | (0)&#160;Disabled</br>(1)&#160;Enabled |

### Web User Table


| Item | Index | Type |
| ---- | ----- | ---- |
| User&#x2011;Active | 1-10 | bool |
| User&#x2011;Name | 1-10 | str |
| User&#x2011;Logon&#x2011;ID | 1-10 | str |
| User&#x2011;Logon&#x2011;Password | 1-10 | str |
| User&#x2011;Read | 1-10 | bool |
| User&#x2011;Write | 1-10 | bool |
| User&#x2011;Restore | 1-10 | bool |
| User&#x2011;Backup | 1-10 | bool |
| User&#x2011;Execute | 1-10 | bool |
| User&#x2011;Upgrade&#x2011;Firmware | 1-10 | bool |
| User&#x2011;Edit&#x2011;User&#x2011;List | 1-10 | bool |
| Current&#x2011;User&#x2011;Name | 1-10 | str |
| Current&#x2011;User&#x2011;Read | 1-10 | bool |
| Current&#x2011;User&#x2011;Write | 1-10 | bool |
| Current&#x2011;User&#x2011;Restore | 1-10 | bool |
| Current&#x2011;User&#x2011;Backup | 1-10 | bool |
| Current&#x2011;User&#x2011;Execute&#x2011;Commands | 1-10 | bool |
| Current&#x2011;User&#x2011;Upgrade&#x2011;Firmware | 1-10 | bool |
| Current&#x2011;User&#x2011;Edit&#x2011;User&#x2011;List | 1-10 | bool |

## SNMP


| Item | Type |
| ---- | ---- |
| SNMP&#x2011;Access | (0)&#160;Disabled</br>(1)&#160;All</br>(2)&#160;Read&#160;Only</br>(3)&#160;V3&#160;Only |
| Generic&#x2011;Traps&#x2011;Enable | (0)&#160;All</br>(1)&#160;Cold&#160;Start&#160;Trap&#160;Only</br>(2)&#160;None |
| SNMP&#x2011;Read&#x2011;Community | str |
| SNMP&#x2011;Write&#x2011;Community | str |
| Trap&#x2011;Version | (0)&#160;SNMP&#160;V1&#160;Trap</br>(1)&#160;SNMP&#160;V2&#160;Trap</br>(2)&#160;SNMP&#160;V3&#160;Trap |
| Enable&#x2011;Trap&#x2011;Repeat | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Trap&#x2011;Repeat&#x2011;Rate | int (TimeIntervalInMinutes) |
| Trap&#x2011;Format | (0)&#160;Eaton</br>(1)&#160;X.733 |
| SNMP&#x2011;Trap | int (Unsigned32) |
| Trap&#x2011;Alarm&#x2011;Number | int (Unsigned16) |
| Trap&#x2011;Alarm&#x2011;Name | str |
| Trap&#x2011;Additional&#x2011;Text | str |
| Trap&#x2011;Alarm&#x2011;Keep&#x2011;Severity | (1)&#160;Critical</br>(2)&#160;Major</br>(3)&#160;Minor</br>(4)&#160;Warning</br>(5)&#160;Cleared |
| SNMPv3&#x2011;User&#x2011;Name | str |
| SNMPv3&#x2011;SHA&#x2011;Password | str |
| SNMPv3&#x2011;DES&#x2011;Password | str |

### SNMP Trap Receiver Table


| Item | Index | Type |
| ---- | ----- | ---- |
| Trap&#x2011;Receiver&#x2011;Level | 1-8 | (1)&#160;Warnings&#160;And&#160;Above</br>(2)&#160;Minor&#160;And&#160;Above</br>(3)&#160;Major&#160;And&#160;Above</br>(4)&#160;None</br>(5)&#160;Critical&#160;Only |
| Trap&#x2011;Receiver&#x2011;Name | 1-8 | str |
| Trap&#x2011;Receiver&#x2011;Community | 1-8 | str |
| Trap&#x2011;Receiver&#x2011;Mode | 1-8 | (1)&#160;Normal&#160;Traps</br>(2)&#160;Acknowledged&#160;Summary&#160;Trap |
| Trap&#x2011;Receiver&#x2011;IP&#x2011;Address | 1-8 | int (IPAddress) |
| Trap&#x2011;Receiver&#x2011;Port | 1-8 | int (Unsigned16) |
| System&#x2011;Object&#x2011;ID | 1-8 | str |
| Trap&#x2011;Alarm&#x2011;Origin | 1-8 | (0)&#160;System&#160;Alarm</br>(1)&#160;AI&#160;High</br>(2)&#160;AI&#160;Low</br>(3)&#160;DI</br>(4)&#160;Smart&#160;Alarm |

## Serial Server


| Item | Type |
| ---- | ---- |
| Serial&#x2011;Server&#x2011;Access | (0)&#160;Disabled</br>(1)&#160;Enabled |

## Modbus


| Item | Type |
| ---- | ---- |
| Modbus&#x2011;Address | int (Unsigned8) |
| Modbus&#x2011;Access | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Modbus&#x2011;Interface&#x2011;Version | int (Unsigned16) |
| Modbus&#x2011;Bus&#x2011;Message&#x2011;Count | int (Unsigned16) |
| Modbus&#x2011;Bus&#x2011;Communication&#x2011;Error&#x2011;Count | int (Unsigned16) |
| Modbus&#x2011;Slave&#x2011;Exception&#x2011;Error&#x2011;Count | int (Unsigned16) |
| Modbus&#x2011;Slave&#x2011;Message&#x2011;Count | int (Unsigned16) |
| Modbus&#x2011;Slave&#x2011;No&#x2011;Response&#x2011;Count | int (Unsigned16) |
| Modbus&#x2011;Bus&#x2011;Character&#x2011;Overrun&#x2011;Count | int (Unsigned16) |

## SMTP


| Item | Type |
| ---- | ---- |
| Email&#x2011;Notifications | (0)&#160;Disabled</br>(1)&#160;Enabled |
| SMTP&#x2011;Server&#x2011;IP&#x2011;Address | int (IPAddress) |
| SMTP&#x2011;Server&#x2011;Port | int (Unsigned16) |
| Email&#x2011;Return&#x2011;Address | str |
| Email&#x2011;Subject&#x2011;Prefix | str |

### Email Receiver Table


| Item | Index | Type |
| ---- | ----- | ---- |
| Email&#x2011;Receiver&#x2011;Level | 1-6 | (1)&#160;Warnings&#160;And&#160;Above</br>(2)&#160;Minor&#160;And&#160;Above</br>(3)&#160;Major&#160;And&#160;Above</br>(4)&#160;None</br>(5)&#160;Critical&#160;Only |
| Email&#x2011;Receiver&#x2011;Address | 1-6 | str |
| Email&#x2011;Receiver&#x2011;Delay | 1-6 | int (TimeIntervalInSeconds) |
| SMTP&#x2011;Result | 1-6 | int (Unsigned16) |

## CSPs


| Item | Type |
| ---- | ---- |
| CSP4&#x2011;Access | (0)&#160;Disabled</br>(1)&#160;Enabled |

## CSP2


| Item | Type |
| ---- | ---- |
| Enable&#x2011;CSP2&#x2011;Stack | (0)&#160;Disabled</br>(1)&#160;Enabled |
| TPE&#x2011;Mode | (0)&#160;Physical</br>(1)&#160;Virtual |
| Time&#x2011;Zone&#x2011;Offset | int (TimeIntervalInMinutes) |
| CSP2&#x2011;Time | int (datetime) |
| CSP2&#x2011;Alarm&#x2011;Report&#x2011;IP&#x2011;Address | int (IPAddress) |
| CSP2&#x2011;Alarm&#x2011;Report&#x2011;IP&#x2011;Port | int (Unsigned16) |
| CSP2&#x2011;Key | str |
| TPE&#x2011;Id | int (Unsigned16) |
| CSP2&#x2011;SW&#x2011;Version | str |
| CSP2&#x2011;T1_317&#x2011;Protocol&#x2011;Version | str |
| CSP3&#x2011;Access | (0)&#160;Disabled</br>(1)&#160;Enabled |

## Control Processes


| Item | Type |
| ---- | ---- |
| Control&#x2011;State | (0)&#160;Normal</br>(1)&#160;Equalize</br>(2)&#160;Fast&#160;Charge</br>(3)&#160;Battery&#160;Test |

## System Voltages


| Item | Type |
| ---- | ---- |
| Float&#x2011;Voltage | Float |
| Maximum&#x2011;System&#x2011;Voltage | Float |
| Minimum&#x2011;System&#x2011;Voltage | Float |
| Operating&#x2011;Voltage | Float |
| Target&#x2011;Voltage | Float |
| Base&#x2011;Voltage | Float |

## Active Voltage Control


| Item | Type |
| ---- | ---- |
| Enable&#x2011;Active&#x2011;Voltage&#x2011;Control | (0)&#160;Disabled</br>(1)&#160;Enabled |
| AVC&#x2011;State | (115)&#160;Disabled</br>(116)&#160;Inoperative</br>(117)&#160;Active</br>(118)&#160;Lost&#160;Control</br>(119)&#160;In&#160;Deadband |
| AVC&#x2011;Offset | Float |

## Temperature Compensation


| Item | Type |
| ---- | ---- |
| Enable&#x2011;Temperature&#x2011;Compensation | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Temperature&#x2011;Compensation&#x2011;Slope | Float |
| Temperature&#x2011;Compensation&#x2011;Reference&#x2011;Temperature | Float |
| Temperature&#x2011;Compensation&#x2011;Lower&#x2011;Limit | Float |
| Temperature&#x2011;Compensation&#x2011;Upper&#x2011;Limit | Float |
| Temperature&#x2011;Compensation&#x2011;State | (80)&#160;Disabled</br>(81)&#160;Inoperative</br>(82)&#160;Active |
| Temperature&#x2011;Compensation&#x2011;Allowed | (190)&#160;Process&#160;Active</br>(191)&#160;Available&#160;To&#160;Start</br>(192)&#160;Cannot&#160;Start&#160;-&#160;Controller&#160;Busy</br>(193)&#160;Cannot&#160;Start&#160;-&#160;Process&#160;Disabled</br>(194)&#160;Cannot&#160;Start&#160;-&#160;Alarms&#160;Active</br>(195)&#160;Cannot&#160;Start&#160;-&#160;Sensor&#160;Failed</br>(196)&#160;Cannot&#160;Start&#160;-&#160;Battery&#160;Not&#160;Charged</br>(197)&#160;Cannot&#160;Start&#160;-&#160;No&#160;Rectifiers&#160;Available</br>(198)&#160;Cannot&#160;Start&#160;-&#160;Rectifier&#160;OVSD</br>(199)&#160;Cannot&#160;Start&#160;-&#160;No&#160;Battery&#160;Configured</br>(200)&#160;Cannot&#160;Start&#160;-&#160;Load&#160;Current&#160;Too&#160;Low</br>(201)&#160;Cannot&#160;Start&#160;-&#160;AC&#160;Failed</br>(202)&#160;Manual&#160;Stop</br>(203)&#160;Cannot&#160;Start&#160;-&#160;Battery&#160;Not&#160;Discharged</br>(204)&#160;Cannot&#160;Start&#160;-&#160;AC&#160;State&#160;Unavailable</br>(205)&#160;Cannot&#160;Start&#160;-&#160;System&#160;Overloaded |
| Temperature&#x2011;Compensation&#x2011;Offset&#x2011;Voltage | Float |

## Equalize


| Item | Type |
| ---- | ---- |
| Enable&#x2011;Equalize | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Equalize&#x2011;Voltage | Float |
| Equalize&#x2011;Duration | int (TimeIntervalInMinutes) |
| Periodic&#x2011;Equalize&#x2011;First&#x2011;Date&#x2011;Time | int (datetime) |
| Equalize&#x2011;Interval | int (TimeIntervalInDays) |
| Equalize&#x2011;State | (0)&#160;Disabled</br>(1)&#160;Active</br>(2)&#160;Inactive</br>(3)&#160;Pending |
| Equalize&#x2011;Remaining&#x2011;Time | int (TimeIntervalInSeconds) |
| Next&#x2011;Equalize&#x2011;Start&#x2011;Time | int (datetime) |
| Equalize&#x2011;Start&#x2011;Allowed | (190)&#160;Process&#160;Active</br>(191)&#160;Available&#160;To&#160;Start</br>(192)&#160;Cannot&#160;Start&#160;-&#160;Controller&#160;Busy</br>(193)&#160;Cannot&#160;Start&#160;-&#160;Process&#160;Disabled</br>(194)&#160;Cannot&#160;Start&#160;-&#160;Alarms&#160;Active</br>(195)&#160;Cannot&#160;Start&#160;-&#160;Sensor&#160;Failed</br>(196)&#160;Cannot&#160;Start&#160;-&#160;Battery&#160;Not&#160;Charged</br>(197)&#160;Cannot&#160;Start&#160;-&#160;No&#160;Rectifiers&#160;Available</br>(198)&#160;Cannot&#160;Start&#160;-&#160;Rectifier&#160;OVSD</br>(199)&#160;Cannot&#160;Start&#160;-&#160;No&#160;Battery&#160;Configured</br>(200)&#160;Cannot&#160;Start&#160;-&#160;Load&#160;Current&#160;Too&#160;Low</br>(201)&#160;Cannot&#160;Start&#160;-&#160;AC&#160;Failed</br>(202)&#160;Manual&#160;Stop</br>(203)&#160;Cannot&#160;Start&#160;-&#160;Battery&#160;Not&#160;Discharged</br>(204)&#160;Cannot&#160;Start&#160;-&#160;AC&#160;State&#160;Unavailable</br>(205)&#160;Cannot&#160;Start&#160;-&#160;System&#160;Overloaded |
| Can&#x2011;Stop&#x2011;Equalize | (0)&#160;Able&#160;To&#160;Stop</br>(1)&#160;Cannot&#160;Stop&#160;-&#160;Battery&#160;Too&#160;Discharged</br>(2)&#160;Cannot&#160;Stop&#160;-&#160;Bus&#160;Voltage&#160;Too&#160;Low</br>(3)&#160;Cannot&#160;Stop&#160;-&#160;Process&#160;Not&#160;Running |
| Equalize&#x2011;Offset&#x2011;Voltage | Float |

## Fast Charge


| Item | Type |
| ---- | ---- |
| Enable&#x2011;Fast&#x2011;Charge | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Fast&#x2011;Charge&#x2011;Voltage | Float |
| Fast&#x2011;Charge&#x2011;Maximum&#x2011;Duration | int (TimeIntervalInMinutes) |
| Fast&#x2011;Charge&#x2011;Ampere&#x2011;Hour&#x2011;Threshold | int (Unsigned8) |
| Fast&#x2011;Charge&#x2011;Voltage&#x2011;Threshold | Float |
| Fast&#x2011;Charge&#x2011;Recharge&#x2011;Percentage | int (Unsigned8) |
| Fast&#x2011;Charge&#x2011;Ampere&#x2011;Hour&#x2011;Stop&#x2011;Threshold | int (Unsigned8) |
| Fast&#x2011;Charge&#x2011;State | (0)&#160;Disabled</br>(1)&#160;Active</br>(2)&#160;Inactive</br>(3)&#160;Pending |
| Can&#x2011;Stop&#x2011;Fast&#x2011;Charge | (0)&#160;Able&#160;To&#160;Stop</br>(1)&#160;Cannot&#160;Stop&#160;-&#160;Battery&#160;Too&#160;Discharged</br>(2)&#160;Cannot&#160;Stop&#160;-&#160;Bus&#160;Voltage&#160;Too&#160;Low</br>(3)&#160;Cannot&#160;Stop&#160;-&#160;Process&#160;Not&#160;Running |
| Fast&#x2011;Charge&#x2011;Maximum&#x2011;Time&#x2011;Remaining | int (TimeIntervalInSeconds) |
| Fast&#x2011;Charge&#x2011;Offset&#x2011;Voltage | Float |
| Fast&#x2011;Charge&#x2011;Start&#x2011;Allowed | (190)&#160;Process&#160;Active</br>(191)&#160;Available&#160;To&#160;Start</br>(192)&#160;Cannot&#160;Start&#160;-&#160;Controller&#160;Busy</br>(193)&#160;Cannot&#160;Start&#160;-&#160;Process&#160;Disabled</br>(194)&#160;Cannot&#160;Start&#160;-&#160;Alarms&#160;Active</br>(195)&#160;Cannot&#160;Start&#160;-&#160;Sensor&#160;Failed</br>(196)&#160;Cannot&#160;Start&#160;-&#160;Battery&#160;Not&#160;Charged</br>(197)&#160;Cannot&#160;Start&#160;-&#160;No&#160;Rectifiers&#160;Available</br>(198)&#160;Cannot&#160;Start&#160;-&#160;Rectifier&#160;OVSD</br>(199)&#160;Cannot&#160;Start&#160;-&#160;No&#160;Battery&#160;Configured</br>(200)&#160;Cannot&#160;Start&#160;-&#160;Load&#160;Current&#160;Too&#160;Low</br>(201)&#160;Cannot&#160;Start&#160;-&#160;AC&#160;Failed</br>(202)&#160;Manual&#160;Stop</br>(203)&#160;Cannot&#160;Start&#160;-&#160;Battery&#160;Not&#160;Discharged</br>(204)&#160;Cannot&#160;Start&#160;-&#160;AC&#160;State&#160;Unavailable</br>(205)&#160;Cannot&#160;Start&#160;-&#160;System&#160;Overloaded |

## Battery Current Limit


| Item | Type |
| ---- | ---- |
| Enable&#x2011;Battery&#x2011;Current&#x2011;Limit | (0)&#160;Disabled</br>(1)&#160;Enabled |
| BCL&#x2011;Limit | int (Unsigned8) |
| BCL&#x2011;Engine&#x2011;Run&#x2011;Limit | int (Unsigned8) |
| BCL&#x2011;State | (110)&#160;Disabled</br>(111)&#160;Inoperative</br>(112)&#160;Active</br>(113)&#160;Inactive</br>(114)&#160;Lost&#160;Control</br>(115)&#160;In&#160;Deadband</br>(116)&#160;Pending |
| BCL&#x2011;Offset&#x2011;Voltage | Float |

## Battery Test


| Item | Type |
| ---- | ---- |
| Enable&#x2011;Battery&#x2011;Test | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Battery&#x2011;Test&#x2011;First&#x2011;Date&#x2011;Time | int (datetime) |
| Battery&#x2011;Test&#x2011;Duration | int (TimeIntervalInMinutes) |
| Battery&#x2011;Test&#x2011;Termination&#x2011;Voltage | Float |
| Battery&#x2011;Test&#x2011;Interval | int (TimeIntervalInDays) |
| Battery&#x2011;Test&#x2011;State | (95)&#160;Disabled</br>(96)&#160;Inactive</br>(97)&#160;Active</br>(98)&#160;Failed</br>(99)&#160;Locked&#160;Out |
| Battery&#x2011;Test&#x2011;Remaining&#x2011;Time | int (TimeIntervalInSeconds) |
| Next&#x2011;Battery&#x2011;Test&#x2011;Start&#x2011;Time | int (datetime) |
| Battery&#x2011;Test&#x2011;Lockout&#x2011;Remaining | int (TimeIntervalInSeconds) |
| Battery&#x2011;Test&#x2011;Start&#x2011;Allowed | (190)&#160;Process&#160;Active</br>(191)&#160;Available&#160;To&#160;Start</br>(192)&#160;Cannot&#160;Start&#160;-&#160;Controller&#160;Busy</br>(193)&#160;Cannot&#160;Start&#160;-&#160;Process&#160;Disabled</br>(194)&#160;Cannot&#160;Start&#160;-&#160;Alarms&#160;Active</br>(195)&#160;Cannot&#160;Start&#160;-&#160;Sensor&#160;Failed</br>(196)&#160;Cannot&#160;Start&#160;-&#160;Battery&#160;Not&#160;Charged</br>(197)&#160;Cannot&#160;Start&#160;-&#160;No&#160;Rectifiers&#160;Available</br>(198)&#160;Cannot&#160;Start&#160;-&#160;Rectifier&#160;OVSD</br>(199)&#160;Cannot&#160;Start&#160;-&#160;No&#160;Battery&#160;Configured</br>(200)&#160;Cannot&#160;Start&#160;-&#160;Load&#160;Current&#160;Too&#160;Low</br>(201)&#160;Cannot&#160;Start&#160;-&#160;AC&#160;Failed</br>(202)&#160;Manual&#160;Stop</br>(203)&#160;Cannot&#160;Start&#160;-&#160;Battery&#160;Not&#160;Discharged</br>(204)&#160;Cannot&#160;Start&#160;-&#160;AC&#160;State&#160;Unavailable</br>(205)&#160;Cannot&#160;Start&#160;-&#160;System&#160;Overloaded |
| Battery&#x2011;Test&#x2011;Offset&#x2011;Voltage | Float |
| Can&#x2011;Stop&#x2011;Battery&#x2011;Test | (0)&#160;Able&#160;To&#160;Stop</br>(1)&#160;Cannot&#160;Stop&#160;-&#160;Battery&#160;Too&#160;Discharged</br>(2)&#160;Cannot&#160;Stop&#160;-&#160;Bus&#160;Voltage&#160;Too&#160;Low</br>(3)&#160;Cannot&#160;Stop&#160;-&#160;Process&#160;Not&#160;Running |

## Low Voltage Disconnect


| Item | Type |
| ---- | ---- |
| LVD&#x2011;Inhibit&#x2011;Period | int (TimeIntervalInSeconds) |
| Allow&#x2011;Front&#x2011;Panel&#x2011;LVD&#x2011;Control | bool |

### LVD Table


| Item | Index | Type |
| ---- | ----- | ---- |
| LVD&#x2011;Inhibited | 1-16 | bool |
| LVD&#x2011;State | 1-16 | (0)&#160;Idle</br>(1)&#160;Connected</br>(2)&#160;Disconnected</br>(3)&#160;Manual</br>(4)&#160;No&#160;Contactors |
| Enable&#x2011;LVD&#x2011;Voltage&#x2011;Disconnect | 1-16 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| LVD&#x2011;Disconnect&#x2011;Voltage | 1-16 | Float |
| LVD&#x2011;Reconnect&#x2011;Voltage | 1-16 | Float |
| LVD&#x2011;Recognition&#x2011;Period | 1-16 | int (TimeIntervalInSeconds) |
| Enable&#x2011;LVD&#x2011;AC&#x2011;Timer | 1-16 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| LVD&#x2011;AC&#x2011;Timer&#x2011;Disconnect&#x2011;Delay | 1-16 | int (TimeIntervalInMinutes) |
| Enable&#x2011;LVD&#x2011;SA&#x2011;Disconnect | 1-16 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| LVD&#x2011;SA&#x2011;Disconnect&#x2011;Index | 1-16 | int (Unsigned8) |
| Enable&#x2011;LVD&#x2011;Chained&#x2011;To&#x2011;Previous | 1-16 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| LVDC&#x2011;Characterization&#x2011;Result | 1-16 | (0)&#160;Not&#160;Run</br>(1)&#160;Running</br>(2)&#160;Success</br>(3)&#160;No&#160;Lock</br>(4)&#160;Disabled</br>(5)&#160;Comms&#160;Lost</br>(6)&#160;Busy</br>(7)&#160;Mapping&#160;Error</br>(8)&#160;Contactor&#160;Fault |

### LVDC Table


| Item | Index | Type |
| ---- | ----- | ---- |
| LVDC&#x2011;State | 1-16 | (0)&#160;Connected</br>(1)&#160;Disconnected</br>(2)&#160;Failed</br>(3)&#160;Missing</br>(4)&#160;Disabled</br>(5)&#160;Conflict</br>(6)&#160;Not&#160;Characterized |
| Enable&#x2011;LVDC | 1-16 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| LVDC&#x2011;LVD&#x2011;Mapping | 1-16 | int (Unsigned8) |
| LVDC&#x2011;IOB&#x2011;Number | 1-16 | int (Unsigned8) |
| LVDC&#x2011;IOB&#x2011;LVD&#x2011;Number | 1-16 | int (Unsigned8) |
| LVDC&#x2011;Type | 1-16 | (0)&#160;Normally&#160;Open</br>(1)&#160;Normally&#160;Closed |
| LVDC&#x2011;Pull&#x2011;In&#x2011;Value | 1-16 | Float |
| LVDC&#x2011;Hold&#x2011;In&#x2011;Value | 1-16 | Float |
| LVDC&#x2011;LVD&#x2011;Version&#x2011;Value | 1-16 | int (Unsigned16) |

## Generator Control


| Item | Type |
| ---- | ---- |
| Generator&#x2011;Fail&#x2011;Alarm&#x2011;Recognition&#x2011;Period | int (TimeIntervalInSeconds) |
| AC&#x2011;Supply&#x2011;State | (0)&#160;Ok</br>(1)&#160;Failed</br>(2)&#160;Unavailable</br>(3)&#160;Missing |
| Generator&#x2011;State | (85)&#160;Not&#160;Running</br>(86)&#160;Running</br>(87)&#160;Unavailable</br>(88)&#160;Missing |
| Generator&#x2011;Control&#x2011;Relay | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |
| Generator&#x2011;Startup&#x2011;Wiring | (0)&#160;Indirect&#160;Start</br>(1)&#160;Direct&#160;Start |
| Fuel&#x2011;Level | Float |
| Fuel&#x2011;Tank&#x2011;Volume | Float |
| Manual&#x2011;Generator&#x2011;Run&#x2011;Time | int (TimeIntervalInMinutes) |
| Generator&#x2011;Run&#x2011;Time&#x2011;Remaining | int (TimeIntervalInSeconds) |
| Generator&#x2011;Backup&#x2011;Time | int (TimeIntervalInSeconds) |
| Tank&#x2011;Empty&#x2011;Date&#x2011;Time | int (datetime) |
| Generator&#x2011;Refuel&#x2011;Date | int (datetime) |
| Generator&#x2011;Refuel&#x2011;Volume | Float |
| Automatic&#x2011;Generator&#x2011;Control&#x2011;Mode | (0)&#160;Disabled</br>(1)&#160;Fast&#160;Charge&#160;Only</br>(2)&#160;Fast&#160;Charge&#160;Or&#160;Equalize</br>(3)&#160;Every&#160;Mains&#160;Failure |

## Logs


## Event Log


| Item | Type |
| ---- | ---- |
| Number&#x2011;Of&#x2011;Event&#x2011;Log&#x2011;Entries | int (Unsigned16) |
| Event&#x2011;Log&#x2011;Earliest&#x2011;Index | int (Unsigned32) |
| Event&#x2011;Log&#x2011;Latest&#x2011;Index | int (Unsigned32) |
| Event&#x2011;Log&#x2011;Version | int (Unsigned16) |

## Event Log Entries


| Item | Index | Type |
| ---- | ----- | ---- |
| Event&#x2011;Log&#x2011;Time | [Event&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Event&#x2011;Log&#x2011;Latest&#x2011;Index] | int (datetime) |
| Event&#x2011;Log&#x2011;Type | [Event&#x2011;Log&#x2011;Earliest&#x2011;Index]-Event&#x2011;Log&#x2011;Latest&#x2011;Index] | (0)&#160;No&#160;Event</br>(1)&#160;Start&#160;Up</br>(2)&#160;Alarm&#160;Activation</br>(3)&#160;Alarm&#160;Deactivation</br>(4)&#160;Configuration&#160;Change</br>(5)&#160;Control&#160;Process&#160;Start</br>(6)&#160;Control&#160;Process&#160;End</br>(7)&#160;Rectifier&#160;Shutdown</br>(8)&#160;Rectifier&#160;Restart</br>(9)&#160;Logs&#160;Cleared</br>(10)&#160;Clock&#160;Change&#160;From</br>(11)&#160;Clock&#160;Change&#160;To</br>(12)&#160;Reserved</br>(13)&#160;AI&#160;High&#160;Activation</br>(14)&#160;AI&#160;High&#160;Deactivation</br>(15)&#160;AI&#160;Low&#160;Activation</br>(16)&#160;AI&#160;Low&#160;Deactivation</br>(17)&#160;DI&#160;Activation</br>(18)&#160;DI&#160;Deactivation</br>(19)&#160;Reserved&#160;2</br>(20)&#160;Reserved&#160;3</br>(21)&#160;DO&#160;Control&#160;Manual&#160;Active</br>(22)&#160;DO&#160;Control&#160;Automatic</br>(23)&#160;Smart&#160;Alarm&#160;Activation</br>(24)&#160;Smart&#160;Alarm&#160;Deactivation</br>(25)&#160;DO&#160;Control&#160;Manual&#160;Inactive</br>(26)&#160;Battery&#160;State&#160;Reset</br>(27)&#160;Fast&#160;Charge&#160;Manual&#160;Stop</br>(28)&#160;Equalize&#160;Manual&#160;Start</br>(29)&#160;Equalize&#160;Manual&#160;Stop</br>(30)&#160;Generator&#160;Start</br>(31)&#160;Generator&#160;Stop |
| Event&#x2011;Information | [Event&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Event&#x2011;Log&#x2011;Latest&#x2011;Index] | int (Unsigned32) |
| Event&#x2011;Information&#x2011;String | [Event&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Event&#x2011;Log&#x2011;Latest&#x2011;Index] | str |

## Data Log


| Item | Type |
| ---- | ---- |
| Data&#x2011;Log&#x2011;Normal&#x2011;Interval | int (TimeIntervalInSeconds) |
| Data&#x2011;Log&#x2011;Off&#x2011;Normal&#x2011;Interval | int (TimeIntervalInSeconds) |
| Data&#x2011;Log&#x2011;Off&#x2011;Normal&#x2011;Offset&#x2011;Voltage | Float |
| Number&#x2011;Of&#x2011;Data&#x2011;Log&#x2011;Entries | int (Unsigned16) |
| Data&#x2011;Log&#x2011;Earliest&#x2011;Index | int (Unsigned32) |
| Data&#x2011;Log&#x2011;Latest&#x2011;Index | int (Unsigned32) |
| Data&#x2011;Log&#x2011;Version | int (Unsigned16) |

## Data Log Entries

[Data&#x2011;Log&#x2011;Latest&#x2011;Index]

| Item | Index | Type |
| ---- | ----- | ---- |
| Data&#x2011;Log&#x2011;Time | [Data&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Data&#x2011;Log&#x2011;Latest&#x2011;Index] | int (datetime) |
| Data&#x2011;Log&#x2011;AC&#x2011;Voltage | [Data&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Data&#x2011;Log&#x2011;Latest&#x2011;Index] | int (Unsigned16) |
| Data&#x2011;Log&#x2011;Bus&#x2011;Voltage | [Data&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Data&#x2011;Log&#x2011;Latest&#x2011;Index] | Float |
| Data&#x2011;Log&#x2011;Load&#x2011;Current | [Data&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Data&#x2011;Log&#x2011;Latest&#x2011;Index] | Float |
| Data&#x2011;Log&#x2011;Rectifier&#x2011;Current | [Data&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Data&#x2011;Log&#x2011;Latest&#x2011;Index] | Float |
| Data&#x2011;Log&#x2011;Battery&#x2011;Current | [Data&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Data&#x2011;Log&#x2011;Latest&#x2011;Index] | Float |
| Data&#x2011;Log&#x2011;Battery&#x2011;Temperature | [Data&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Data&#x2011;Log&#x2011;Latest&#x2011;Index] | Float |
| Data&#x2011;Log&#x2011;Ah&#x2011;Discharged | [Data&#x2011;Log&#x2011;Earliest&#x2011;Index]-[Data&#x2011;Log&#x2011;Latest&#x2011;Index] | Float |

## Misc


## Database Control


| Item | Type |
| ---- | ---- |
| Reset&#x2011;Community | (1)&#160;Monitor&#160;Unique</br>(2)&#160;System&#160;Unique</br>(3)&#160;System&#160;Shared |
| Database&#x2011;State | (410)&#160;Unavailable</br>(411)&#160;Available</br>(412)&#160;Locked</br>(413)&#160;Updating |
| Configuration&#x2011;Hash | int (Unsigned32) |
| Database&#x2011;Read&#x2011;State | (0)&#160;Not&#160;Yet&#160;Read</br>(1)&#160;Successful&#160;Read</br>(2)&#160;Successful&#160;Read&#160;With&#160;Recoverable&#160;Errors</br>(3)&#160;File&#160;Not&#160;Found</br>(4)&#160;File&#160;Corrupt |
| Database&#x2011;Write&#x2011;State | (0)&#160;Not&#160;Yet&#160;Written</br>(1)&#160;Successful&#160;Write</br>(2)&#160;Write&#160;Failed</br>(3)&#160;Writing |
| Configuration&#x2011;Flash&#x2011;Write&#x2011;Enable | bool |
| Bus&#x2011;Sensor&#x2011;Fail&#x2011;Triggered | bool |
| Battery&#x2011;Test&#x2011;Fail&#x2011;Triggered | bool |
| Battery&#x2011;Current&#x2011;Sensor&#x2011;Failed | bool |

## ModBus AC Metering


| Item | Type |
| ---- | ---- |
| AC&#x2011;Frequency | Float |
| AC&#x2011;Energy | Float |

## AC Phase Values


| Item | Type |
| ---- | ---- |
| AC&#x2011;Phase&#x2011;Voltage | Float |
| AC&#x2011;Phase&#x2011;Current | Float |
| AC&#x2011;Phase&#x2011;Real&#x2011;Power | Float |
| AC&#x2011;Phase&#x2011;Reactive&#x2011;Power | Float |
| AC&#x2011;Phase&#x2011;Apparent&#x2011;Power | Float |
| AC&#x2011;Phase&#x2011;Power&#x2011;Factor | 3 |
| AC&#x2011;Phase&#x2011;Harmonic&#x2011;Distortion | Float |

## Time


| Item | Type |
| ---- | ---- |
| Controller&#x2011;Time | int (datetime) |
| TestRTCTime | int (datetime) |

## SNTP


| Item | Type |
| ---- | ---- |
| Poll&#x2011;Interval | int (TimeIntervalInSeconds) |
| Primary&#x2011;Address | int (IPAddress) |
| Backup&#x2011;Address | int (IPAddress) |
| UDP&#x2011;Port | int (Unsigned16) |
| SNTP&#x2011;Last&#x2011;Update | int (datetime) |

## Identity


| Item | Type |
| ---- | ---- |
| Slave&#x2011;Type | (0)&#160;Undefined</br>(1)&#160;SM20</br>(2)&#160;SM50</br>(3)&#160;SM30</br>(4)&#160;SM30&#160;SLAVE</br>(5)&#160;IOM</br>(6)&#160;CBC</br>(7)&#160;WEIR</br>(8)&#160;SM35</br>(9)&#160;NES&#160;BATTERY&#160;TRAY</br>(10)&#160;SM30&#160;SLAVE&#160;FRONT&#160;PORT</br>(11)&#160;SM60</br>(12)&#160;SM40</br>(13)&#160;SM70_IOB</br>(14)&#160;SM70</br>(15)&#160;SM45_IOB</br>(16)&#160;SM45</br>(17)&#160;SM65</br>(18)&#160;SC200 |
| Software&#x2011;Version | str |
| Interface&#x2011;Version | int (Unsigned16) |
| Compatible&#x2011;Interface&#x2011;Version | int (Unsigned16) |
| Manufacturer&#x2011;Name | str |
| System&#x2011;Type | str |
| Contact | str |
| System&#x2011;Manufacturer | str |
| System&#x2011;Location | str |
| System&#x2011;Serial&#x2011;Number | str |
| Site&#x2011;Name | str |
| Site&#x2011;Address | str |
| Site&#x2011;Notes | str |
| Configuration&#x2011;Name | str |
| Ethernet&#x2011;MAC&#x2011;Address | str |

### Software Modules Table


| Item | Index | Type |
| ---- | ----- | ---- |
| Software&#x2011;Module&#x2011;Versions | 1-64 | 2 |
| Software&#x2011;Module&#x2011;Names | 1-64 | str |
| LDR&#x2011;Software&#x2011;Version | 1-64 | str |
| Serial&#x2011;Number | 1-64 | str |
| Hardware&#x2011;Version | 1-64 | str |
| Run&#x2011;Up&#x2011;Date | 1-64 | str |
| Subversion&#x2011;Revision | 1-64 | int (Unsigned32) |

## RXP


| Item | Type |
| ---- | ---- |
| RP&#x2011;Bus&#x2011;Load | Float |

## RXP Slave Values


| Item | Index | Type |
| ---- | ----- | ---- |
| RXP&#x2011;Slave&#x2011;Command&#x2011;Set | 1-142 | int (Unsigned32) |
| RXP&#x2011;Slave&#x2011;Type | 1-142 | (0)&#160;Unknown</br>(1)&#160;IOB</br>(2)&#160;Rectifier |
| RXP&#x2011;Slave&#x2011;Serial&#x2011;Number | 1-142 | int (Unsigned32) |
| RXP&#x2011;Slave&#x2011;Registration&#x2011;State | 1-142 | (0)&#160;Not&#160;Detected</br>(1)&#160;Detected</br>(2)&#160;Registered</br>(3)&#160;Comms&#160;Lost</br>(4)&#160;Missing</br>(5)&#160;Rebooting |
| RXP&#x2011;Slave&#x2011;Name | 1-142 | str |
| RXP&#x2011;BOM&#x2011;Revision | 1-142 | str |
| RXP&#x2011;Software&#x2011;Version | 1-142 | str |
| Identify&#x2011;RXP&#x2011;Slave | 1-142 | bool |
| RXP&#x2011;Slave&#x2011;Is&#x2011;Identifying | 1-142 | bool |

## IOBs


| Item | Type |
| ---- | ---- |
| Num&#x2011;IOB&#x2011;Shadows | int (Unsigned8) |

## IOB Values


| Item | Index | Type |
| ---- | ----- | ---- |
| IOB&#x2011;Serial&#x2011;Number&#x2011;Map | 1-16 | int (Unsigned32) |
| IOB&#x2011;RXP&#x2011;Slave&#x2011;Table&#x2011;Index | 1-16 | int (Unsigned8) |
| IOB&#x2011;Registration&#x2011;State | 1-16 | (0)&#160;Not&#160;Detected</br>(1)&#160;Detected</br>(2)&#160;Registered</br>(3)&#160;Comms&#160;Lost</br>(4)&#160;Missing</br>(5)&#160;Rebooting |
| IOB&#x2011;Number&#x2011;Of&#x2011;Voltages | 1-16 | int (Unsigned8) |
| IOB&#x2011;Number&#x2011;Of&#x2011;Currents | 1-16 | int (Unsigned8) |
| IOB&#x2011;Number&#x2011;Of&#x2011;Temperatures | 1-16 | int (Unsigned8) |
| IOB&#x2011;Number&#x2011;Of&#x2011;Digital&#x2011;Inputs | 1-16 | int (Unsigned8) |
| IOB&#x2011;Number&#x2011;Of&#x2011;Relays | 1-16 | int (Unsigned8) |
| IOB&#x2011;Number&#x2011;Of&#x2011;LVDs | 1-16 | int (Unsigned8) |
| IOB&#x2011;Status | 1-16 | int (Unsigned8) |
| Num&#x2011;Rectifier&#x2011;Shadows | 1-16 | int (Unsigned8) |
| RXP&#x2011;Comms&#x2011;Filter | 1-16 | int (Unsigned32) |
| RXP&#x2011;Comms&#x2011;Mask | 1-16 | int (Unsigned32) |

## Batteries


| Item | Type |
| ---- | ---- |
| Cells&#x2011;Per&#x2011;String | int (Unsigned8) |
| Battery&#x2011;Capacity | int (Unsigned32) |
| Battery&#x2011;Current&#x2011;Sensor&#x2011;Fail&#x2011;Recognition&#x2011;Period | int (TimeIntervalInSeconds) |
| Fast&#x2011;Charge&#x2011;Ah&#x2011;Discharged | Float |
| Battery&#x2011;Charge&#x2011;State | (100)&#160;Float</br>(101)&#160;Discharge</br>(102)&#160;Charge</br>(103)&#160;Unavailable |
| Battery&#x2011;State&#x2011;Threshold | Float |

## Midpoint Battery Monitoring


| Item | Type |
| ---- | ---- |
| MPM&#x2011;Lockout&#x2011;Period | int (TimeIntervalInMinutes) |
| MPM&#x2011;Convergence&#x2011;Period | int (TimeIntervalInMinutes) |
| String&#x2011;Fail&#x2011;Recognition&#x2011;Period | int (TimeIntervalInMinutes) |
| MPM&#x2011;Start&#x2011;Threshold | Float |
| MPM&#x2011;Stable&#x2011;Threshold | Float |
| MPM&#x2011;State | (0)&#160;Unable&#160;To&#160;Start</br>(1)&#160;Locked&#160;Out</br>(2)&#160;Converging</br>(3)&#160;Stable</br>(4)&#160;Disabled |
| Time&#x2011;In&#x2011;This&#x2011;State | int (TimeIntervalInMinutes) |
| Current&#x2011;MPM&#x2011;Threshold | Float |

### Midpoint Monitoring String Table


| Item | Index | Type |
| ---- | ----- | ---- |
| String&#x2011;Name | 1-24 | str |
| Midpoint&#x2011;Voltage | 1-24 | Float |
| Imbalance&#x2011;Percent | 1-24 | Float |
| String&#x2011;State | 1-24 | (0)&#160;OK</br>(1)&#160;Pending&#160;Fail</br>(2)&#160;Failed</br>(3)&#160;Unavailable</br>(4)&#160;Not&#160;Configured |
| Abnormal&#x2011;Time | 1-24 | int (TimeIntervalInMinutes) |
| Reference&#x2011;Voltage | 1-24 | Float |

## Battery Time Remaining


| Item | Type |
| ---- | ---- |
| BTR&#x2011;State | (0)&#160;Inoperative</br>(1)&#160;Inactive</br>(2)&#160;Active</br>(3)&#160;Characterizing</br>(4)&#160;Waiting</br>(5)&#160;Not&#160;Characterized |
| BTR&#x2011;Time&#x2011;Remaining | int (TimeIntervalInSeconds) |
| BTR&#x2011;End&#x2011;Voltage | Float |
| BTR&#x2011;Characterization&#x2011;End&#x2011;Voltage | Float |
| BTR&#x2011;End&#x2011;Time | int (datetime) |
| BTR&#x2011;Wait&#x2011;Time | int (TimeIntervalInSeconds) |
| BTR&#x2011;Characterization&#x2011;Rate | Float |
| BTR&#x2011;State&#x2011;Of&#x2011;Health | int (Unsigned8) |
| BTR&#x2011;Automatic&#x2011;Characterization | (0)&#160;Disabled</br>(1)&#160;Enabled |
| BTR&#x2011;Characterization&#x2011;Delay | int (TimeIntervalInMinutes) |
| BTR&#x2011;Characterization&#x2011;Start | int (TimeIntervalInSeconds) |
| Battery&#x2011;Type | str |
| BTR&#x2011;Characterization&#x2011;Possible | (0)&#160;Yes</br>(1)&#160;Characterization&#160;Active</br>(2)&#160;Not&#160;Fully&#160;Charged</br>(3)&#160;AC&#160;Not&#160;Present</br>(4)&#160;Low&#160;Load</br>(5)&#160;End&#160;Voltage&#160;Too&#160;Low</br>(6)&#160;BCL&#160;Disabled</br>(7)&#160;Busy</br>(8)&#160;Battery&#160;Test&#160;Failed</br>(9)&#160;Sensor&#160;Failed</br>(10)&#160;No&#160;Battery&#160;Configured</br>(11)&#160;Battery&#160;Already&#160;Characterized |
| BTR&#x2011;Characterization&#x2011;Result | (0)&#160;Not&#160;Yet&#160;Run</br>(1)&#160;Sensor&#160;Failed</br>(2)&#160;Not&#160;Fully&#160;Charged</br>(3)&#160;Unstable&#160;Battery&#160;Current</br>(4)&#160;Voltage&#160;Step&#160;Detected</br>(5)&#160;Complete</br>(6)&#160;Updated</br>(7)&#160;User&#160;Canceled |
| BTR&#x2011;Characterization&#x2011;Time | int (datetime) |

## Battery Characterization Data


| Item | Index | Type |
| ---- | ----- | ---- |
| Battery&#x2011;Characterization&#x2011;Sample | 1-25 | Float |

## Rectifiers


| Item | Type |
| ---- | ---- |
| Number&#x2011;Of&#x2011;Registered&#x2011;Rectifiers | int (Unsigned8) |
| Number&#x2011;Of&#x2011;Rectifiers&#x2011;Failed | int (Unsigned8) |
| Number&#x2011;Of&#x2011;Rectifiers&#x2011;Comms&#x2011;Lost | int (Unsigned8) |
| OVSD&#x2011;Set&#x2011;Point | Float |
| Ramp&#x2011;Up&#x2011;Slope | int (Unsigned8) |
| Rectifier&#x2011;Shutdown&#x2011;Mode | (0)&#160;Disabled</br>(1)&#160;Manual</br>(2)&#160;Automatic |
| Rectifier&#x2011;Current&#x2011;Limit | int (Unsigned8) |
| Enable&#x2011;Current&#x2011;Share | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Mii&#x2011;Rect&#x2011;State&#x2011;Has&#x2011;Changed | bool |
| Mii&#x2011;Rect&#x2011;Fail&#x2011;Alarm&#x2011;State&#x2011;Has&#x2011;Changed | bool |
| Rectifier&#x2011;Start&#x2011;Up&#x2011;Delay | int (TimeIntervalInSeconds) |
| AC&#x2011;Rectifier&#x2011;Current&#x2011;Limit | int (Unsigned8) |
| Sum&#x2011;Of&#x2011;Rectifier&#x2011;Current&#x2011;Limits | Float |

## Rectifier Values


| Item | Index | Type |
| ---- | ----- | ---- |
| Rectifier&#x2011;RXP&#x2011;Slave&#x2011;Table&#x2011;Index | 1-126 | int (Unsigned8) |
| Rectifier&#x2011;Failed&#x2011;State | 1-126 | (0)&#160;Not&#160;Failed</br>(1)&#160;Bad&#160;Status</br>(2)&#160;Bad&#160;Output |
| Rectifier&#x2011;Deduced&#x2011;Status | 1-126 | int (Unsigned32) |
| Rectifier&#x2011;Power&#x2011;Limit | 1-126 | Float |
| Rectifier&#x2011;Registration&#x2011;State | 1-126 | (0)&#160;Not&#160;Detected</br>(1)&#160;Detected</br>(2)&#160;Registered</br>(3)&#160;Comms&#160;Lost</br>(4)&#160;Missing</br>(5)&#160;Rebooting |
| Rectifier&#x2011;Reported&#x2011;Current | 1-126 | Float |
| Rectifier&#x2011;Reported&#x2011;AC&#x2011;Voltage | 1-126 | Float |
| Rectifier&#x2011;Heatsink&#x2011;Temperature | 1-126 | Float |
| Rectifier&#x2011;Maximum&#x2011;Power&#x2011;Limit | 1-126 | int (Unsigned16) |
| Rectifier&#x2011;Maximum&#x2011;Current&#x2011;Limit | 1-126 | int (Unsigned8) |
| Shutdown&#x2011;Rectifier | 1-126 | bool |
| Rectifier&#x2011;Has&#x2011;Been&#x2011;Shutdown | 1-126 | bool |
| Load&#x2011;Based&#x2011;Run&#x2011;Time | 1-126 | int (TimeIntervalInSeconds) |
| Rectifier&#x2011;Output&#x2011;Is&#x2011;Limited | 1-126 | bool |
| Rectifier&#x2011;Capabilities | 1-126 | int (Unsigned8) |
| Rectifier&#x2011;Reported&#x2011;Voltage | 1-126 | Float |
| Rectifier&#x2011;Maximum&#x2011;OVSD&#x2011;Set&#x2011;Point | 1-126 | Float |
| Rectifier&#x2011;Minimum&#x2011;OVSD&#x2011;Set&#x2011;Point | 1-126 | Float |
| Rectifier&#x2011;Status | 1-126 | int (Unsigned8) |
| Rectifier&#x2011;Serial&#x2011;Number | 1-126 | int (Unsigned32) |
| Rectifier&#x2011;Failed | 1-126 | int (Unsigned8) |
| Rectifier&#x2011;Shutdown | 1-126 | int (Unsigned8) |
| Rectifier&#x2011;Maximum&#x2011;AC&#x2011;Current&#x2011;Limit | 1-126 | Float |
| Rectifier&#x2011;Output&#x2011;Power | 1-126 | Float |
| Rectifier&#x2011;Power&#x2011;Share&#x2011;Voltage&#x2011;Offset | 1-126 | Float |
| Rectifier&#x2011;Phase&#x2011;1 | 1-126 | Float |
| Rectifier&#x2011;Phase&#x2011;2 | 1-126 | Float |
| Rectifier&#x2011;Phase&#x2011;3 | 1-126 | Float |
| Is&#x2011;Three&#x2011;Phase&#x2011;System | 1-126 | bool |

## Load Based Rectifier Shutdown


| Item | Type |
| ---- | ---- |
| Rect&#x2011;Cycle&#x2011;Low&#x2011;Threshold | int (Unsigned8) |
| Rect&#x2011;Cycle&#x2011;High&#x2011;Threshold | int (Unsigned8) |
| Rect&#x2011;Cycle&#x2011;Interval | int (TimeIntervalInMinutes) |
| LBRS&#x2011;State | (80)&#160;Disabled</br>(81)&#160;Inactive</br>(82)&#160;Active |
| LBRS&#x2011;Number&#x2011;Of&#x2011;Shutdown&#x2011;Rectifiers | null |

## Alarms


| Item | Type |
| ---- | ---- |
| Alarm&#x2011;Recognition&#x2011;Period | int (TimeIntervalInSeconds) |
| Enable&#x2011;Audible&#x2011;Alarm&#x2011;Indication | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Summary&#x2011;Alarm&#x2011;Critical | bool |
| Summary&#x2011;Alarm&#x2011;Major | bool |
| Summary&#x2011;Alarm&#x2011;Minor | bool |
| Summary&#x2011;Alarm&#x2011;Warning | bool |

## System Alarms


| Item | Type |
| ---- | ---- |
| In&#x2011;Discharge&#x2011;Alarm&#x2011;Condition | (0)&#160;Always</br>(1)&#160;Only&#160;While&#160;AC&#160;Present |
| Low&#x2011;Load&#x2011;Threshold | Float |

### Alarm Table


| Item | Index | Type |
| ---- | ----- | -----|
| Alarm&#x2011;Send&#x2011;Trap | 0-59 | bool |
| Alarm&#x2011;Severity | 0-59 | (0)&#160;Disabled</br>(1)&#160;Critical</br>(2)&#160;Major</br>(3)&#160;Minor</br>(4)&#160;Warning</br>(5)&#160;Control |
| Alarm&#x2011;DO&#x2011;Mapping&#x2011;A | 0-59 | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |
| Alarm&#x2011;DO&#x2011;Mapping&#x2011;B | 0-59 | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |
| Alarm&#x2011;Notes | 0-59 | str |
| Alarm&#x2011;Name |v str |
| Alarm&#x2011;State | 0-59 | (0)&#160;Not&#160;Active</br>(1)&#160;Active&#160;Warning</br>(2)&#160;Active&#160;Major</br>(3)&#160;Active&#160;Minor</br>(4)&#160;Reserved</br>(5)&#160;Active&#160;Critical</br>(6)&#160;Active&#160;Control |
| Alarm&#x2011;State&#x2011;Change&#x2011;Time | 0-59 | int (datetime) |
| Low&#x2011;Float&#x2011;Threshold | 0-59 | Float |
| Enable&#x2011;Low&#x2011;Float&#x2011;Tracking | 0-59 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| High&#x2011;Float&#x2011;Threshold | 0-59 | Float |
| Enable&#x2011;High&#x2011;Float&#x2011;Tracking | 0-59 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| High&#x2011;Load&#x2011;Threshold | 0-59 | Float |
| AC&#x2011;Fail&#x2011;Recognition&#x2011;Period | 0-59 | int (TimeIntervalInSeconds) |
| System&#x2011;Overload&#x2011;Threshold | 0-59 | int (Unsigned8) |
| System&#x2011;Overload&#x2011;Recognition&#x2011;Period | 0-59 | int (TimeIntervalInMinutes) |
| System&#x2011;Overload&#x2011;Type | 0-59 | (0)&#160;Total&#160;Capacity</br>(1)&#160;Redundancy |
| Battery&#x2011;Temperature&#x2011;High&#x2011;Threshold | 0-59 | Signed8 |
| Battery&#x2011;Temperature&#x2011;Low&#x2011;Threshold | 0-59 | Signed8 |
| Nominal&#x2011;AC&#x2011;Voltage | 0-59 | Float |
| AC&#x2011;Phase&#x2011;Fail&#x2011;Threshold | 0-59 | int (Unsigned8) |
| AC&#x2011;Phase&#x2011;Voltage&#x2011;Threshold | 0-59 | int (Unsigned8) |
| Nominal&#x2011;AC&#x2011;Frequency | 0-59 | Float |
| AC&#x2011;Frequency&#x2011;Threshold | 0-59 | int (Unsigned8) |

## Smart Alarms


### Source Alarm Table


| Item | Index | Type |
| ---- | ----- | ---- |
| Source&#x2011;Alarm&#x2011;Status | 1-64 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Source&#x2011;Alarm&#x2011;Trigger&#x2011;State | 1-64 | (0)&#160;Active</br>(1)&#160;Inactive</br>(2)&#160;Cycle</br>(3)&#160;Invalid |
| Source&#x2011;Alarm&#x2011;Mapping | 1-64 | int (Unsigned8) |
| Source&#x2011;Alarm&#x2011;Logic | 1-64 | (0)&#160;EQUAL</br>(1)&#160;NOT |
| Source&#x2011;Trigger | 1-64 | (0)&#160;Triggered</br>(1)&#160;Active |
| Source&#x2011;Alarm&#x2011;Type | 1-64 | (0)&#160;System&#160;Alarm</br>(1)&#160;AI&#160;High</br>(2)&#160;AI&#160;Low</br>(3)&#160;DI</br>(4)&#160;Smart&#160;Alarm |
| Source&#x2011;Alarm&#x2011;Index | 1-64 | int (Unsigned8) |

### Source Schedule Table


| Item | Index | Type |
| ---- | ----- | ---- |
| Source&#x2011;Schedule&#x2011;Status | 1-20 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Is&#x2011;Source&#x2011;Schedule&#x2011;Active | 1-20 | bool |
| Source&#x2011;Schedule&#x2011;Mapping | 1-20 | int (Unsigned8) |
| Source&#x2011;Schedule&#x2011;First&#x2011;Date&#x2011;Time | 1-20 | int (datetime) |
| Source&#x2011;Schedule&#x2011;Duration | 1-20 | int (TimeIntervalInMinutes) |
| Source&#x2011;Schedule&#x2011;Interval | 1-20 | int (TimeIntervalInMinutes) |
| Source&#x2011;Schedule&#x2011;Repetitions | 1-20 | int (Unsigned32) |
| Source&#x2011;Schedule&#x2011;Next | 1-20 | int (datetime) |
| Source&#x2011;Schedule&#x2011;End | 1-20 | int (datetime) |

### System Value Source Table


| Item | Index | Type |
| ---- | ----- | ---- |
| System&#x2011;Value&#x2011;Source&#x2011;Status | 1-20 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| Is&#x2011;System&#x2011;Value&#x2011;Source&#x2011;Active | 1-20 | bool |
| System&#x2011;Value&#x2011;Source&#x2011;Mapping | 1-20 | int (Unsigned8) |
| System&#x2011;Value&#x2011;Source&#x2011;Threshold&#x2011;Type | 1-20 | (0)&#160;High</br>(1)&#160;Low |
| System&#x2011;Value&#x2011;Source&#x2011;Input | 1-20 | Float |
| System&#x2011;Value&#x2011;Source&#x2011;Value | 1-20 | (0)&#160;Bus&#160;Voltage</br>(1)&#160;Rectifier&#160;Current</br>(2)&#160;Load&#160;Current</br>(3)&#160;Battery&#160;Current</br>(4)&#160;Battery&#160;Temperature</br>(5)&#160;Load&#160;Power</br>(6)&#160;System&#160;Power</br>(7)&#160;Ah&#160;Discharged</br>(8)&#160;Number&#160;Of&#160;Rectifiers&#160;Failed</br>(9)&#160;Number&#160;Of&#160;Rectifiers&#160;Comms&#160;Lost</br>(10)&#160;AC&#160;Voltage</br>(11)&#160;Battery&#160;Time&#160;Remaining</br>(12)&#160;Alternative&#160;Source&#160;Current</br>(13)&#160;Highest&#160;Rectifier&#160;Heatsink&#160;Temperature</br>(14)&#160;Fuel&#160;Level</br>(15)&#160;Generator&#160;Backup&#160;Time</br>(16)&#160;Fuel&#160;Remaining&#160;Time |
| System&#x2011;Value&#x2011;Source&#x2011;Threshold | 1-20 | Float |
| System&#x2011;Value&#x2011;Source&#x2011;Hysteresis | 1-20 | Float |

### Smart Alarm Table


| Item | Index | Type |
| ---- | ----- | ---- |
| Smart&#x2011;Alarm&#x2011;Name | 1-32 | str |
| Smart&#x2011;Alarm&#x2011;State | 1-32 | (0)&#160;Not&#160;Active</br>(1)&#160;Active&#160;Warning</br>(2)&#160;Active&#160;Major</br>(3)&#160;Active&#160;Minor</br>(4)&#160;Reserved</br>(5)&#160;Active&#160;Critical</br>(6)&#160;Active&#160;Control |
| Smart&#x2011;Alarm&#x2011;State&#x2011;Change&#x2011;Time | 1-32 | int (datetime) |
| Smart&#x2011;Alarm&#x2011;Severity | 1-32 | (0)&#160;Disabled</br>(1)&#160;Critical</br>(2)&#160;Major</br>(3)&#160;Minor</br>(4)&#160;Warning</br>(5)&#160;Control |
| Smart&#x2011;Alarm&#x2011;Operator | 1-32 | (0)&#160;AND</br>(1)&#160;OR</br>(2)&#160;XOR |
| Smart&#x2011;Alarm&#x2011;Recognition&#x2011;Period | 1-32 | int (TimeIntervalInSeconds) |
| Smart&#x2011;Alarm&#x2011;Deactivation&#x2011;Recognition&#x2011;Period | 1-32 | int (TimeIntervalInSeconds) |
| Smart&#x2011;Alarm&#x2011;Send&#x2011;Trap | 1-32 | bool |
| Smart&#x2011;Alarm&#x2011;Group | 1-32 | int (Unsigned8) |
| Smart&#x2011;Alarm&#x2011;Notes | 1-32 | str |
| Smart&#x2011;Alarm&#x2011;DO&#x2011;Mapping&#x2011;A | 1-32 | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |
| Smart&#x2011;Alarm&#x2011;DO&#x2011;Mapping&#x2011;B | 1-32 | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |

## Analogue Inputs


| Item | Type |
| ---- | ---- |
| Bus&#x2011;Voltage | Float |
| Battery&#x2011;Current | Float |
| Internal&#x2011;Battery&#x2011;Current | Float |
| Load&#x2011;Current | Float |
| Internal&#x2011;Load&#x2011;Current | Float |
| Rectifier&#x2011;Current | Float |
| Internal&#x2011;Rectifier&#x2011;Current | Float |
| Sum&#x2011;Of&#x2011;Reported&#x2011;Rectifier&#x2011;Currents | Float |
| Alternative&#x2011;Source&#x2011;Current | Float |
| Internal&#x2011;Alternative&#x2011;Source&#x2011;Current | Float |
| System&#x2011;Has&#x2011;AES | bool |
| Load&#x2011;Power | Float |
| System&#x2011;Power | int (Unsigned8) |
| AC&#x2011;Voltage | Float |
| Battery&#x2011;Temperature | Float |
| Highest&#x2011;Rectifier&#x2011;Heatsink&#x2011;Temperature | Float |
| Phase&#x2011;1 | Float |
| Phase&#x2011;2 | Float |
| Phase&#x2011;3 | Float |

### Analog Input Table


| Item | Index | Type |
| ---- | ----- | ---- |
| AI&#x2011;High&#x2011;Send&#x2011;Trap | 1-48 | bool |
| AI&#x2011;Low&#x2011;Send&#x2011;Trap | 1-48 | bool |
| AI&#x2011;Name | 1-48 | str |
| AI&#x2011;Status | 1-48 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| AI&#x2011;Units | 1-48 | (30)&#160;None</br>(31)&#160;Volts</br>(32)&#160;Milli&#160;Amps</br>(33)&#160;Amps</br>(34)&#160;Kilo&#160;Amps</br>(35)&#160;degree&#160;celsius</br>(36)&#160;Kilo&#160;Watts</br>(37)&#160;Percent</br>(38)&#160;Volts&#160;AC</br>(39)&#160;Volts&#160;DC</br>(40)&#160;Amps&#160;AC</br>(41)&#160;Amps&#160;DC</br>(42)&#160;Litre</br>(43)&#160;Litre&#160;Per&#160;Sec</br>(44)&#160;Cubic&#160;Meter&#160;Per&#160;Hour</br>(45)&#160;Pascal</br>(46)&#160;Kilo&#160;Pascal</br>(47)&#160;mmH2O</br>(48)&#160;Percent&#160;Relative&#160;Humidity</br>(49)&#160;RPM</br>(50)&#160;Hertz</br>(51)&#160;Kilo&#160;Volt&#160;Amps</br>(52)&#160;Kilo&#160;Watt&#160;Hour |
| AI&#x2011;IOB&#x2011;Number | 1-48 | int (Unsigned8) |
| AI&#x2011;IOB&#x2011;AI&#x2011;Number | 1-48 | int (Unsigned8) |
| AI&#x2011;Gain | 1-48 | Float |
| AI&#x2011;Offset | 1-48 | Float |
| AI&#x2011;Function | 1-48 | (1)&#160;User&#160;Defined</br>(2)&#160;Bus&#160;Voltage</br>(3)&#160;Battery&#160;Temperature</br>(4)&#160;Battery&#160;Current</br>(5)&#160;Load&#160;Current</br>(6)&#160;Rectifier&#160;Current</br>(7)&#160;Battery&#160;Midpoint</br>(8)&#160;Reverse&#160;Battery&#160;Detect</br>(9)&#160;Alternative&#160;Energy&#160;Source&#160;Current</br>(10)&#160;Fuel&#160;Level |
| AI&#x2011;Hysteresis | 1-48 | Float |
| AI&#x2011;High&#x2011;Threshold | 1-48 | Float |
| AI&#x2011;High&#x2011;Severity | 1-48 | (0)&#160;Disabled</br>(1)&#160;Critical</br>(2)&#160;Major</br>(3)&#160;Minor</br>(4)&#160;Warning</br>(5)&#160;Control |
| AI&#x2011;High&#x2011;DO&#x2011;Mapping&#x2011;A | 1-48 | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |
| AI&#x2011;High&#x2011;DO&#x2011;Mapping&#x2011;B | 1-48 | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |
| AI&#x2011;Low&#x2011;Threshold | 1-48 | Float |
| AI&#x2011;Low&#x2011;Severity | 1-48 | (0)&#160;Disabled</br>(1)&#160;Critical</br>(2)&#160;Major</br>(3)&#160;Minor</br>(4)&#160;Warning</br>(5)&#160;Control |
| AI&#x2011;Low&#x2011;DO&#x2011;Mapping&#x2011;A | 1-48 | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |
| AI&#x2011;Low&#x2011;DO&#x2011;Mapping&#x2011;B | 1-48 | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |
| AI&#x2011;Group | 1-48 | int (Unsigned8) |
| AI&#x2011;High&#x2011;Notes | 1-48 | str |
| AI&#x2011;Low&#x2011;Notes | 1-48 | str |
| AI&#x2011;Value | 1-48 | Float |
| AI&#x2011;High&#x2011;State | 1-48 | (0)&#160;Not&#160;Active</br>(1)&#160;Active&#160;Warning</br>(2)&#160;Active&#160;Major</br>(3)&#160;Active&#160;Minor</br>(4)&#160;Reserved</br>(5)&#160;Active&#160;Critical</br>(6)&#160;Active&#160;Control |
| AI&#x2011;High&#x2011;State&#x2011;Change&#x2011;Time | 1-48 | int (datetime) |
| AI&#x2011;Low&#x2011;State | 1-48 | (0)&#160;Not&#160;Active</br>(1)&#160;Active&#160;Warning</br>(2)&#160;Active&#160;Major</br>(3)&#160;Active&#160;Minor</br>(4)&#160;Reserved</br>(5)&#160;Active&#160;Critical</br>(6)&#160;Active&#160;Control |
| AI&#x2011;Low&#x2011;State&#x2011;Change&#x2011;Time | 1-48 | int (datetime) |

## Digital Inputs


## System States


| Item | Type |
| ---- | ---- |
| Battery&#x2011;Fuse&#x2011;Fail | (0)&#160;Ok</br>(1)&#160;Failed</br>(2)&#160;Unavailable</br>(3)&#160;Missing |
| Fan&#x2011;Fail | (0)&#160;Ok</br>(1)&#160;Failed</br>(2)&#160;Unavailable</br>(3)&#160;Missing |
| AC&#x2011;Fail | (0)&#160;Ok</br>(1)&#160;Failed</br>(2)&#160;Unavailable</br>(3)&#160;Missing |
| Mains&#x2011;Fail | (0)&#160;Ok</br>(1)&#160;Failed</br>(2)&#160;Unavailable</br>(3)&#160;Missing |
| MOV&#x2011;Fail | (0)&#160;Ok</br>(1)&#160;Failed</br>(2)&#160;Unavailable</br>(3)&#160;Missing |
| Load&#x2011;Fuse&#x2011;Fail | (0)&#160;Ok</br>(1)&#160;Failed</br>(2)&#160;Unavailable</br>(3)&#160;Missing |
| Cabinet&#x2011;Fan&#x2011;Fail | (0)&#160;Ok</br>(1)&#160;Failed</br>(2)&#160;Unavailable</br>(3)&#160;Missing |
| Phase&#x2011;Fail | (0)&#160;Ok</br>(1)&#160;Failed</br>(2)&#160;Unavailable</br>(3)&#160;Missing |

### Digital Input Table


| Item | Index | Type |
| ---- | ----- | ---- |
| DI&#x2011;Send&#x2011;Trap | 1-108 | bool |
| DI&#x2011;Name | 1-108 | str |
| DI&#x2011;Status | 1-108 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| DI&#x2011;IOB&#x2011;Number | 1-108 | int (Unsigned8) |
| DI&#x2011;IOB&#x2011;DI&#x2011;Number | 1-108 | int (Unsigned8) |
| DI&#x2011;Severity | 1-108 | (0)&#160;Disabled</br>(1)&#160;Critical</br>(2)&#160;Major</br>(3)&#160;Minor</br>(4)&#160;Warning</br>(5)&#160;Control |
| DI&#x2011;Recognition&#x2011;Period | 1-108 | int (TimeIntervalInSeconds) |
| DI&#x2011;Deactivation&#x2011;Recognition&#x2011;Period | 1-108 | int (TimeIntervalInSeconds) |
| DI&#x2011;DO&#x2011;Mapping&#x2011;A | 1-108 | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |
| DI&#x2011;DO&#x2011;Mapping&#x2011;B | 1-108 | (0)&#160;None</br>(1)&#160;Digital&#160;Output&#160;1</br>(2)&#160;Digital&#160;Output&#160;2</br>(3)&#160;Digital&#160;Output&#160;3</br>(4)&#160;Digital&#160;Output&#160;4</br>(5)&#160;Digital&#160;Output&#160;5</br>(6)&#160;Digital&#160;Output&#160;6</br>(7)&#160;Digital&#160;Output&#160;7</br>(8)&#160;Digital&#160;Output&#160;8</br>(9)&#160;Digital&#160;Output&#160;9</br>(10)&#160;Digital&#160;Output&#160;10</br>(11)&#160;Digital&#160;Output&#160;11</br>(12)&#160;Digital&#160;Output&#160;12</br>(13)&#160;Digital&#160;Output&#160;13</br>(14)&#160;Digital&#160;Output&#160;14</br>(15)&#160;Digital&#160;Output&#160;15</br>(16)&#160;Digital&#160;Output&#160;16</br>(17)&#160;Digital&#160;Output&#160;17</br>(18)&#160;Digital&#160;Output&#160;18</br>(19)&#160;Digital&#160;Output&#160;19</br>(20)&#160;Digital&#160;Output&#160;20</br>(21)&#160;Digital&#160;Output&#160;21</br>(22)&#160;Digital&#160;Output&#160;22</br>(23)&#160;Digital&#160;Output&#160;23</br>(24)&#160;Digital&#160;Output&#160;24</br>(25)&#160;Digital&#160;Output&#160;25</br>(26)&#160;Digital&#160;Output&#160;26</br>(27)&#160;Digital&#160;Output&#160;27</br>(28)&#160;Digital&#160;Output&#160;28</br>(29)&#160;Digital&#160;Output&#160;29</br>(30)&#160;Digital&#160;Output&#160;30</br>(31)&#160;Digital&#160;Output&#160;31</br>(32)&#160;Digital&#160;Output&#160;32 |
| DI&#x2011;Function | 1-108 | (1)&#160;User&#160;Defined</br>(2)&#160;Battery&#160;Fuse&#160;Fail</br>(3)&#160;Load&#160;Fuse&#160;Fail</br>(4)&#160;MOV&#160;Fail</br>(5)&#160;ACD&#160;Fan&#160;Fail</br>(6)&#160;Cabinet&#160;Fan&#160;Fail</br>(7)&#160;Start&#160;Battery&#160;Test</br>(8)&#160;Start&#160;Equalize</br>(9)&#160;Engine&#160;Run</br>(10)&#160;AC&#160;Fail</br>(11)&#160;Phase&#160;Fail</br>(12)&#160;Mains&#160;Fail |
| DI&#x2011;Active&#x2011;State | 1-108 | (2)&#160;Closed</br>(3)&#160;Open |
| DI&#x2011;Group | 1-108 | int (Unsigned8) |
| DI&#x2011;Notes | 1-108 | str |
| DI&#x2011;Value | 1-108 | (1)&#160;Missing</br>(2)&#160;Closed</br>(3)&#160;Open</br>(4)&#160;Disabled |
| DI&#x2011;State | 1-108 | (0)&#160;Not&#160;Active</br>(1)&#160;Active&#160;Warning</br>(2)&#160;Active&#160;Major</br>(3)&#160;Active&#160;Minor</br>(4)&#160;Reserved</br>(5)&#160;Active&#160;Critical</br>(6)&#160;Active&#160;Control |
| DI&#x2011;State&#x2011;Change&#x2011;Time | 1-108 | int (datetime) |

## Digital Outputs


### Digital Output Table


| Item | Index | Type |
| ---- | ----- | ---- |
| DO&#x2011;Status | 1-32 | (0)&#160;Disabled</br>(1)&#160;Enabled |
| DO&#x2011;Name | 1-32 | str |
| DO&#x2011;IOB&#x2011;Number | 1-32 | int (Unsigned8) |
| DO&#x2011;IOB&#x2011;DO&#x2011;Number | 1-32 | int (Unsigned8) |
| DO&#x2011;Active&#x2011;State | 1-32 | (0)&#160;De&#160;Energized</br>(1)&#160;Energized |
| DO&#x2011;Group | 1-32 | int (Unsigned8) |
| DO&#x2011;State | 1-32 | (0)&#160;Active</br>(1)&#160;Inactive</br>(2)&#160;Missing</br>(3)&#160;Disabled</br>(4)&#160;Conflict |
| DO&#x2011;Control&#x2011;State | 1-32 | (0)&#160;Active</br>(1)&#160;Automatic</br>(2)&#160;Inactive |

