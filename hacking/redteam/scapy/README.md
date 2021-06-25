# Scapy v2.4.4

At the time this is being written we're at version 2.4.4.

```
└─$ scapy                        
INFO: Can't import PyX. Won't be able to use psdump() or 
                                      
                     aSPY//YASa       
             apyyyyCY//////////YCa       |
            sY//////YSpcs  scpCY//Pp     | Welcome to Sca
 ayp ayyyyyyySCP//Pp           syY//C    | Version 2.4.4
 AYAsAYYYYYYYY///Ps              cY//S   |
         pCCCCY//p          cSSps y//Y   | https://github
         SPPPP///a          pP///AC//Y   |
              A//A            cyP////C   | Have fun!
              p///Ac            sC///a   |
              P////YCpc           A//A   | Craft packets 
       scccccp///pSP///p          p//Y   |               
      sY/////////y  caa           S//P   |
       cayCyayP//Ya              pY/Ya
        sY/PsY////YCc          aC//Yp 
         sc  sccaCY//PCypaapyCP//YSs  
                  spCPY//////YPSps    
                       ccaacs         
                                       using IPython 7.20
                                       
```

## Table of Content

## Out of the Gate

###


```python
>>> i = IP()
>>> i.display()
###[ IP ]### 
  version= 4
  ihl= None
  tos= 0x0
  len= None
  id= 1
  flags= 
  frag= 0
  ttl= 64
  proto= hopopt
  chksum= None
  src= 127.0.0.1
  dst= 127.0.0.1
  \options\ 

>>> u = UDP()
>>> u.display()
###[ UDP ]### 
  sport= domain
  dport= domain
  len= None
  chksum= None
```

