# Active Directory Fundamentals

Active Directory is a directory service for Windows network environments. It has a distributed, hierarchichal structure that allows for centralized management of an organization's resources, including users, computers, groups, network devices and file shares, group policies, servers and workstations, and trusts. 

AD provides authentication and authorization functions within Windows.

A directory service, such as _Active Directory Domain Services (AD DS)_ gives an organization ways to store directory data and make it available to both standard users and administrators on the same network. AD DS stores information such as usernames and passwords and manages rights needed to authorized users to access this information.

First shipped in Windows Server 2000; it has come under increasing attack in recent years. Many features are arguably not 'secure by default'. Difficult to manage properly, especially in large environments.

Active Directory flaws and misconfigurations can often be used to obtain a foothold (internal access), move laterally and vertically within a network, and gain unauthorized access to protected resources such as databases, file shares, source code, and more. 

AD is essentially a large database accessible to all users within the domain, regardless of their privilege level. A basic AD user account with no added privileges can be used to enumerate the majority of objects contained within AD, including but not limited to:

| Domain Computers | Domain Users |
| Domain Group Information | Organizaations Units (OUs) |
| Default Domain Policy | Functional Domain Levels |
| Password Policy | Group Policy Objects (GPOs) |
| Domain Trusts | Access Control Lists (ACLs) |

For this reason, we must understand how Active Directory is set up and the basics of administration before attempting to attack it.

## Active Directory Engagements

AD is arranged in a hierarchical tree structure, with a forest at the top containing one or more domains, which can themselves have nested subdomains.



---

↩️: [Home](../../index.md)
