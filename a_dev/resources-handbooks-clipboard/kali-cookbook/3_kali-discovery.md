# Kali Linux Discovery

## Contents

* Using Scapy to perform host discovery (layers 2/3/4)
* Using Nmap to perform host discovery (layers 2/3/4)
* Using ARPing to perform host discovery (layer 2)
* Using netdiscover to perform host discovery (layer 2)
* Using Metasploit to perform host discovery (layer 2)
* Using ICMP to perform host discovery
* Using fping to perform host discovery
* Using hping3 to perform host discovery (layers 3/4)

## Using Scapy to perform host discovery (layers 2/3/4)

Scapy is a power interactive Python tool that can capture, anaylze, manipulate and create protocol-compliant network traffic, which can then be injected into a network.

Here we will demonstrate how to use Scapy to perform discover in layer 2, 3, and 4.

1. Use Scapy to perform ARP discovery
2. Use Scapy to inkect and analyze ICMP traffic (L3)
3. Use Scapy to perform L4 discovery using TCP & UDP

### Scapy in Action

Python scripting can be effective in automating redundant tasks while using Scapy. With Python and Scapy we can create a loop that will iterate through a list of IP addresses and send ARP requests to each one.

[Here we have a script](./tools/scapy/arp-request-loop.py) that can be used to perform layer 2 discovery on a sequential series of hosts. Let's examine the code more closely.

```python
#!/usr/bin/python

import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 2:
    print("Usage - ./arp_disc.py [interface]")
    print("Example - ./arp_disc.py eth0")
    print("Example will perform an ARP scan of the local subnet to which eth0 is assigned")
    sys.exit()

interface = str(sys.argv[1])
ip = subprocess.check_output("ifconfig " + interface +
    " | grep 'inet ' | awk '{ print $2 }' | cut -d ':' -f2", shell=True).strip()
prefix = ip.split('.')[0] + '.' + ip.split('.')[1] + '.' +ip.split('.')[2] + '.'

for addr in range(0,254):
    answer=sr1(ARP(pdst=prefix+str(addr)),timeout=1,verbose=0)
    if answer == None:
        pass
else:
    print(prefix+str(addr))
```

### Scapy Example 1Code Review

Line 1

> #!/usr/bin/python

The first line indicates where the Python interpreter is located so that the scripte can be executed without it being passed to interpreter. The script then imports all Scapy functions and also defines Scapy logging levels to eliminate unnecessary output in the script.

To be continued...

If the script is executed without any arguments supplied

## Using Nmap to perform host discovery (layers 2/3/4)

## Using ARPing to perform host discovery (layer 2)

## Using netdiscover to perform host discovery (layer 2)

## Using Metasploit to perform host discovery (layer 2)

## Using ICMP to perform host discovery

## Using fping to perform host discovery

## Using hping3 to perform host discovery (layers 3/4)


---
