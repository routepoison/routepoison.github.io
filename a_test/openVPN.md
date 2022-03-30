# OpenVPN Installation

## Server Install

Open a terminal:

> sudo apt install openvpn easy-rsa

## Public Key Infrastructure Setup & Certificate Authority

Copy **easy-rsa** directory to */etc/openvpn'. This ensures that any changes to the scripts will not be lost whe packages update. From terminal:

> sudo make-cadir /etc/openvpn/easy-rsa

**Note**: If desired, you can alternatively edit */etc/openvpn/easy-rsa/vars* directory, adjusting it to your needs.

As **root** user change to the newly created diretory */etc/openvpn/easy-rsa* and run:

```
./easyrsa init-pki
./easyrsa build-ca
```

## Server Keys and Certificates

Next, we will generate a key pair for the server:

> ./easyrsa gen-req myservername nopass

Diffie-Hellman parameters must be generated for the OpenVPN server. The following will place them in **pki/dh.pem**.

> ./easyrsa gen-dh

And finally a certificate for the server:

```
./easyrsa gen-req myservername nopass
./easyrsa sign-req server myservername
```

All certificates and keys have been generated in subdirectories. Common practice is to copy them to */etc/openvpn/:*

> cp pki/dh.pem pki/ca.crt pki/issued/myservername.crt pki/private/myservername.key /etc/openvpn/

## Client Certificates

The VPN client will also need a certificate to authenticate itself to the server. Usually you create a different certificate for each client.

This can either be done on the server (as the keys and certificates above) and then securely distributed to the client. Or vice versa: the client can generate and submit a request that is sent and signed by the server.

To create the certificate, enter the following in terminal while being **root** user.

```
./easyrsa gen-req myclient1 nopass
./easyrsa sign-req client myclient1
```

If the command above was done on a remote system, then copy the **.req** file to the CA server. There you can import it via 

> easyrsa import-req /incoming/myclient1.req myclient1

Then you can go on with the second **sign-eq** command:

In both cases, afterwards copy the following files to the client using a secure method:

* **pki/ca.crt**
* **pki/issued/myclient.crt**

As the client certificates and keys are only required on the client machine, you can remove them from the server.

## Simple Server Configuration

---
