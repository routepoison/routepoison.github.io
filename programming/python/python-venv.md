C:\Users\grs\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\Scripts

$ sudo apt update
$ sudo apt install python3-pip
$ python3 -m venv venv 
$ source venv/bin/activate
(venv) $
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
