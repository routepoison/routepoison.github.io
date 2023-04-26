# Introduction to Active Directory

## Contents

* Overview
    + Why?
    + Research over the years
* Fundamentals
* AD Protocols
* Users
* Advanced
* In Practice
* Summary

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

AD is essentially a sizeable read-only database accessible to all users within the domain, regardless of their privilege level. A basic AD user account with no added privleges can enumerate most objects within AD. 

This fact makes it extremely important to properly secure an AD implementation because ANY user account, regardless of their privilege level, can be used to enumerate the domain and hunt for misconfigurations and flaws thoroughly. 

Also, multiple attacks can be performed with only a standard domain user account, showing the importance of a defense-in-depth strategy and careful planning focused on security and hardening AD, network segmentation, and least privilege.

One example is the [noPac](https://www.secureworks.com/blog/nopac-a-tale-of-two-vulnerabilities-that-could-end-in-ransomware) attack that was first released in December of 2021.

AD makes info easy to find and use for adminstrators and users. AD is highly scalable, supports millions of objects per domain, and allows the creation of additional domains as an organization grows.

---

It is estimated that 95% of Fortune 500 companies run Active Directory, making AD a key focus for attackers. A successful attack within AD that provides standard domain user gives enough access to begin mapping out the domain and looking for avenues of attack. As a security professional, expect to encounter AD environments of all sizes. This makes it essential to understand structure and function of AD.

## History of AD

LDAP, the foundation of Active Directory, was first introduced in RFCs as early as 1971. Active Directory was predated by the X.500 organizational unit concept, which was the earliest version of all directory systems created by Novell and Lotus and released in 1993 as Novell Directory Services.

---

↩️: [Home](../../index.md)
