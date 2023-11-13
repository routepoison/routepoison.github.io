# Environment Enumeration

Enumeration is the key to privilege escalation. Several helper scripts (such as LinPEAS and LinEnum) exist to assist with enumeration. Still, it is important to understand what pieces of information to look for an to be able to perform your enumeration manually. When you gain intial shell access to the host, it is important to check several key details.

**OS Version**: Knowing the distribution will you give an idea of the types of tools that may be available. This would also identify the operating system version, for which there may be public exploits available.

**Kernel Version**: As with the OS version, there may be public exploits that target a vulnerability in a specific kernel version. Kernel exploits can cause system instability or even a complete crash. Be careful running these against any production system, and make sure you fully understand the exploit and possible ramifications before running one.

**Running Services**: Knowing what services are running on the host is important, especially those running as root. A misconfigured or vulnerable service running as root can be an easy win for privilege escalation. Flaws have been discovered in many common services such as Nagios,Exim,Samba,ProFTPd. Public exploit PoCs exist for many of them, such as CVE-2016-9566, a local privilege escalation flaw in Nagios Core < 4.2.4.

## Gaining Situational Awareness

Let's say we have just gained access to a Linux host by exploiting an unrestricted file upload vulnerabilitly during an External Penetration Test. After establishing our reverse shell (and ideally some sort of persistence), we should start by gatherin some basics about the system we are working with.

First, we'll answer the fundemental question: What operating system are we dealing with? If we landed on a CentOS host or Red Hat Enterprise Linux Host, our enumeration would likely be slightly different than if we landed on a Debian-based host such as Ubuntu. If we land on a host such as FreeBSD,Solaris, or something more obscure such as a HP proprietary OS HP-UX or the IBM OS AIX, the commands we would work with will likely be different. Though the commands may be different, and we may even need to look up a command reference in some instances, the principles are the same.

For our purposes, we'll begin with an Ubuntu target to cover general tactics and techniques. Once we learn the basics and combine them with a new way of thinking and the stages of the Penetration Testing Process, it shouldn't matter what type of Linux system we land on because we'll have a thorough and repeatable process.

There are many cheat sheets out there to help with enumerating Linux systems and some bits of information we are interested in will have two or more ways to obtain it. In this module we'll cover one methodology that can likely be used for a majority of Linux Systems that we envounter in the wild. That being said, make sure you understand what the commands are doing and how to tweak them or find the information you need a different way if a particular command doesn't work. Challenge yourself during this module to try things various ways to practice your methodology and what works best for you.

Anyone can re-type commands from a cheat sheet but a deep understanding of what you are looking for and how to obtain it will help us be successful in any environment.

Let's orientate ourselves:

* `whoami` - what user are we running as
* `id` - what groups does our user belong to
* `hostname` - what is the server named, can we gather anything from the naming
* `ifconfig` or `ip -a` what subnet did we land in, does the host have additional NICs in other subnets
* `sudo -l` - can our user run anything with sudo (as another user as root) without needing a password? this can sometimes be the easiest win and we can do something like sudo su and drop right into a root shell

The above information can be helpful in a client report to provide evidence of a successful Remote Code Execution (RCE) and to clearly identify the affected system. 

`cat /etc/os-release`

After checking the OS, we'll want to check out our current user's PATH. This is where the Linux system looks every time a command is executed for any executables to match the name of what we type, i.e., **id** which on this system is located at **/usr/bin/id**. As we'll see later in this module, if the PATH variable for a target user is misconfigured we may be able to leverage it to escalate privileges. For now we'll note it down and add it to our notetakikng tool of choice.

`echo $PATH`

We can also check out all the environment variables that are set for our current user, we may get lucky and find something sensitive in there such as a password. We'll note this down and move on.

`env`

Next we'll note down the Kernel version. We can do some searches to see if the target is vulnerable Kernel (which we'll take advantage of later) which has some public exploit PoC. We can do this a few ways, another way would be `cat /proc/version` but we'll use the `uname -a` command.

`uname -a`

We can next gather some additional information about the host itself such as the CPU type/version:

`lscpu`

What login shells exist on the server? Note these down and highlight that both Tmux and Screen are available to us.

`cat /etc/shells`

You can also check to see if any defenses are in place and we can enumerate any info about them:

* exec shield
* iptables
* apparmor
* SELinux
* fail2ban
* snort
* uncomplicated firewall (ufw)

Often we will not have the privileges to enumerate the configurations of these protections but knowing what, if any, are in place, can help us not to waste time on certain tasks.

Next, look at the drives and any shares on the system. First, we can use the `lsblk` command to enumerate information about block devices on the system (hard disks, USB drives, optical drives, etc.) IF we discover and can mount an additional drive or unmounted file system, we may find sensitive files, passwords, or backups that can be leveraged to escalate privileges.

`lsblk`

The command `lpstat` can be used to find information about any printers attached to the system. If there are active or queued print jobs we can gain access to some sort of sensitive information?

We should also check for mounted drives and unmounted drives. Can we mount an unmounted drive and gain access? Can we find any type of credentials in **fstab** for mounted drives by grepping for common words such as password, username, credential, etc. in **/etc/fstab**?

Check out the routing table by typing `route` or `netstat -rn`. Here we can see what other networks are avilable via which interface.

In a domain environment we'll definitely want to check **/etc/resolve.conf** if the host is configured to use internal DNS we may be able to use this as a starting point to query the Active Directory Environment.

We'll also want to check the ARP table with `arp -a`

