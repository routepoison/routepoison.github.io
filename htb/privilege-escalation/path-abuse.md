# PATH Abuse

PATH is an environnment variable that specifies the set of directories where an executable can be located. An account's PATH variable is a set of absolute path to the binary. For example, a user can type `cat /tmp/test.txt` instead of specifying the absolute path `/bin/cat /tmp/test.txt` We can check the contents of the PATH variable by typing `env | grep PATH` or `echo $PATH`

`echo $PATH`

Creating a script or program in a directory specified in the PATH will make it executable from any directory on the system.


`pwd && conncheck`

The `conncheck` script created in `/usr/local/sbin` will still run when in the **/tmp** directory because it was created in a directory specified in the PATH

Adding **.** to the user's PATH adds their current working directory to the list. For example, if we modify a user's PATH, we could rplace a common binary such as ls with a malicious script such as a reverse shell. If we add **.** to the path by issuing the command 

`echo $PATH`

```
PATH=.:${PATH}
export PATH
echo $PATH
```

In this next example, we modify the path to run a simple echo command when the command **ls** is typed.

```
touch ls
echo 'echo "PATH ABUSE!"' > ls
chmod +x ls
```

---

↩️: [Home](../../index.md)
