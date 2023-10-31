# Escaping Restricted Shells

A restricted shell is a type of shell that limits the user's ability to execute commands. In a restricted shell, the user is only allowed to execute a specific set of commands or only allowed to execute commands in specific directories.

Restricted shells are often used to provide a safe environment for users who may accidentally or intentionally damage the system or provide a way for users to access only certain system features. Some common examples of restricted shells include the **rbash** shell in Linux and the "Restricted-access Shell" in Windows.

### RBASH

[Restricted Bourne Shell](https://www.gnu.org/software/bash/manual/html_node/The-Restricted-Shell.html) (**rbash**) is a restricted version of the Bourne shell, a standard command-line interpreter

### RKSH

[Restricted Korn Shell](https://www.ibm.com/docs/en/aix/7.2?topic=r-rksh-command) (**rksh**) is a restricted version of the Korn shell, another standard command-line interpreter. The **rksh** shell limits the user's abaility to use certain features of the Korn shell, such as executing commands in other directories, creating or modifying shell functions, and modifying the shell environment.

### RZSH

[Restricted Z Shell](https://manpages.debian.org/experimental/zsh/rzsh.1.en.html) (**rzsh**) is a restricted version of the Z shell and is the most powerful and flexible command-line interpreter. The **rzsh** shell limits the user's ability to use certain features of the Z shell, such as running shell scripts, defining aliases, and modifying the shell environment.

Admins often use restricted shells in enterprise networks to provide a safe and controlled environment for users who may accidentally or intentionally damage the system. By limiting the user's ability to execute specific commands or access certain directories, administrators can ensure that users cannot perform actions that could harm the system or compromise the network's security. Additionally, restricted shells can give users access to only certain features, allowing admins to control which resources and functions are available to each user.

Imagine a company with a network of Linux servers hosting critical businesss applications and services. Many users, including employees, contractors, and external partners, access the network. To protect the security and integrity of the network, the organiztaion's IT team decided to implement restricted shells for all users.

To do this, IT staff set up several **rbash**,**rksh**, and **zsh** shells on the network and assigns each user to a specific shell. For example, external partnets who need to access only certain network features, such as e-mail and file sharing, are assigned **rbash** shells, which limits their ability to execute specific commands and access certain directories. Contractors who need to access more advanced network features, such as database servers and web servers, are assigned to **rksh**  shells, which provide them with more flexibilty but still limit their abilities.



## Escaping

##  Command Injection

Imagine that we are in a restricted shell that allows us to execute commands by passing them as arguments to the `ls` command. Unfortunately, the shell only allows us to execute the **ls** command with a specific set of arguments, such as `ls -l` or `ls -a`, but it does not allow us to execute any other commands. In this situation, we can use command injection to escape from the shell injecting additional commands into the argument of the **ls** command.



---

↩️: [Home](../../index.md)
