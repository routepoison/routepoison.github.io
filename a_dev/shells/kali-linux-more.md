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

---
