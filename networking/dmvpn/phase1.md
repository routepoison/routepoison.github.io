# Dynamic Multipoint VPN - DMVPN

## Hub Configuration

```
conf t
interface Tunnel0
ip address 10.0.0.2 255.255.255.0
no ip redirects
ip mtu 1400
ip nhrp map multicast dynamic
ip nhrp network-id 99
ip tcp adjust-mss 1360
tunnel source Gig0/0
tunnel mode gre multipoint
tunnel key 99
end
```

## Default Spoke Tunnel Config

```
conf t
int tun 0
ip add 10.0.0.1 255.255.255.0
ip nhrp map multicast 1.1.2.2
ip nhrp map 10.0.0.1 1.1.2.2
ip nhrp network-id 99
ip nhrp nhs 10.0.0.1
tunne source gig 0/0
tunnel destin 1.1.2.2
tunnel key 99
end
```

## Validation

### Hub

> show dmvpn

```
Legend: Attrb --> S - Static, D - Dynamic, I - Incomplete
        N - NATed, L - Local, X - No Socket
        # Ent --> Number of NHRP entries with same NBMA peer
        NHS Status: E --> Expecting Replies, R --> Responding, W --> Waiting
        UpDn Time --> Up or Down Time for a Tunnel
==========================================================================

Interface: Tunnel0, IPv4 NHRP Details 
Type:Hub, NHRP Peers:1, 

 # Ent  Peer NBMA Addr Peer Tunnel Add State  UpDn Tm Attrb
 ----- --------------- --------------- ----- -------- -----
     1 1.1.2.1                10.0.0.1    UP 00:00:03     D

R2#sho ip nhrp
10.0.0.1/32 via 10.0.0.1
   Tunnel0 created 00:00:21, expire 01:59:38
   Type: dynamic, Flags: unique registered used 
   NBMA address: 1.1.2.1 
```

> show ip nhrp

```
R2#sho ip nhrp
10.0.0.1/32 via 10.0.0.1
   Tunnel0 created 00:00:21, expire 01:59:38
   Type: dynamic, Flags: unique registered used 
   NBMA address: 1.1.2.1 
```

### Spoke 

> show dmvpn

```
R1#show dmvpn
Legend: Attrb --> S - Static, D - Dynamic, I - Incomplete
        N - NATed, L - Local, X - No Socket
        # Ent --> Number of NHRP entries with same NBMA peer
        NHS Status: E --> Expecting Replies, R --> Responding, W --> Waiting
        UpDn Time --> Up or Down Time for a Tunnel
==========================================================================

Interface: Tunnel0, IPv4 NHRP Details 
Type:Spoke, NHRP Peers:1, 

 # Ent  Peer NBMA Addr Peer Tunnel Add State  UpDn Tm Attrb
 ----- --------------- --------------- ----- -------- -----
     1 1.1.2.2                10.0.0.1    UP 00:00:11     S

```

> show ip nhrp

```
10.0.0.1/32 via 10.0.0.1
   Tunnel0 created 00:19:42, never expire 
   Type: static, Flags: 
   NBMA address: 1.1.2.2 
R1#
```

## Don't understand? Need an explanation?

Please refer to my [FAQ](https://github.com/gil-ryan/ultimate-cli-handbook#learn-more-faq) portion of the handguide!
