Have you ever performed a show running-configuration (or show run) command and waited "too many" seconds for it to appear? Frustrating, right? You can use a new version of the parser command to speed up that view time. As the parser system is a caching system, it is going to do two things: (1) keep the IOS configuration in memory and use more of your memory to do it and (2) be more effective as repetition increases and as the configuration gets larger.


Ciscozine#sh line console 0
Ciscozine(config)#line console 0
Ciscozine(config-line)#speed 115200


Console output is encoded by your SSH or terminal program.

> clear log

To clear the internal buffer, use "clear log"

> no logging console

This will disable logging on your console session so you dono't see a lot of messaged when you need to work on it.

> no monitor

If you're directly connected to the router or switch device, just do a "no terminal monitor" to disable console message or logs.

> term monitor

Disable console messages from a telnet sessions.

> no terminal monitor

Enable console messages 

IDF-A#show run | i line
line con 0
line aux 0
line vty 0 4
line vty 5 15

IDF-A(config)#line vty 0 15
IDF-A(config-line)#line vty 0 4 
IDF-A(config-line)#login
% Login disabled on line 2, until 'password' is set
% Login disabled on line 3, until 'password' is set
% Login disabled on line 4, until 'password' is set
% Login disabled on line 5, until 'password' is set
% Login disabled on line 6, until 'password' is set
IDF-A(config-line)#password cisco
IDF-A(config-line)#exit


## --- [ Console & Terminal ] --- ##
#
!
#  Output in full --More-- 
term length 0
!
# DIST-A#term length 0
# DIST-A#sho run all | i term length
# DIST-A#
!
# Set back to default 
term length 24

!
# DIST-A#show run all | i length
# length 24
# length 24
# length 24
# length 24
!
## --- [ END ] --- ##