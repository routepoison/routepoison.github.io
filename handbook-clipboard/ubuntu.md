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
