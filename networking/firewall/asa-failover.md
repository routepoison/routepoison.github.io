# 🔥 ASA Transparent and Routed Modes

ASA Failover has a few other files that I will try to link in this that I reviewed.

```PRIMARY
!
enable
config t
!
failover lan unit primary
interface gigabitEthernet 0/3
no shutdown
failover lan interface LANFAIL gigabitethernet 0/3
failover interfaces ip LANFAIL 10.10.1.1 255.255.255.0 standby 10.10.1.2
failover key secretkey
failover link LANFAIL
exit
show failover

monitor external
monitor internal
exit
show failover
failover
exit
show failover interface
show failover
```

```SECONDARY
en
config t
no failover
failover lan unit secondary
interface gigabitEthernet 0/3
no nameif
no shutdown
failover lan interface LANFAIL gigabitEthernet 0/3

failover interface ip LANFAIL 10.10.1.1 255.255.255.0 standby 10.10.1.2
failover key secretkey
failover link LANFAIL
failover
exit
show run
```

---

↩️ [Back to Routepoison.com!](../../index.md)
