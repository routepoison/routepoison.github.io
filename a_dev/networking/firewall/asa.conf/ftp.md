# FTP Files from NAS to ASA

Took forever, but I finally got a FTP connection to work.

## Commands

Passwords have been sanitized.

```ASA
grs-fuji# copy ftp: disk0:

Address or name of remote host [192.168.1.163]? 

Source username [grs]? 

Source password []? *********

Source filename [/Public/test.txt]? 

Destination filename [test.txt]? 

Accessing ftp://grs:*********@192.168.1.163//Public/test.txt...!
Writing file disk0:/test.txt...
!
229 bytes copied in 0.140 secs
```
