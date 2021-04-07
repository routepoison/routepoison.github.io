# Gateway Redundancy with FHRP

Why is FHRP in the switching section of our certification? 

Remember the 3-tier Network model, the access layer is where you provide different VLANs and broadcast domains. They terminate on the distribution layer, all SVIs live on the distribution. So in this case you'll be using multi-layer switches, with their switched-virtual interfaces, are serving as the gateway for our various end users.

## HSRP

* Hot Standby Router Protocol
* Cisco Proprietary
* Uses UDP port 1985 and multicast address 224.0.0.2

Switches participating in HSRP, all in the same subnet (at least two) see each and need to send hello messages.

* HSRP router with highest priority is considered "Active"
    + Default priority = 100
* MAC address: 0000.0c07.acxx
    + xx refers to the group number in hex
* preemption disabled by default
* HSRP/VRRP = no load-sharing feature

## Implementing Basic HSRP

* Enabling HSRP in the interface

> standby [group-id] ip <virtual-ip>

* Configure priority

> standby [group-id] priority [priority]

### Enable Preemption

> standby [group-id] preempt

## HSRP State Machine

* Disabled
* Initial (INIT)
* Learn
* Listen
* Speak
* Standby/Active

## HSRP Hello Timers

* HSRP Hello timer = 3-secs
* Dead Time = 10-sec or 3 * Hello

> standby 1 timers ?

> standby 1 timers msec 200

## Modifying Preemption

* HSRP Preemtion can be delayed to allow time for other protocol to re-build their tables.

> standby 1 preempt delay ?

* Preemption allows the original _active_ gateway take back over after it is goes into standby


## HSRP Authentication (interface keys)

* Auth Supported
    + Plain text
    + MD5

### Plain-text configuration

> standby [group-id] authentication [password]

###  MD5 Configuration

> standby [group-id] authentication md5 key-string [0|7] string

## HSRP Authentication with Key Chain Keys

* HSRP can obtain current/active MD5 key from a key chain.
* NTP should also be confiured

```
key chain INE
key 1
    key-string cisco
    accept-lifetime 08:00:00 Aug 1 2014 11:59:59 Sep 1 2014
    send-lifetime 01:01:00 Aug 1 2014 11:59:59 Sep 1 2014
key 2
    key-string INE-123
    accept-lifetime 01:01:00 Sep 2 2014 12:59:59 Oct 1 2014
    send-lifetime 01:01:00 Sep 2 2014 12:59:59 Oct 1 2014
!
interface vlan1
    ip address 1.1.1.100 255.255.255.0
    standby 1 ip 1.1.1.1
    standby 1 authentication md5 key-chain INE
end
```

## HSRP Object Tracking

* HSRP can track objects (typically interfaces)
* If tracked object fails, HSRP priority is reduced by configurable amount (Default = 10)

* First, create "track object" globally

> standby [group] track [object #] [decrement value]

## Verifying HSRP

```
show standby
!
show standby brief
!
```

### NX-OS

```
show nhrp
```

---

[HSRP](./hsrp.md)
[VRRP](./VRRP.md)
[GLBP](./HSRP.md)
[Supervisor and Switch CPU Redundancy](./sup-route-CPU-redundancy.md)
