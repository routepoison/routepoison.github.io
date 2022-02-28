show ip eigrp topology active

R1(config-if)#ip hello-interval eigrp 10 16
*Apr 22 13:23:13.875: %DUAL-5-NBRCHANGE: IP-EIGRP(0) 10: Neighbor 1.1.2.2 (FastEthernet0/0) is down: Interface Goodbye received
*Apr 22 13:23:14.363: %DUAL-5-NBRCHANGE: IP-EIGRP(0) 10: Neighbor 1.1.2.2 (FastEthernet0/0) is up: new adjacency

R1(config-if)#ip hold-time eigrp 10 2
*Apr 22 13:23:34.759: %DUAL-5-NBRCHANGE: IP-EIGRP(0) 10: Neighbor 1.1.2.2 (FastEthernet0/0) is down: Interface Goodbye received
*Apr 22 13:23:35.607: %DUAL-5-NBRCHANGE: IP-EIGRP(0) 10: Neighbor 1.1.2.2 (FastEthernet0/0) is up: new adjacency

R1(config-if)#ip hold-time eigrp 10 15
*Apr 22 13:23:40.423: %DUAL-5-NBRCHANGE: IP-EIGRP(0) 10: Neighbor 1.1.2.2 (FastEthernet0/0) is down: Interface Goodbye received
*Apr 22 13:23:41.371: %DUAL-5-NBRCHANGE: IP-EIGRP(0) 10: Neighbor 1.1.2.2 (FastEthernet0/0) is up: new adjacency

R1#show ip eigrp interfaces detail Fa0/0 | i Hello|Hold
  Hello interval is 5 sec