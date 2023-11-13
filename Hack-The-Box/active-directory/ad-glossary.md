# Active Directory Glossary

Here are additional definitions that you should be familiar with when dealing with AD:

### Object

An object can be defined as any resource present within an Active Directory environment such as OUs, printers, users, domain controllers, etc.

### Attributes

Every object in AD has an associated set of attributes used to define characteristics ofSthe given object. A computer object contains attributes such as the hostname and DNS name. All attributes in AD have an associated LDAP name that can be used when performing LDAP queries, such as __displayName__ for __FullName__ and __given name__ for __First Name__

### Schema

AD schema is essentially the blueprint of any enterprise environment. It defines what types of objects can exist in the AD database and their associated attributes. It lists definitions corresponding to AD objects and holds information about each object. For example, users in AD belong to the class "user", and computer objects to "computer," and so on. Each object has its own information (some required to be set and others optional) that are stored in Attributes. When an object is created from a class, this is called instantiation, and an object created from a specific call is called an instance of that class. 

### Domain

A domain is a logical group of objects such as computers, users, OUs, groups, etc. We can think of each domain as a different city within a state or country. Domains can operate entirely independetly of one another or be connected via trust relationships.

### Forest

A forest is a collection of Active Directory domains. It is the topmost container and contains all of the AD objects introduced below, including but not limited to domains,users, groups, computers, and Group Policy objects. A forect can contain one or multiple domains and be thouguht of as a state in the US or a country within the EU. Each forest operates independently but may have various trust relationships with other forests.

### Tree

A tree is a collection of Active Directory domains that begins at a single root domain. A forest is a collection of AD trees. Each domain in a tree shares a boundary with the other domains. A parent-child trust relationship is formed when a domain is added underanother domain in a tree. 

Two trees in the same forest cannot share a name (namespace). Let's say we have two trees in an AD forest:

* __inlanefreight.local__
* __ilfreight.local__

A child domain of the first would be __corp.inlandfreight.local__ while a child domain of the second could be __corp.ilfreight.local__. All domains in a tree share a standard Global Catalog which contains all information about objects that belong to the tree.

### Container

Container objects hold other objects and have a defined place in the directory subtree hierarchy.

### Leaf

Leaf objects do not contain other objects and are found at the end of the subtree hierarchy.

### Global Unique Identifier (GUID)

A GUID is a unique 128-bit value assigned when a domain user or group is created. This GUID is unique across the enterprise,  similar to a MAC address. Every single object created by Active Directory is assigned a GUID, not only user and group objects. The GUID is stored in the __ObjectGUID__ attribute. When querying for an AD object (such as a user, group, computer, domain, domain controller, etc.), we can query for its __objectGUID__ value using PowerShell or search for it by specifying its distinguished name, GUID, SID, or SAM account name.

GUIDs are used by AD to identify objects internally. Searching in Active Directory by GUID value is probably the mose accurate and reliable way to find the exact object you ar elooking for, especially if the global catlog may contain.

### Security Principals

Security principals are anything that the operating system can authenticate, including users, computer accounts, or even threads/processes that run in the context of auser or computer account (i.e., an application such as Tomcat running in the context of a service account within the domain). In AD, security groups used to control access to resources on only that specific computer. Thse are not managed by AD but rather by the Security Accounts Manager (SAM).

### Security Identifier (SID)

A security identifier, or SID is used as a unique identifier for a security principle or security group. Every account, group, or process has its own unique SID, which, in an AD environment, is issued by the domain controller and stored in a secure database.

### Distinguished Name (DN)

A Distinguished Name (DN) describes the full path to an object in AD (such as __cn=bjones, ou=IT, ou=Employees, dc=inlanefreight, dc=local__).

In this example, the user __bjones__ works in the IT department of the company Inlanefreight, and his account is created in an Organizational Unit (OU) that holds accounts for company employees. The Common Name (CN) __bjones__ is just one way the user object could be searched or accessed within the domain.

### Relative Distinguished Name (RDN)

A __Relative Distinguished Name (RDN)__ is a single component of the Distinguished Name that identifies the object as unique from other objects at the current level in the naming hierarchy. In our example, __bjones__ is the Relative Distinguished Name of the object. AD does not allow two objects with the same name under the same parent container, but there can be two objects with the same RDNs that are still unique in the domain because they have different DNs. For example, the object __cn=bjones, dc=dev, dc=inlanefreight, dc=local__ would be recognized as different from __cn=bjones, dc=inlanefreight, dc=local.__

### sAMAccountName

The __sAMAccountName__ is the user's logon name. Here it would just be __bjones__. It must be a unique value and 20 or fewer characters.

### userPrincipleName

The __userPrincipleName__ attribute is another way to identify users in AD. This attribute consists of a prefix (the user account name) and a suffix (the domain name) in the format __bjones@inlanefreight.local__. This attribute is not mandatory.

### FSMO Roles

In the early days of AD, if you had multiple DCs in an environment, they would fight over which DC gets to make changes, and sometimes changes would not be made properly. Microsoft then implemented "last writer wins," which could introduce its own problems if the last change breaks things. They then introduced a model in which a single "master" DC could apply changes to the domain while the others merely fulfilled authentication requests. 

This was a flawed design because if the master DC went down, no changes could be made to the environment until it was restored. To resolve this single point of failure model, Microsoft separated the various responsibilites that a DC can have into __Flexible Single Master Operation (FSMO)__ roles.

### Global Catalog

### Read-Only Domain Controller

### Replication

### Service Principle Name (SPN)

### Group Policy Object (GPO)

### Service Principle Name (SPN)

### Group Policy Object (GPO)

### Access Control List (ACL)

### Access Control Entites (ACEs)

### Discretionary Access Control List (DACL)

### System Access Control Lists (SACL)

### Tombstone

### AD Recycle Bin

### SYSVOL

### AdminSDHolder

### deHeuristics

### adminCount

### Active Directory Users and Computers (ADUC)

### ADSI Edit

### sIDHistory

### NTDS.DIT

### NTDS.DIT

### MSBROWSE


---

↩️: [Home](../../index.md)
