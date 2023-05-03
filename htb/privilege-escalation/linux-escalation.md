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


---

↩️: [Home](../../index.md)
