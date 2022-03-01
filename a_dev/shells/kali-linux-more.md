# Reconnaisancee

## Chapter Outline

* Using Google to find subdomains
* Finding e-mail addresses using theHarvester
* Enumerating DNS using the host command
* Enumerating DNS using DNSRecon
* Enumerating DNS using the dnsenum command

---

## Introduction

In my modest opinion, reconnaisance will play the most vital role throughout all of your experimentation. The more you understand your target, the more information that's gathered, the better. However - this must be carried out in a public and passive manner, obviously to avoid exposing yourself early on.

Reconnaisance issometimes referred to as **passive information gathering**.

Once we have enough findings from public sources, we move onto **active information-gathering** phase. The delineation here is we will now be physically interacting with the target's assets. We can begin by actively querying the target's DNS servers to uncover more information. The goal is to uncover networks of the target suitable for further investigation.

## Using Google

Great Google syntax for your toolkit:

* site:
* inurl:
* intitle:
 
### Working Google Example

Navigate to [https://www.google.com](https://www.google.com) and user the following:

> site:google.com

You'll find about About 48,70,00,000 results (0.40 seconds), but lets whittle that down more:

> site:google.com -site:google.com

THis should provide less results, but it didn't work effectively on my own attempt. Summary of google crap:

``` 
site:google.com -site:www.google.com -site:cloud.google.com -
site:translate.google.com -site:gsuite.google.com -
site:duo.google.com -site:domains.google.com -
site:store.google.com -site:blog.google.com -
site:firebase.google.com -site:on.google.com -
site:developers.google.com
```

## theHarvester

theHarvest is a great tool to grab loads of information from a doman. Again, we'll use Google as the example:

> theHarvester -d google.com -l 500 -b google

```
┌──(grs㉿kali)-[~]
└─$ theHarvester -d google.com -l 500 -b google

*******************************************************************
*  _   _                                            _             *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
* | __|  _ \ / _ \  / /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__| *
* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\__ \ ||  __/ |    *
*  \__|_| |_|\___| \/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|    *
*                                                                 *
* theHarvester 4.0.3                                              *
* Coded by Christian Martorella                                   *
* Edge-Security Research                                          *
* cmartorella@edge-security.com                                   *
*                                                                 *
******************************************************************* 


[*] Target: google.com 
 
        Searching 0 results.
        Searching 100 results.
        Searching 200 results.
        Searching 300 results.
        Searching 400 results.
        Searching 500 results.
[*] Searching Google. 

[*] No IPs found.

[*] No emails found.

[*] Hosts found: 12
---------------------
accounts.google.com:142.251.35.173
adservice.google.com:142.251.40.226
apis.google.com:142.250.64.110
maps.google.com:142.251.32.110
meet.google.com:142.251.40.206
myactivity.google.com:142.250.31.102, 142.250.31.139, 142.250.31.138, 142.250.31.113, 142.250.31.101, 142.250.31.100
ogs.google.com:142.251.40.206
passwords.google.com:142.250.72.110
policies.google.com:142.250.176.206
support.google.com:142.251.32.110
translate.google.com:142.251.41.14
www.google.com:142.250.176.196
```

---
