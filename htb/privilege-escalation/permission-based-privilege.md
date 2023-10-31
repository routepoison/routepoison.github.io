# Permission-based Privilege Escalation

The **Set user ID upon Execution (setuid)** permission can allow a user to execute a program or script with the permissions of another user, typically with elevated privileges. The **setuid** appears as an **s**

`find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null`

It may be possible to reverse engineer program with the SETUID bit set, identify a vulnerability, and exploit this to escalate our privileges. Many programs have additional features that can be leveraged to execute commands and, if the **setuid** bit is set on them, these can be used for our purpose.

The **Set-Group-ID (setgid)** permission is another special permission that allows us to run binaries as if we were part of the group that created them. these files can be enumerated using the following command:

`find / -uid 0 -perm -6000 -type f 2>/dev/null`

These files can be leveraged in the same manner as **setuid** binaries to escalate privilege.

## Special Permissions
## Sudo Rights Abuse
## Privileged Groups
## Capabilities


---

↩️: [Home](../../index.md)
