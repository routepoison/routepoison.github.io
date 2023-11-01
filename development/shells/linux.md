# Linux General Commands

## Kali Linux

### Check Versions

> lsb_release -a

> cat /etc/os-release 

> hostnamectl

> cat /proc/version

### Getting Started

The first thing is to cleanup, and install packages.

```
sudo apt-get clean
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
```

### Managing Packages

Show pack version:

> sudo apt show postgresql

### Customize the Look & Feel

```
$ sudo apt install gnome-tweaks
$ sudo apt install gnome-software
$ gnome-tweaks
$ gnome-software
```
### Disable Autolock

> Settings > Power 

Change the ‘Blank screen‘ option to never. Next, return to your main settings menu and under privacy, switch off the ‘Screen lock‘.

---

## Applications

### FTP

FTP Client/Server required for general usage.

```
$ sudo apt install filezilla filezilla-common -y
## Armitage
```

### Install ToR

Browser used for Onion Network.

> $ sudo apt install tor

### gdebi

Kali comes with dpkg but does not provide dependencies, gdebi manages this.

> $ sudo apt install gdebi

### Katoolin

Katoolin is a tool with which you can add and remove all the necessary Kali Linux repositories and as well as install Kali Linux tools.

```
$ sudo apt install git
$ sudo git clone https://github.com/LionSec/katoolin.git 
$ sudo cp katoolin/katoolin.py /usr/bin/katoolin
$ sudo chmod +x /usr/bin/katoolin
$ sudo katoolin
```

### Install VLC

Best open source media tool.

> $ sudo apt install vlc

If you want to run VLC as root use the command:

> $ sudo sed -i s/geteuid/getppid/g /usr/bin/vlc

## Armitage

Armitage is a graphical user interface for the Metasploit Framework. At first glance, it may seem that Armitage is just a pretty front-end on top of Metasploit. That’s not quite true. Armitage is a scriptable red team collaboration tool. It has a server component to allow a team of hackers to share their accesses to compromised hosts.

[Armitage Website](https://www.cobaltstrike.com/blog/getting-started-with-armitage-and-the-metasploit-framework-2013/)

### MSF

```
sudo msfdb init
sudo msfdb
sudo msfdb start
sudo msfdb init
msfconsole -q 
```

┌──(grs㉿kali)-[~]                                        
└─$ /etc/init.d/postgresql start
Starting postgresql (via systemctl): postgresql.service. 


---
