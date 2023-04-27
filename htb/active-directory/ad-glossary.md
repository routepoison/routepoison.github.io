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

### Container

### Leaf

### Global Unique Identifier (GUID)

### Security Principals

### Security Identifier (SID)

### Distinguished Name (DN)

### Relative Distinguished Name (RDN)

### sAMAccountName

### userPrincipleName

### FSMO Roles

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
