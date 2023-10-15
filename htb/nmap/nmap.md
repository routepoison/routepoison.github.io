# Network Enumeration w NMAP

Network Mapper (Nmap) is an open-source network analysis and security auditing tool written in C, C++, Python, and Lua. It is designed to scan networks and identify which hosts are availabel on the network using raw packets, and services and applications, including the name and version, where possible. It can also identify the operatin systems and version of these host. Besides other features, Nmap also offers scanning capabilities that can determine if packet filters, firewalls, or IDS are configured as needed.

The tool is one of the must used tools by network administrators and IT security specialists. It is used to:

    * Audit the security aspects of networks
    * Simulate penetration tests
    * check firewall and IDS settings and configurations
    * types of possible connections
    * network mapping
    * response analysis
    * indentifying open ports
    * vulnerability assessment as well

## Nmap Architecture

Nmap offers many different types of scans that can be used to obtain various results about our targets. Basically, Nmap can be divided into the following scanning techniques:

* host discovery
* port scanning
* service enumeration and detection
* OS detection
* scriptable interaction with the target service (Nmap scripting engine)

```
grs7@htb[/htb]$ nmap --help

<SNIP>
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
<SNIP>
```

For example, the TCP-SYN scan (-sS) is one of the default settings unless we have defined otherwise and is also one of the most popular scan methods. This scan method makes it possible to scan several thousand ports per second. The TCP-SYN scan sends one packet with the SYN flag and, therefore, never completes the three-way handshake, which results in not establishing a full TCP connection to the scanned port.

  * If our target sends an SYN-ACK flagged packet back to the scanned port, Nmap detects that the port is open.
  * If the packet receives and RST flag, it is an indicator that the port is closed.
  * If Nmap does not receive a packet back, it will display it as filtered. Depending on the firewall configuration, certain packets may be dropped or ignored by the firewall.

  > grs7@htb[/htb]$ sudo nmap -sS localhost

  -oA tnet	Stores the results in all formats starting with the name 'tnet'.
  -iL	Performs defined scans against targets in provided 'hosts.lst' list.


## Host Discovery

When we need to conduct and internal penetration test for the entire network of a company, for example, then we should first of all, get an overview of which systems are online that we can work with. To actively discover such systems on the network, we can use various Nmap host discovery options. There are many options Nmap provides to determine whether our target is alive or not. The most effective host discovery method is to use ICMP echo requests, which we will look into.

It is always recommened to store every single scan. This can later be used for comparison, documentation, and reporting, After all, different tools may produce different results. Therefor it can be beneficial to distinguish which tool produces which results.

### Scan Network Range

> grs7@htb[/htb]$ sudo nmap 10.129.2.0/24 -sn -oA tnet | grep for | cut -d" " -f5

This scanning method works only if the firewalls of the host allow it. Otherwise, we can use other scanning techniques to find out if the hosts are active or not. We will take a closer look at these techniques in, 'Firewall and IDS Evasion'.

```EXAMPLE LIST
grs7@htb[/htb]$ cat hosts.lst

10.129.2.4
10.129.2.10
10.129.2.11
10.129.2.18
10.129.2.19
10.129.2.20
10.129.2.28
```

If we use the same scanning technique on the predefined list, the command will look like this:

> grs7@htb[/htb]$ sudo nmap -sn -oA tnet -iL hosts.lst | grep for | cut -d" " -f5

-sn	Disables port scanning.
-oA host	Stores the results in all formats starting with the name 'host'.

If we disable port scan (-sr), Nmap automaticall ping scan with ICMP Echo Requests (-PE). Once such a request is sent, we usually expect an ICMP reply if the pinging host is alive. The more interesting fact is that our previous scans did not do that because before NMap could send an ICMP echo request, it would sent an ARP ping resulting in an ARP reply. We can confirm this with the "--packet-trace" option. To ensure that ICMP echo requests are sent, we also define the option (-PE) for this.

```EXAMPLE
grs7@htb[/htb]$ sudo nmap 10.129.2.18 -sn -oA host -PE --packet-trace 

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 00:08 CEST
SENT (0.0074s) ARP who-has 10.129.2.18 tell 10.10.14.2
RCVD (0.0309s) ARP reply 10.129.2.18 is-at DE:AD:00:00:BE:EF
Nmap scan report for 10.129.2.18
Host is up (0.023s latency).
MAC Address: DE:AD:00:00:BE:EF
Nmap done: 1 IP address (1 host up) scanned in 0.05 seconds
```

  -oA host	Stores the results in all formats starting with the name 'host'.
  -PE	Performs the ping scan by using 'ICMP Echo requests' against the target.
  --packet-trace	Shows all packets sent and received

Another way to determine why Nmap has our target marked as "alive" is with the "--reason" option.


> grs7@htb[/htb]$ sudo nmap 10.129.2.18 -sn -oA host -PE --reason 

Nmap detects whether the host is alive or not through the ARP request and ARP reply alone. To disable ARP requests and scan our target with the desired ICMP  echo request, we can disable ARP pings by setting the "--disable-arp-ping" option. Then we can scan our target again and look at the packets sent and received.

> grs7@htb[/htb]$ sudo nmap 10.129.2.18 -sn -oA host -PE --packet-trace --disable-arp-ping 

## Host and Port Scanning

We will take a closer look at at and analyze some of the scanning methods. After we have found out that our target is alive, we want to get a more accurate picture of the system. The information we need includes:

  * open ports and its services
  * services versions
  * information that the services provided
  * Operating system

There are a total of 6 different states for a scanned port we can obtain:

| state | description | 
|:-:|:-:|
| open | this indicates that the connection to the scanned port has been established. These connections can be TCP connections, UDP datagrams as well as SCTP associations |
| closed | when the port is shown as closed, the TCP protocol indicates that the packet we recieved contains an RST flag. This scanning method can also be used for the port or we get an error code from the target. |
| filtered | Nmap cannot correctly identify whether the scanned port is open or closed because either no response is returned from the target for the port or we get an error code from the target. | 
| unfiltered | this state of a port only occurs during the TCP-ACK scan and means that the port is accessible, but it cannot be determined whether it is open or closed. |
| "open|filtered" | 

## Enumeration





---

↩️: [Home](../../index.md)
