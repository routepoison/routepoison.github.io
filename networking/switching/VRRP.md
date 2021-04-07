# VRRP

* Open standard (original RFC 3768, now 5798)
* Built-in transport protocol: 112
* Multicast address 224.0.0.18
* Master router replies to ARP request for virtual IP address
* Preemption enabled by default
    + default priority = 100
* Timers
    + adverisement interval = 1 second
    + master down interval = 3.6 seconds

* MAC address; 0000.5e00:01xx
    = XX refers to the VRRP group number in hex
* No load-sharing feature
* different instance of VRRP can provide load-sharing

## Implementing VRRP

*  Enabling VRRP in the interface

> vrrp [group-id] [virtual]

* Configuring priority

> vrrp [group-id] [virtual IP] priority [priority]

## VRRP Authentication

* Auth supportedl
    + Plain-text
    + MD5

### Plain-text Config

> vrrp [group-id] authentication [password]

* MD5 Configuration
* Interface configuration mode

### Key-string

> vrrp [group-id] authentication md5 key-string [password]

### Key-chain

> vrrp [group-id] authentication md5 key-chain [key-chain name]

## Optimizing VRRP Timers

* All routers in VRRP group must share the same Hello timer.
* Configuring advertise timer

> vrrp [group-id] timers advertise msec [value]

* When increasing VRRP Hello timer, all other routers must 'learn' the new timer (not default behavior).

> vrrp [group-id] timers learn

* VRRP Hello packets cannot advertise millisecond timers.
* If configuring sub-second timers, must be configured on all VRRP routers in group

## Verifying VRRP

* Verification commands

> show vrrp

> show vrrp brief

---

[HSRP](./hsrp.md)
[VRRP](./VRRP.md)
[GLBP](./HSRP.md)
[Supervisor and Switch CPU Redundancy](./sup-route-CPU-redundancy.md)
