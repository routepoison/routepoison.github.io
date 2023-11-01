# Special Permissions

The **Set User ID upon Execution** (**setuid**) permission can allow a user to execute a program or script with the permissions of anothre user, typically with elevated privileges. The **setuid** bit appears as an **s**.

`find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null`

It may be  possible to reverse engineer the program with the SETUID bit set, identify a vulnerability, and exploit this to escalate our privileges. Many programs have additional features that can be leveraged to execute commands and, if the **setuid** bit is set on them, these can be used for our purpose.

The Set-Group-ID (setgid) permission is another special permission that allows us to run binaries as if we were part of the group that created them. These files can be enumerated using the following command: `find / -uid 0 -perm -6000 -type f 2>/dev/null`. These files can be leveraged in the same manner as **setuid** binaries to escalate privileges.

`find / -user root -perm -6000 -exec ls -ldb {} \; 2>/dev/null`

[Check here](https://linuxconfig.org/how-to-use-special-permissions-the-setuid-setgid-and-sticky-bits) for more information about the **setuid** and **setgid** bits, including how to set bits.

## GTFOBins

The [GTFOBins](https://gtfobins.github.io/) project is a curated list of binaries and scripts that can be used by an attacker to bypass security restrictions. Each page details the program's features that can be used to break out of restricted shells, escalate privileges, spawn reverse shell connections, and transfer files. For example, **apt-get** can be used to break out of restricted environments and spawn a shell by adding Pre-invoke command:

`sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh`

It's worth familiaring ourselves with as many GTFOBins as possible to quickly identify misconfigurations when we land on a system that we must escalate our privileges to move further.

---

↩️: [Home](../../index.md)
