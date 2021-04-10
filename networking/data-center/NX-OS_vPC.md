# Nexus NX-OS vPC Configuration Script

↩️ [Back to Routepoison.com!](../../index.md)

---

```
############################
## vPC Peer Configuration
############################
!
# feature tacacs+
!
feature udld
!
feature interface-vlan
!
feature lacp
!
feature vpc
!
feature lldp
!
# Switch-A
!
interface mgmt0
  speed 1000
  duplex full
  vrf member management
  ip address 1.1.1.1/30
!
# Switch-B
!
interface mgmt0
  speed 1000
  duplex full
  vrf member management
  ip address 1.1.1.2/30
!
## PO 10
!
interface ethernet 1/1
  description vPC peer link Po10
  switchport mode trunk
  switchport trunk allowed vlan 500,508-511,543-548,555,620-621
  flowcontrol receive on
  flowcontrol send on
  channel-group 10 mode active
!
interface ethernet 1/2
  description vPC peer link Po10
  switchport mode trunk
  switchport trunk allowed vlan 500,508-511,543-548,555,620-621
  flowcontrol receive on
  flowcontrol send on
  channel-group 10 mode active
!
interface port-channel 10
  description vPC peer link
  switchport mode trunk
  switchport trunk allowed vlan 500,508-511,543-548,555,620-621
  spanning-tree port type network
  speed 10000
  flowcontrol receive on
  flowcontrol send on
  vpc peer-link
!
# PO 20
!
interface ethernet 1/10
  description L2  link to #
  switchport mode trunk
  switchport trunk allowed vlan 1
  channel-group 20 mode active
!
interface ethernet 1/11
  description L2  link to #
  switchport mode trunk
  switchport trunk allowed vlan 1
  channel-group 20 mode active
!
interface port-channel 20
!
  description L2 Non-VPC Trunk to #
  switchport mode trunk
  switchport trunk allowed vlan 1
  spanning-tree port type normal
!
vpc domain 1
  peer-switch
  role priority 10
  peer-keepalive destination 1.1.1.2 source 1.1.1.1
  delay restore 180
  peer-gateway
#  track 2
  ip arp synchronize
!
vpc domain 1
  peer-switch
  role priority 20
  peer-keepalive destination 1.1.1.1 source 1.1.1.2
  delay restore 180
  peer-gateway
#  track 2
  ip arp synchronize
```

---

↩️ [Back to Routepoison.com!](../../index.md)
