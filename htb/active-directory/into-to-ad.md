# Introduction to Active Directory

## Why?

Active Directory is a directory service for Windows network environments. It is a distributed, hierarchical structure that allows for centralized management of an organization's resources, including:

* users
* computers
* groups
* network devices
* file shares
* group policies
* devices
* trusts

AD provides authentication and authorization functions within a Windows domain environment.

It has come under increasing attack in recent years. It is designed to be backward-compatible, and many features are arguably not 'secure by default,'  and it can be easily misconfigured.

This weakness can be leveraged to move laterally and vertically within a network and gain unauthorized access. AD is essentially a sizeable read-only database accessible to all users within the domain, regardless of their privilege level.

AS is essentially a sizeable read-only database accessible to all users within the domain, regardless of their privilege level. A basic AD user account with no added privleges can enumerate most objects within AD. 

This fact makes it extremely important to properly secure an AD implementation because ANY user account, regardless of their privilege level, can be used to enumerate the domain and hunt for misconfigurations and flaws thoroughly. 

Also, multiple attacks can be performed with only a standard domain user account, showing the importance of a defense-in-depth strategy and careful planning focused on security and hardening AD, network segmentation, and least privilege.

One example is the [noPac] attack that was first released in December of 2021.



---

↩️: [Home](../../index.md)
