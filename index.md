# Welcome

## Directory

* :file_folder: [Networking](./#)
    + :open_file_folder: [Administrative Distance](./networking/admin-distances.md)
* :file_folder: [Programming](./#)
* :file_folder: [Hacking](./#)

---

## April 8th

```
# Full Example
!
configure terminal
!
router ospf 1 vrf VPN01
!
network 0.0.0.0 255.255.255.255 area 0
!
router ospf 2 vrf VPN02
!
network 0.0.0.0 255.255.255.255 area 0
!
# VALIDATE
!
show vrf
```

---

## April 7th

### Routing Administrative Distances

| Protocol | Administrative Distance |
|:--------:|:-----------------------:|
|Connected|0|
|Static|1|
|EIGRP Summary Route|5|
|BGP|20|
|iEIGRP|90|
|iGRP|110|
|IS-IS|115|
|Routing Information Protocol RIP|120|
|Exterior Gateway Protocol|140|
|On Demand Routing (ODR)|160|
|External EIGRP|170|
|Internal BGP|200|
|Unknown|255|
