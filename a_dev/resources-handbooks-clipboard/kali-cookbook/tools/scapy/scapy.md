# Scapy

Learning Scapy, an extremely powerful Python based networking tool that allows us to create, manipulate, and transmit traffic.

```
┌──(grs㉿kali)-[~]
└─$ scapy
INFO: Can't import PyX. Won't be able to use psdump() or pdfdump().
                                      
                     aSPY//YASa       
             apyyyyCY//////////YCa       |
            sY//////YSpcs  scpCY//Pp     | Welcome to Scapy
 ayp ayyyyyyySCP//Pp           syY//C    | Version 2.4.4
 AYAsAYYYYYYYY///Ps              cY//S   |
         pCCCCY//p          cSSps y//Y   | https://github.com/secdev/scapy
         SPPPP///a          pP///AC//Y   |
              A//A            cyP////C   | Have fun!
              p///Ac            sC///a   |
              P////YCpc           A//A   | Craft packets like I craft my beer.
       scccccp///pSP///p          p//Y   |               -- Jean De Clerck
      sY/////////y  caa           S//P   |
       cayCyayP//Ya              pY/Ya
        sY/PsY////YCc          aC//Yp 
         sc  sccaCY//PCypaapyCP//YSs  
                  spCPY//////YPSps    
                       ccaacs         
                                       using IPython 7.31.1
>>> ARP().display()
###[ ARP ]### 
  hwtype= 0x1
  ptype= IPv4
  hwlen= None
  plen= None
  op= who-has
  hwsrc= 08:00:27:95:bd:54
  psrc= 10.0.2.15
  hwdst= 00:00:00:00:00:00
  pdst= 0.0.0.0
```

Since we're working with Python, its easy to instantiate variables with requests.

```python
arp_request = ARP()
arp_request.pdst = "172.16.69.128"
arp_request.display()

sr1(arp_request)
```

You can also perform this task by calling functions directly and passing arguments, which in some circumstances may be beneficial in completing a task with one single line of code, or by limiting unnecessary variables.

> sr1(ARP(pdst='127.0.0.1'))

If your destination address is not up or connected, you will not receive responses, and the function will continue to analyze and wait for incoming traffic on your local interface indefinitely.  You will need to terminate the function or specify a timeout argument in your code. Timeouts are critical when using Scapy for this sole reason.

---
