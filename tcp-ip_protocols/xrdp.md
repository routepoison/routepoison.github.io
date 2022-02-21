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

## From OSX

```
You can use Microsoft Remote Desktop from App Store. Set up your Ubuntu this way:

From DigitalOcean community page.

    sudo apt-get update

If you don't have desktop installed:

    sudo apt-get install ubuntu-desktop

After that install XRDP:

    sudo apt-get install xrdp

Enable XRDP to start on boot:

    sudo systemctl enable xrdp

If you have a firewall make sure that the 3389 port is open:

    sudo ufw allow 3389/tcp

Now connect with Microsoft Remote desktop to your Linux machine.
```

## How to Fix “Authentication is required to create a color profile/managed device”

/etc/polkit-1/localauthority.conf.d/02-allow-colord.conf

> sudo nano /etc/polkit-1/localauthority.conf.d/02-allow-colord.conf

```Create a config profile, reboot, and the message should decease
polkit.addRule(function(action, subject) {
 if ((action.id == "org.freedesktop.color-manager.create-device" ||
 action.id == "org.freedesktop.color-manager.create-profile" ||
 action.id == "org.freedesktop.color-manager.delete-device" ||
 action.id == "org.freedesktop.color-manager.delete-profile" ||
 action.id == "org.freedesktop.color-manager.modify-device" ||
 action.id == "org.freedesktop.color-manager.modify-profile") &&
 subject.isInGroup("{users}")) {
 return polkit.Result.YES;
 }
});
```

---
