# venv (Virtual Environment)

## installation

If you haven’t installed pip, you can install it

> sudo apt-get install python3-pip

### Install Virtualenv using pip3

> sudo pip3 install virtualenv

### You can create a virtual environment

> virtualenv venv

### You can use the specific version

> virtualenv --python python3 venv

### You can use specific interpreter

> virtualenv -p /usr/bin/python2.7 venv

### Activate your virtual environment

> source venv/bin/activate

### How to deactivate?

> deactivate

### If you face any issues in Ubuntu, you may need to install

> sudo apt-get install build-essential libssl-dev libffi-dev python-dev

---

```
C:\Users\grs\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\Scripts

$ sudo apt update

$ sudo apt install python3-pip

$ python3 -m venv venv 

$ source venv/bin/activate

(venv) $ which python
/home/echou/venv/bin/python
(venv) $ deactivate

grs@ubuntu:$ python3 -m venv venv
grs@ubuntu:$ which python
grs@ubuntu:$ source venv/bin/activate
(venv) grs@ubuntu:$ which python
/home/grs/venv/bin/python
(venv) grs@ubuntu:$ deactivate 
grs@ubuntu:$ python3 -m venv grs
grs@ubuntu:$ source grs/bin/activate
(grs) grs@ubuntu:$ which python
/home/grs/grs/bin/python
(grs) grs@ubuntu:$ deactive
deactive: command not found
(grs) grs@ubuntu:$ deactivate 
```

---
