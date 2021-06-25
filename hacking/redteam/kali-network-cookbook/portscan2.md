# Portscanning Examples and Usage

## Scapy

[Check out my dedicated section on Scapy!](../scapy/README.md)

UDP scanning tends to be more challenging, the realy being is that UDP services will onyl reply to __service-specific__ requests. Therefore knowledge of any particular service can make it easier to positively identify that service; however, there are general techniqus that can be used to determine, with a reasonable amount of accuracy, whether a service is running on a given UDP port. This technique will at least use Scapy to identify closed UDP ports with the ICMP port-unreachable replies.

1. To send a UDP request to any port, we will ned to build layers of that request. First we would need to build layers of that request, withe first layer being IP.

In Scapy we can few and modify the IP packet  how we choose, in this case, we'll set it to _123_, or, the _Network Time Protocol (NTP)_