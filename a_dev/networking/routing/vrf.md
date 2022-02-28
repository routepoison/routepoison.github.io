# VRF-Lite

1. Create the VRF(s)
2. Assign interface(s) to the VRF
3. Enable routing for the VRF

## 1. Getting Started - Configuring VRF-Lite

```
# Create IPV4 VRF called GUEST using old VRF CLI Format
!
ip vrf GUEST
!
# Create a VRF called STAFF using the new VRF CLI format
!
vrf definition STAFF
!
# Enable IPv4 address family for the STAFF VRF using the new VRF CLI Format
!
address-family ipv4
!
# Enable IPv4 address family for the STAFF VRF using the new VRF CLI Format
!
address-family ipv6
!
```

## 2. Assign an Interface to the VRF

```
!
interface gigabitethernet 0/0/0
!
ip vrf forwarding GUEST
!
interface gigabitethernet 0/0/1
!
vrf forawrding STAFF
!
```

## 3. Enable Routing

```
# Static route
!
ip route vrf GUEST 0.0.0.0 0.0.0.0 172.16.16.2
!
# OSPFv3
!
router ospfv3 1
!
address-family ipv4 unicast vrf STAFF
!
# EIGRP
!
router eigrp CISCO
!
address-family ipv4 unicast vrf GUEST autonomous-system 100
!
router bgp 65001
!
address-family ipv4 vrf STAFF
!
```

## Verifying VRF-Lite

> show vrf

> show vrf detail _vrf-name_