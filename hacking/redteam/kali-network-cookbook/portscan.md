# Port Scanning

## Introduction to Port 

Open ports on a target system is an important step to defining the attack surface of a target. Open ports correspond to the networked services that are running on a system.

These open ports correspond to services that may be addressed with either UDP or TCP traffic. __Both TCP and UDP are transport protocols__. __Transmission Control Protocol (TCP)__ is the more commonly used of the two and provides _connection-oriented_ communication. __User Datagram Protocol (UDP)__ is a _non connection-oriented_ protocol that is sometimes used with services for which speed of transmission is more important than data integrity.

The penetration testing technique used to enumerate these services is called __port scanning__.

## UDP port scanning

UDP scanning can often be challenging, tedious, and time consuming. The first three recipes in this chapter will cover how to perform a UDP port scan with different tools in Kali Linux. To understand how these tools work, it is important to understand the two different approaches to UDP scanning that will be used.

One technique, which is addressed in the first recipe, is to rely exclusively on ICMP port-unreachable responses.

This type of scanning relies on the assumption that any UDP ports that are not associated with a live service will return an _ICMP port-unreachable_ response, and a lack of this response is interpreted as an indication of a live service.

While this approach can be effective in some circumstances, it can also return inaccurate results in cases where the host is not generating port-unreachable responses or the port-unreachable replies are rate limited or are filtered by a firewall.

The alternative approached, addressed in second and third recipes we review, is to use a service-specific probe to attemp to solicit a response, which would indicate that the expected service is running on the targeted port.

## TCP port scanning


TCP port scanning is much more common. These techniques includeL stealth scannig, connect scanning, and zombie scanning. Before diving into these techniques, it's important to understand how TCP connections are established and maintained. TCP is connection-oriented and data is only transferered after a connection has been established between two systems. This process associated with establishing with TCP connections is called the __three-way handshake__.

![3-Way Handshake](./3way-handshake.png)

---