# Xrdp

Xrdp is open-source implementation of Microsoft's RDP.

## Install

```
sudo apt update
sudo apt install xrdp
sudo systemctl enable xrdp
```

### Validate xrdp is Running

```
sudo systemctl status xrdp
```

## Connecting to Ubuntu Server

Server's don't always have GUI setup. Run these commands to install required packages.

```
sudo apt update
sudo apt install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils
```

Next, xrdp user to the ssl-cert group:

```
sudo adduser xrdp ssl-cert
```

If the Ubuntu Firewall is enabled, run the following example with proper parameters:

```
sudo ufw allow from 192.168.1.0/24 to any port 3389
sudo ufw allow 3389
```


---
