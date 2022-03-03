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
# subprocess.check_output() returns bytes.
ip = subprocess.check_output("ifconfig " + interface + " | grep 'inet ' | awk '{ print $2 }' | cut -d ':' -f2", shell=True).strip()
prefix = ip.split(b'.')[0] + b'.' + ip.split(b'.')[1] + b'.' + ip.split(b'.')[2] + b'.'

for addr in range(0,254):
    answer=sr1(ARP(pdst=bytes(prefix)+ bytes(addr)),timeout=1,verbose=0)
    if answer == None:
        pass
else:
    print(prefix+str(addr))