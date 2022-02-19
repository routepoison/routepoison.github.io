# Ubuntu Commands

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

---
