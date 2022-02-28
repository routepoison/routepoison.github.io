# Netcat

## Man Page

```text
NC(1)                     BSD General Commands Manual                    NC(1)

NAME
     nc -- arbitrary TCP and UDP connections and listens

SYNOPSIS
     nc [-46AcDCdhklnrtUuvz] [-b boundif] [-i interval] [-p source_port]
        [-s source_ip_address] [-w timeout] [-X proxy_protocol] [-x proxy_address[:port]]
        [--apple-delegate-pid pid] [--apple-delegate-uuid uuid] [--apple-ext-bk-idle]
        [--apple-nowakefromsleep n] [--apple-ecn mode] [hostname] [port[s]]

DESCRIPTION
     The nc (or netcat) utility is used for just about anything under the sun involving
     TCP or UDP.  It can open TCP connections, send UDP packets, listen on arbitrary TCP
     and UDP ports, do port scanning, and deal with both IPv4 and IPv6.  Unlike
     telnet(1), nc scripts nicely, and separates error messages onto standard error
     instead of sending them to standard output, as telnet(1) does with some.

     Common uses include:

           o   simple TCP proxies
           o   shell-script based HTTP clients and servers
           o   network daemon testing
           o   a SOCKS or HTTP ProxyCommand for ssh(1)
           o   and much, much more

     The options are as follows:

     -4      Forces nc to use IPv4 addresses only.

     -6      Forces nc to use IPv6 addresses only.

     -A      Set SO_RECV_ANYIF on socket.

     -b boundif
             Specifies the interface to bind the socket to.

     -c      Send CRLF as line-ending

     -D      Enable debugging on the socket.

     -C      Forces nc not to use cellular data context.

     -d      Do not attempt to read from stdin.

     -h      Prints out nc help.

     -i interval
             Specifies a delay time interval between lines of text sent and received.
             Also causes a delay time between connections to multiple ports.

     -G conntimeout
             TCP connection timeout in seconds.

     -H keepidle
             Initial TCP keep alive timeout in seconds.
:
```

---
