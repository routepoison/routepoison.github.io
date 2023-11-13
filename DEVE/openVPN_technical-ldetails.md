# OpenVPM Techincal Details

## Public Key Infrastructure Setup

The first step in building an OpenVPN configuration is to establish a **PKI** (_public key infrastructure_)

A PKI consists of:

* a seperate cert (public key cert) and private keys for the server and each cl ient.
* a master Certificate Authority (CA) certificate and key, used to sign the server and client certificates.

OpenVPN supports bidirectional authencation based on certificates, meaning that the client must authenticate the server certifcate and the server must authenticate the client certification before mutual trust is established.

Both server and client will authenticate the other by first verifying that the presented certicate was signed by the master certificate authority (CA), and then by testing information in the now-authenticated certificate header, such as the certificate common name or certificate type (client or server)

## Certificate Authority Setup

To setup your own CA, and generate certificates and keys for an OpenVPN Server and multiple clients, first copy the **easy-rsa** directory to '/etc/openvpn/easy-rsa', and run:

```
mkdir /etc/openvpn/easy-rsa
cd /etc/openvpn/easy-rsa



```

OK, the additional portions are too challenging to type on Delta's shitty Wi-Fi I just paid $30 for,



---
