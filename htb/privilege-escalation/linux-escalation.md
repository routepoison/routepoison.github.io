# Introduction to Linux Privilege Escalation

The root account on Linux systems provides full administrative leve access to the operating system. During an assessment, you may gain a low-privleged shell on a Linux host and need to perform privilege escalation to the root account.

Fully compromising the host would allow us to capture traffic and access sesnsitive files, which may be used to further access withing the environment.

Additionally, if the Linux machine is domain joined, we can gain the NTLM hash and being enumerating and attacking Active Directory.

## Enumeration

Enumeration is the key to privilege. Several helper scripts (such as LinEnum) exist to assist with enumeration. Still, it is also important to understand what pieces of information to look for and to be able to perform your enumeration manually. When you gain initial shell access to the host, it is important to check several key details.

## Versioning

### OS Version

Knowing the distribution (Ubuntu, Debian, FreeBSD, Fedora, SUSE, Red Hat, CentOS, etc.) will give you an idea of the types of tools that may be available. This would also identify the operating system version, for which there may be public exploits available.

### Kernal Version

As with the OS version, there may be public exploits that target a vulerability in a specific kernel version. Kernel exploits can cause system instability or even a complete crash. Be careful running these against any production system , and make sure you fully understand the exploit and possible ramifications before running one.

### Running Services

Knowing what services are running on the host is important, especially those running as root. A misconfigured or vulerable service running as root can be an easy win for privilege escalation. Flaws have been discovered in many common services such as Nagios, Exim, Samba, ProFTPd, etc. Public exploit PoXs exist for many of them, such as CVE-2016-9566, a local privilege esclataion flaw in Nagios Core < 4.2.4.

#### List Current Processes

`ps aux | grep root`

Let's get down to business.

**Installed Packages and Version**: Like running services, it is important to check for any out-of-date or vulnerable packages that may be easily leveraged for privilege escalation. An example is Screen, which is a common terminal multiplexer (similar to tmux). It allows you to start a session and open many windows or virtual terminals instead of opening multiple terminal sessions.

Screen version 4.05.00 suffers from a privilege escalation vulnerability that can be easily leveraged to escalate privileges.

**Logged in Users**: Knowing which other uses are logged into the system and what they are doing can give greater insight into possible local lateral movement and privilege escalation paths

`ps au`

**User Home Directories**: Are other user's home directories accessible? User home folders may also contain SSH keys that can be used to access other systems or scripts and configuration files containing credentials. It is not uncommon to find files containing credentials that can be leveraged to access other systems or even gain entry into the Active Directory environment.


## Home Directory Contents

`ls /home`

We can check individual user directories and check to see if files such as the **.bash_history** file are readable and contain any interesting commands, look for configuration files, and check to see if we can obtain copies of a user's SSH keys.

### SSH Directory

`ls -l ~/.ssh`

## Bash History

`history`

**Sudo Privileges**: Can the user run any commands either as another user or as root? If you do not have credentials for the user, it may not be possible to leverage sudo permissions. However, often sudoer entries include **NOPASSWD**, meaning that the user can run the specified command without being prompted for a password. Not all commands, even we can run as root, will lead to privilege escalation. It is not uncommon to gain access as a user with full sudo privileges, meaning they can run any command as root. Issuing a simple **sudo su** command will immediately give you a root session.

## Sudo - List User's Privilege

`sudo -l`


**Configuration files**: Configuration files can hold a wealth of information. It is worth searching through all files that end extensions such as **.conf** and **.config** for usernames, passwords, and other secrets.

**Readable Shadow File**: If the shadow file is readable, you will be able to gather password hashes for al users who have a password set. While this does not guarantee further access, these hashes can be subjected to an offline brute-force attack to recover the cleartext password

**Password Hashes in /etc/passwd**: Occasionally, you will see password hashes directly in the /etc/passwd file. This file is readable by all users, and as with hashes in the **shadow** file, these can be subjected to an offline password cracking attack. This configuration, while not common, can sometimes be seen on embedded devices and routers.

## Passwd

cat /etc/passwd

