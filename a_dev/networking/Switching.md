# Switching

Repeaters make a strong copy of a signal.
They are actually considered layer one devices.

Hubs do the same exact thing, except with more ports.

Both devices can only transmit one signal at a time, in effect;
it operates as one giant collision domain. Meaning that switching provides
multiple collision domains. 
CSMA/CD
--
Host listens to the wire, if it is in use, the host backs off and then listens again.
If it is not busy then it sends the signal. If two devices try to send at the same time,
it actually changes the voltage.  The end users that sent the data will then invoke a backofftimer,
set to milliseconds. When each host's random timer expires, they will each begin the process
from the beginning and listen to the wire. Since the back off timer is random, it is unlikely the two
hosts will have the same problem.

Continue to add PCs and you could see how this may turn into a problem.
---

The more collision domains the better, leading to switching. As you already know, if a PC sends data
the hub with then flood out the broadcast to every other PC. Regardless if they want it or not.

"Everything we do on a router or switch has a cost."

Not a finanicial cost, but a cost of power, bandwidth, etc. Hubs and repeaters have serious limitations.
So lets move on to switches and bridges..

Bridges
---
This was the next giant step forward. It allowed smaller collision domains, by actually segmenting your 
network. Having collision domains may sound couter intuitive, but it's actually a good thing.
Overall bridges do still end up becoming one large broadcast domain.

Switches
---
EACH switchport is its own collision domain.
With the correct switch configs and network cards, each host can theoretically run at 200Mbps (100 sending and
100 recieving)
However all of the ports still remain as one broadcast domain, that is, out of the box of a fresh Cisco switch.

Microsegmentation is used in Cisco documentation to describe the "one host, one collision domain" segmentation
performed by switches. 

The fram forwarding/decision making process
Filter it
Flood it

When a frame first comes into a switch, it first looks at the frames source MAC address.
The reason being because source addresses are how the switch builds and maintains
its dynamic MAC address table.

You can actually statically assign MAC addresses, but it's not very efficient. On a side note it's interesting in terms of spoofing. IF you ask me...

When booting up a switch there will be some entries in the MAC address table, these are for the CPU
SW1#show mac address-table

MAC address table is also known as the switching table, the Content Addressable Memory table (CAM), and or the bridging table (Not so popular)

----

So when a frame comnes in, the switch goes: "Do I have an entry for this MAC address in my table"
So there is no gray area, it either does, or doesn't.
Now here comes the frame forwarding decision, the switch checks if it has the destination MAC address in it's table. Since it doesn't (we just turned the switch on). It will flood the frame.


SW#1show mac address-table dynamic

The amount of time a MAC address remains in a MAC table is 5 minutes by default.
SW1#mac address-table aging-time 600 

LIVE LAB
---

Showing dynamic and static MAC table entries

Frame processing Methods
Short and simple:

Store-and-forward
Entire frame is stored by the switch, and the forwarded.

Cut-through
The switch reads the MAC addresses on the incoming frame and then begins to forward the frame even as part of it is still being received. The FCS is not checked, so there is zero error detection.

Fragment-free
The middle ground, this makes an assumption that if there's corruption in the frame, it's in the first 64 bytes.

Store and forward is the slowerst, but has the best error detection.
Cut through has no error detection, but it fastest.
Fragment free is the middleground of the other two.

VLANs
They are guarenteed to be all over your exams.
Getting familiar with the ping command.



SW#1show vlan brief

Default vlan is also known as the default vlan.


===

Layer 3 Switches (you can make routing ports)

"Router on a Stick" 
We're going to get back to that later

Port Security
===
You must enable it first
SW1#config-if)#switchport port-security
SW1#switchport port-security ?

aging allows you to set aging options for Secure MAC addresses

mac-address allows you to specify secure MAC address

maximum allows you to specify how many secure MAC addresses there will be. The default is one.

violation allows you to specify what action will be taken if a non-secure source MAC address is received on the port.
	Default is shutdown, this mode shuts down the port, transmits a message to the log indicating the action taken, and drops the violating frames. The interface status will be err-disabled.
	protect simply drops the violating frames 
