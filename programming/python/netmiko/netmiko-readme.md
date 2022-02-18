# Netmiko


```python
# SIMPLE SCRIPT
import sys
import click

from netmiko import ConnectHandler

device = {
        'device_type':'cisco_ios',
        'ip':'192.168.1.100',
        'username':'grs',
        'password':''
        }
vlan20 = ["vlan 2", "int range fa1/0/2 - 48", "description THIS PORT IS IN VLAN 2"]

print("\n\n *** Configure VLAN 2")

connect = ConnectHandler(**device)
output = connect.send_config_set(vlan20)

print("\n\n *** Netmiko Python Script Execution Complete ***\n\n")
```

```python
# SIMPLE SCRIPT 2
import getpass
from netmiko import ConnectHandler

ip = raw_input("Target Switch: ")
user = raw_input("Enter your TACACS: ")
p = getpass.getpass()

# Functions setup 

def connect1(): 
        net_connect = ConnectHandler(device_type='cisco_ios', ip=ip, username=user, password=p
, global_delay_factor=.5, secret=p)
        #
        # Setup Terminal
        #
        print("! term length 0")
        net_connect.send_command("term length 0")
        # !
        # output 1
        # !
        print("! show ip intf. brief")
        o1 = net_connect.send_command("show ip interface brief")
        print(o1)
        # !
        # output 2
        # !
        print("! show run")
        o2 = net_connect.send_command("show run")
        print(o2)
        # !
        # output 3
        # !
        print("! show version")
        o3 = net_connect.send_command("show version")
        print(o3)
        # !
        # end of script cleanup
        # !
        print("! end script - term no length 0")
        net_connect.send_command("term no length 0")
        # !
        # DISCONNECT
        # !
        print("Disconnecting...")
        net_connect.disconnect()
        # end function   

connect1()
```

---
