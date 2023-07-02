# Windows Attack and Defense

## Kerberoasting

In Active Directory, a __Service Principle Name (SPN)__ is a unique service instance identifier. Kerberos uses SPNs for authentication to associate a service instance with a service logon, account, which allows a slient application to request that the service authenticate an account even if the client does not have the account name. When a Kerberos __TGS__ service ticket is asked for, it gets encrypted with the service account's NTLM password hash.

__Kerberoasting__ is a post-exploitation attack that attempts to exploit this behavior by obtaining a ticket and performing offline password cracking to _open_ the ticket. If the ticket opens, then the candidate password that opened the ticket is ther service account's password.

The success of this attack depends on the strength of the service account's password. Another factor that has some impact is encryption algorithm used when the ticket is created, with the likely options being:

* __AES__
* __RC4__
* __DES__ (found in environment that are 15+ old with legacy apps from the early 2000s, otherwise, this will be disabled)



## AS-REProasting
## GPP Passwords
## GPO Permissions/GPO Files
## Credentials in Shares
## Credentials in Object Properties
## DCSync
## Golden Ticket
## Kerberos Constrained Delegation
## Print Spooler & NTLM Relaying
## Coercing Attacks & Unconstrained Delegation
## Object ACLs
## PKI - ESC1

---

↩️: [Home](../../index.md)
