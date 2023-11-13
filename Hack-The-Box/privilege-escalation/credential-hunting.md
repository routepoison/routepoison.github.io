# Credential Hunting

When enumerating a system, it is important to note down any credentials. These may be found in configuration files (.conf, .config, .xml, etc.), shell scripts, a user's bash history file, backup (.bak) files, within database files or even in text files. Credentials may be useful for escalating to other users or even root, accessing databases and other systems within the environment.

The /var directory typically contains the web root for whatever web server is running on the host. The web root may contain database credentials or other types of credentials that can be leveraged to further access. A common example is MySQL database credentials within WordPress configuration files:

`cat wp-config.php | grep 'DB_USER\|DB_PASSWORD'`

The spool or mail directories, if accessible, may also contain valuable information or even credentials. It is common to find credentials stored in files in the web root (i.e. MySQL connection strings, WordPress configuration files).

`find / ! -path "*/proc/*" -iname "*config*" -type f 2>/dev/null`

## SSH Keys

It is also useful to search around the system for accessible SSH private keys. We may locate a private key for another, more privileged, user that we can use to connect back to the box with additional privileges. We may also sometimes find SSH keys that can be used to access other hosts in the environment. Whenever finding SSH keys check the known_hosts file to find targets. This file contains a list of public keys for all the hosts which the user has connected to in the past and may be useful for lateral movement or to find data on a remote host that can be used to perform privilege escalation on our target.

`ls ~/.ssh`

---

↩️: [Home](../../index.md)
