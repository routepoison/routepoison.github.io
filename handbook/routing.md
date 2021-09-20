#
route-map ADD permit 200
!
set tag 1
!
#

#
router ospf1
!
redistribute rip subnets route-map ADD
#


ipv6 access-list Deny_Telnet sequence 10 deny tcp host 198A:0:200C::1/64 host 201A:0:205C::1/64 eq telnet
!
int Gi0/0
 ipv6 traffic-filter Deny_Telnet in

ipv6 access-list
!
int Gi0/0
 ipv6 access-map Deny_Telnet in

ipv6 access-list

ipv6 access-list


!
show policy-map

Policy Map LIMIT_BGP
 Class BGP
  drop
Policy Map SHAPE_BGP
 Class BGP
  Average Rate Traffic Shaping
  cir 10000000 (bps)
Policy Map POLICE_BGP
 Class BGP
  police cir 1000k bc 1500
   conform-action transmit
   exceed-action transmit
Policy Map COPP
 Class BGP
  police cir 1000bk bc 1500
   conform-action transmit
   exeed-action drop
