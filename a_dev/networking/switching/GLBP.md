# Gateway Load-Balancing Protocol (GLBP)

* Cisco proprietary
* provides gateway redundancy AND per-host load-balancing
* __AVG (Active Virtual Gateway)__ in charge of determining host-to-gateway allocations

* preemption for role of AVG on by default.
* AVG replies to the ARP request sent to the virtual IP
* A single AVG per group
    + highest priority or...
    + highest IP address

* Gateways capable of forwarding packets in GLBP are called __AVF__
    + __Active Virtual Forwarder__
    + Maximum of 4-AVFs per group

* AVG is also an AVF
* Each AVF assigned virtual MAC
    + 0007.b4xx.xxyy where:
        - xx:xx = GLBP Group #
        - YY = AVF #
* AVFs request their AVF# and virtual MAC from AVG
* AVG and AVFs all send Hello packets (3-secs)

![GLBP](./glbp.png)

## Implementing GLBP

* Enabling GLBP in the interface

> glbp [group-id] ip [virtual-ip]

* Configuring priority

> glbp [group-id] priority [priority]

* Disabling preemption

> no glbp [group-id] preempt

## GLBP Load Balancing

* Load-balancing algorithms:
    + round-robin (default)
    + host dependent
    + weightd
* Configred with

> glbp [group-id] load-balancing [weighted | round| host ]

## GLBP Weighted Load Balacing

* Configured on Acitve Virtual Gateway:

> glbp [group-id] load-balancing weighted

* Configured on AVFs

> glbp [group-id] weighting [value] lower [value] upper [value]

## AVF Object Tracking

* every router has default AVF weight = 100 (max value)
* beneath "lower" weight, router can no longer participate as AVF
* object tracking can be used to dynamically decrement weight value if tracked object fails

```
!
# global
track 1
!
# interface
glbp 1 weighting track 1
!
```

## Optimizing GLBP Intervals

* Configure hello and hold timers

> glbp [group-id] timers [hello time] [hold time]

* Configure redirect timer

```
!
# interface config
glbp 1 timers redirct ?
!
glbp 1 timers redirect 60 ?
!
glbp 1 timers redirect 60
```

## Verifying GLBP

```
!
show glbp
!
show glbp brief
!
```

---

[HSRP](./hsrp.md)
[VRRP](./VRRP.md)
[GLBP](./HSRP.md)
[Supervisor and Switch CPU Redundancy](./sup-route-CPU-redundancy.md)
