# Kali Linux Network Scanning Cookbook 2E (2017)

## Reconnaissance

### Subdomains

The Google search engine provides a number of search operators that allow you to narrow your results when performing queries. A few that can come in particularly handy for the penetration tester are:

* site:
* inurl:
* intitle:

```
site:google.com -site:www.google.com
```

### Finding E-mail Addresses

#### theHarvester

theHarvester comes preinstalled on Kali Linux, however, you can also refer to the [GitHub page](https://github.com/laramies/theHarvester).

>  theHarvester -d google.com -l 500 -b google

### DNS

#### host command

Looking up nameservers:

> host -t ns google.com

```output
google.com name server ns1.google.com.
google.com name server ns2.google.com.
google.com name server ns4.google.com.
google.com name server ns3.google.com.
```

---
