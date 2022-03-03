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

[Here we have a script](./tools/scapy/arp-request-loop.py) that can be used to perform layer 2 discovery on a sequential series of hosts.

## Using Nmap to perform host discovery (layers 2/3/4)

## Using ARPing to perform host discovery (layer 2)

## Using netdiscover to perform host discovery (layer 2)

## Using Metasploit to perform host discovery (layer 2)

## Using ICMP to perform host discovery

## Using fping to perform host discovery

## Using hping3 to perform host discovery (layers 3/4)


---
