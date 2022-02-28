# Readme

## Linux Commands

> sudo apt update

> sudo apt install python3-pip

```python
# Script to list all Python packages into a list
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
print(installed_packages_list)
```

> pip list

```python
WARNING: You are using pip version 20.1.1; however, version 20.3.4 is available.
You should consider upgrading via the '/usr/local/opt/python@2/bin/python2.7 -m pip install --upgrade pip' command.
```

> '/usr/local/opt/python@2/bin/python2.7 -m pip install --upgrade pip'

> which pip

```shell
~ % which pip 
/usr/local/bin/pip
```

To change default pip to pip3, run:

> sudo ln -s /usr/local/bin/pip3 /usr/local/bin/pip

The  pipenv lock -r command can be used to generate output from a pipfile.lock file in a pipenv environment. All packages, including dependencies will be listed in the output. For example:

pipenv lock -r

### virtual env

python3 -m venv venv 
source venv/bin/activate

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
