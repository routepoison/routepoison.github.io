# Prefix-List Specified for RFC1918

↩️ [Back to Routepoison.com!](../../index.md)

---

Prefix-List Specified for RFC1918

```
ip prefix-list RFC1918 seq 5 permit 192.168.0.0/12 ge 32
ip prefix-list RFC1918 seq 10 deny 0.0.0.0/0 ge 32
ip prefix-list RFC1918 seq 15 permit 10.0.0.0/7 ge 8
ip prefix-list RFC1918 seq 20 permit 172.16.0.0/11 ge 12
ip prefix-list RFC1918 seq 25 permit 192.168.0.0/15 ge 16
```

---

↩️ [Back to Routepoison.com!](../../index.md)
