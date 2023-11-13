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
### Nessus Examples

A basic example. In order to find e-mail addresses from google.com using the Google search engine, we'll use the following:

> theHarvester -d google.com -l 500 -b google

In order to find e-mail addresses from google.com using the Google search
engine, we'll use the following
Output:

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
myactivity.google.com:142.250.31.102, 142.250.31.139, 10.31.100
ogs.google.com:142.251.40.206
passwords.google.com:142.250.72.110
policies.google.com:142.250.176.206
support.google.com:142.251.32.110
translate.google.com:142.251.41.14
www.google.com:142.250.176.196
```

The command uses _-d_ as the domain we want to search. We use _-l_ to limit the number of results, and _-b_ to define the data source. _-f_ writes the results to a file. You won't always get e-mail addresses, using our next example, we get back usernames.

Another example:

> theHarvester -d google.com -l 500 -b linkedin

You can also search against not only e-mails, but hosts and virtual hosts.

> theHarvester -d google.com -l 500 -b all

## Enumerating DNS using the host command

Using DNS will give leverage in almost every phase of recon. DNS can be compared to an address book and for this reason will normally divulge at least some information regarding domains they are the authority for. We can use the _-a_ flag to do a comprehensive look up or use _-t_ flag followed by the type to be more specific.

Example:

> host -a google.com

```
┌──(grs㉿kali)-[~]
└─$ host google.com
google.com has address 142.250.80.46
google.com has IPv6 address 2607:f8b0:4006:820::200e
google.com mail is handled by 20 alt1.aspmx.l.google.com.
google.com mail is handled by 40 alt3.aspmx.l.google.com.
google.com mail is handled by 50 alt4.aspmx.l.google.com.
google.com mail is handled by 10 aspmx.l.google.com.
google.com mail is handled by 30 alt2.aspmx.l.google.com.
```

> host -t ns google.com

```
┌──(grs㉿kali)-[~]
└─$ host -t ns google.com 

google.com name server ns3.google.com.
google.com name server ns1.google.com.
google.com name server ns4.google.com.
google.com name server ns2.google.com.
```

It is also possible to initiate DNS zone transfers with _host_. Though most domains should not allowe you to, here's how:

> host -l google.com ns1.google.com

When an organization has a large number of nameservers, it would be easiest to automate this process with a bash script, or script in general.

This script will generate a list of namesevers, and then iterate over each, attempting a zone transfer:

```bash
#!/bin/bash
if [ ! $1 ]; then
echo "Usage: #./dns-find-transfer.sh <domain>";
exit;
fi
for server in $(host -t ns $1 |cut -d" " -f4);do
printf $server | sed 's/.$//'
host -l $1 $server |grep "Address: " | cut -d: -f2 | sed 's/...$
done
```

---