The environment enumeration also includes knowledge  about the users that exist on the target system. This is because individual users are often configured  during the installation of applications and services to limit the service's privileges. The reason for this is to maintain the security of the system itself. Because if a service is running with the highest privileges (root) and this is brought under the control of an attacker, the attacker will automatically have the highest rights over the system.

All users on the system are stored in the **/etc/passwd** file. The format goes as follows:

* username
* password
* user ID
* group ID
* home ID
* home directory
* shell

Occasionally, we'll see password hashes directly in the **/etc/passwd** file. This file is readable by all users, and as with hashes in the **/etc/shadow** file, these can be subjected to an offline password cracking attack. This configuration, while not common, can sometimes be seen on embedded devices and routers.

`cat /etc/passwd | cut -f1 -d:`

With Linux, several different hash algorithms can be used to make the passwords unrecognizable. Identifying them from the first hash blocks can help us to use and work with them later if needed. Here is a list of the most used ones:

| **Algorithm** | **Hash** |
| --------------|-------------------|
| Salted MD5 | `$1$`... |
| SHA-256| `$5$`... |
| SHA-512 | `$6$`... |
| BCrypt | `$2a$`... |
| Scrypt | `$7$`... |
| Argon2 | `$argon2i$`... |

We'll also want to check which users have login shells. Once we see what shells are on the system, we can check each version for vulnerabilities. Because outdated versions, such as Bash v4.1, are vulnerable to **shellshock** exploit.

`grep "*sh$" /etc/passwd`

Each user in Linux systems is assigned to a specific group or groups and thus receives special privileges. For example, if we have a folder named **dev** only for developers, a user must be assigned to the appropriate group to access that folder. The information about the available groups can be found in the **/etc/group** file, which shows us both the group name and the assigned usser names.

## Existing Groups

`cat /etc/group`

The **cat /etc/group** file lists all of the groups on the system. We can then use the [getent](https://man7.org/linux/man-pages/man1/getent.1.html) command to list member of any interesting groups.

`getent group sudo`

We can also check out which users have a folder under the **/home** directory. We'll want to enumerate each of these to see if any of the system users are storing any sensitive data, files containing passwords. We should check to see if files such as the **.bash_history** file are readable and contain any interesting commands and look for configuration files. It is not uncommon to find files containing credentials that can be leverage to access other systems or even gain entry into the Active Domain environment. Its also important to check for SSH keys for all users, as these could be used to achieve persistence on the system, potentially to escalate privleges, or to assist with pivoting and port forwarding further into the internal network. At the minimum, check the ARP cache to see what other hosts are being accessed and cross-reference these against any useable SSH private keys.


`ls /home`

Finally, we can search for any "low hanging fruit" such as config files, and other files that may contain sensitive information. Configuration files can hold a wealth of information. it is worth searching through all files that end in extensions such as .conf and .config, for usernames passwords, and other secrets.

If we've gathered any passwords we should try them at this time for all users present on the system. Password re-use is common.

In Linux, there are many different places where such files can be stored, including mounted file systems. A mounted file system is a file system that is attached to a particular directory on the system and accessed through that directory. many file systems, such as ext4, NTFS, and FAT32, can be mounted. Each type of file system has its own benefits and drawbacks. 

For example, some file systems can only be read by the operating system, which other can be read and written by the user. File systems that can be read and written by the user are called read/write file systems. mounting a file system allows the user to access the files and folders stored on that file system. In order to mount a file system, a user must have root privileges, Once a file system is mounted, it can be unmounted by the user with root privileges. We may have access to such file systems and find info, docs, or applications.

`df -h`

## Mounted File Systems

When a file system is unmounted, it is no longer accessible by the system. This can be done for various reasons, such as when a disk is removed, or a file system is no longer needed. Another reason may be that files, scripts, documents, and other important information must not be mounted and viewed by a standard user. Therefore, if we can extend our privleges to the **root** user, we could mount and read these file systems ourselves. Unmoutned file systems can be viewed as follows:

## Unmounted File Systems

`cat /etc/fstab | grep -v "#" | column -t`

Many folders and files are kept hidden on a Linux system so they are not obvious, and accidental editing is prevented. Why such file ands folders are kept hidden, there are many more reasons than those mentioned so far. Nevertheless, we need to be able to locate all hidden files and folders because they often contain senstive information, even if we have read-only permission.

## All Hidden Files

`find / -type f -name ".*" -exec ls -l {} \; 2>/dev/null | grep username`

## All Hidden Directory

`find / -type d -name ".*" -ls 2>/dev/null`

In addition, three default folders are intended for temporary files. These folders are visible to all users and can be read. In addition, temporary logs or script output can be found there.

Both **/tmp** and **/var/tmp** are used to store data temporarily. However, the key difference is how long the data is stored in these file systems. The data rention time for **/var/tmp** is much longer than that of **/tmp** directory. By default, all files and data stored in **/var/tmp** are trained for up to 30 days. In **/tmp**, on the other hand, the data is automatically deleted after ten days.

In addition, all the temporary files stored in the **/tmp** directory are deleted immediately when the system is restarted. Therefore, the **/var/tmp** directory is used by programs to store data that must be kept between reboots temporarily.

## Temporary Files

`ls -l /tmp /var/tmp /dev/shm`

## Moving On

We've gotten an initial lay of the land and some sensitive or useful data points that can help us on our way to escalating privileges or even moving laterally in the internal network. Next we'll look at permissions, and check to see what directories, scripts, binaries, etc we can read and write with our current user privileges.

Though we are focusing on manual enumeration in this module, its worth running the [linPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS) script at this point in a real-world test.

---

↩️: [Home](../../index.md)
