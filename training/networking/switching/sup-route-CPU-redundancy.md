# Supervisor and Route Processor Redundancy

## Switching Supervisor

* Difference between modular and fixed configuration switches
* What is a supervisor?
* Why do we need Supervisor and Route Processor Redundancy

## RPR Route Processor Redundancy

* Redundany Sup partially booted and initialized technically in "Standby" mode
* Any uplinks on Standby are active and usable
* Changes to Startup-Config and Config-Register settings on ACtive are replicated to Standby
* Both supervisors should have same IOS image, but not required

* takes a minimum of 2-minutes to complete switchover process
* when activated

- [x] all linecards must reload
- [x] routing engine initialized
- [x] L2 Protocols Initialized

* Sup that boots first is Active

## Configuration

```
!
# config mode
redundancy
!
# (config-red)#
mode rpr
!
```

* Verification

```
!
show redundancy states
!
```

## RPR+ Route Processor Redundancy Plus

* Both Sups MUST have same IOS version
* Standby Sup fully initialized and configured
* __30-60 seconds switchover__
* installed modules don't need to be reloaded
* FIB tables are cleared during a switchover, so routed traffic will be temporarily dropped...but static routes are maintained
* Gig uplinks on standby are always active

```
!
redundancy
!
# (config-red)
mode rpr-plus
!
```

* Verification

```
!
show redundancy states
!
```

## SSO Stateful Switchover

* Similar to RPR+
* Maintatins stateful feature information
    + FIB and Adjacency Tables
    + STP information and port states
* Faster thatn RPR+ due to configuration synch of statful information (0-3 seconds)
    + PFC information is synchronized
    + routing protocol info (running on RP of MSFC) NOT synchronized
* not all switches/RP supports this feature

![SSO Architecture](./sso.png)

## SSO with NSF

* Stateful Switchover with Non-Stop Forwarding
* Works with SSO (requires it)
* allows a layer-3 device to continue forwarding packets along known routes, even as routing peers are lost and re-established
    - Data Plane continue to use CEF information and forwarding
    - Control Plane busy re-establishing neihgbors and routes

* Stateful Switchover with Non-Stop forwarding
* Routers classified as NSF-Capable and NSF-Aware
    -NSF-Capable is the switch, Capable of continuing to foward packets even while rebuilding routing relationships
    - NSF-Aware: a peer router that understands it shouldn't tear down neighbor relationships when its peer fails and should continue to accept packets from peer
* each routing protocol must be configured with NSF-related commmands:

## NSF Configuration

```
!
# BGP (config-router)
bgp graceful restart
!
# EIGRP
nsf
!
# OSPF
nsf
```

---

[HSRP](./hsrp.md)
[VRRP](./VRRP.md)
[GLBP](./HSRP.md)
[Supervisor and Switch CPU Redundancy](./sup-route-CPU-redundancy.md)
