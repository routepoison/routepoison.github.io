# Ubuntu Commands

## Update System

Simple command to update packages, also can test your privileges with it.

> sudo apt update

## Working with Packages

```
! List Packages
sudo apt list --installed
! List Less Packages
sudo apt list --installed | less
! List Specific Package
sudo apt list --installed | grep -i package_name
```

### Another way to view packages

> sudo dpkg-query -l | less

## Installing Packages & Applications

### Install App

> sudo apt install ./[APP.deb]

### Uninstall App

> sudo apt remove 

## Add User

```
sudo adduser [USERNAME]
```

```
! view hashed passwords
cat /etc/passwd | grep cloudcone
```

```
! add user to sudo group
sudo usermod -aG sudo [USERNAME]
```

## Messaging in Ubuntu

```
wall "System will go down for 2 hours maintenance at 13:00 PM"
```

## Open Current Directory

Open current working directory in shell.

> xdg-open .

##

---
