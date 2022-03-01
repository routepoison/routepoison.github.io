# Linux General Commands

## Kali Linux

### Starting, Stopping Services

We will use SSH as an example, by default, it will generally be turned off when first booting Kali. You can check the status and start it as follows:

> service ssh start

The check the current status:

```linux
┌──(grs㉿kali)-[~]
└─$ service ssh status
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; disabled; vendor prese>
     Active: active (running) since Mon 2022-02-28 16:40:26 EST; 1min 46s ago
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 234497 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SU>
   Main PID: 234498 (sshd)
      Tasks: 1 (limit: 9321)
     Memory: 2.2M
        CPU: 276ms
     CGroup: /system.slice/ssh.service
             └─234498 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startu>
```

Now we can add and whitelist SSH so the service will start automatically whenever the server is rebooted. This will allow you to review current services:

> cat /usr/sbin/update-rc.d 

Comment out SSH from the blackisted section, and enable it on the whitelist section. Then finally you can update the system to start.

```
update-rc.d ssh defaults
update-rc.d ssh enable
```

Thats all you need and now SSH will start when you reboot. The _rc.local_ file is executed after all the normal Linux services have started.

```
┌──(grs㉿kali)-[~]
└─$ /etc/init.d/ssh start
Starting ssh (via systemctl): ssh.service.
```

---