**Cron Jobs**: Cron jobs on Linux systems are similar to Widnows scheduled tasks. They are often set up to perform maintenance and backup tasks. In conjunction with other such as relative paths or weak permissions, they can leverage to escalate privileges when the scheduled cron job runs.

`ls -la /etc/cron.daily/`

**Unmounted File Systems and Additional Drives**: If you discover and can mount an additional drive or unmounted file system, you may find sensitive files, passwords, or backups that can be leveraged to escalate privileges.

## File Systems & Additional Drives

`lsblk`

**SETUID and SETGID Permissions**: Binaries are set with these permissions to allow a user to run a command as root, without having to grant root-level access to the user. Many binaries contain functionality that can be exploited, to get a root shell.

**Writeable Directories**: It is important to discover which directories are writeable if you need to download tools to the system. You may discover a writeable directory where a cron job places files, which provides an idea of how often the cron job  runs and could be used to elevate privileges if the script that the cron job runs is also writeable.

## Find Wiretable Directories

`find / -path /proc -prune -o -type d -perm -o+w 2>/dev/null`

**Writeable Files**: Are any scripts or configuration files world-writeable? While altering configuration files can be extremely destructive, there may be instances where a minor modifications can open up further access. Also, any scripts that are run as root using cron jobs can be modified slightly  to append a command.

## Find Writeable Files

`find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null`

## Cheatsheet

| **Command** | **Description** |
| --------------|-------------------|
| `ssh htb-student@<target IP>` | SSH to lab target |
| `ps aux \| grep root` | See processes running as root |
| `ps au` | See logged in users |
| `ls /home` | View user home directories |
| `ls -l ~/.ssh` | Check for SSH keys for current user |
| `history` | Check the current user's Bash history |
| `sudo -l` | Can the user run anything as another user? |
| `ls -la /etc/cron.daily` | Check for daily Cron jobs |
| `lsblk` | Check for unmounted file systems/drives |
| `find / -path /proc -prune -o -type d -perm -o+w 2>/dev/null` | Find world-writeable directories |
| `find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null` | Find world-writeable files |
| `uname -a` | Check the Kernel versiion |
| `cat /etc/lsb-release ` | Check the OS version |
| `gcc kernel_expoit.c -o kernel_expoit` | Compile an exploit written in C |
| `screen -v` | Check the installed version of `Screen` |
| `./pspy64 -pf -i 1000` | View running processes with `pspy` |
| `find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null` | Find binaries with the SUID bit set |
| `find / -user root -perm -6000 -exec ls -ldb {} \; 2>/dev/null` | Find binaries with the SETGID bit set |
| `sudo /usr/sbin/tcpdump -ln -i ens192 -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root` | Priv esc with `tcpdump` |
| `echo $PATH` | Check the current user's PATH variable contents |
| `PATH=.:${PATH}` | Add a `.` to the beginning of the current user's PATH |
| `find / ! -path "*/proc/*" -iname "*config*" -type f 2>/dev/null` | Search for config files |
| `ldd /bin/ls` | View the shared objects required by a binary |
| `sudo LD_PRELOAD=/tmp/root.so /usr/sbin/apache2 restart` | Escalate privileges using `LD_PRELOAD` |
| `readelf -d payroll  \| grep PATH` | Check the RUNPATH of a binary |
| `gcc src.c -fPIC -shared -o /development/libshared.so` | Compiled a shared libary |
| `lxd init` | Start the LXD initialization process |
| `lxc image import alpine.tar.gz alpine.tar.gz.root --alias alpine` | Import a local image |
| `lxc init alpine r00t -c security.privileged=true` | Start a privileged LXD container |
| `lxc config device add r00t mydev disk source=/ path=/mnt/root recursive=true` | Mount the host file system in a container |
| `lxc start r00t` | Start the container |
| `showmount -e 10.129.2.12` | Show the NFS export list |
| `sudo mount -t nfs 10.129.2.12:/tmp /mnt` | Mount an NFS share locally |
| `tmux -S /shareds new -s debugsess` | Created a shared `tmux` session socket |
| `./lynis audit system` | Perform a system audit with `Lynis` |

---

↩️: [Home](../../index.md)
