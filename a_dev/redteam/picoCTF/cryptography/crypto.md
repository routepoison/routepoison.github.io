# Cryptography

Cryptography can assists in achieving many properties or features:

* confidentiality: no one unintended will be able to read the message
* integrity: if a message is tampered, it is possible to detect what it is
* authentication: the identity of a person can be verified accurately
* nonrepudiation: if a person sent a specific message, then the person cannot deny that the message was sent by them

## Compressing and Encrypting files

### Standard Compression

> zip -r my_info.zip my_info/

### Compression with Encryption

This will ask you to encrypt the compression with a password.

> zip --encrypt -r my_protected_info.zip my_info/

### Unzip the compression

Unzip the standard compressed .zip:

> unzip my_info.zip

Unzip the encrypted .zip:

> unzip my_protected_info.zip

##

---
