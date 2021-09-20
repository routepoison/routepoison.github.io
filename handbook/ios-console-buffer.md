The parser command

Have you ever performed a show running-configuration (or show run) command and waited "too many" seconds for it to appear? Frustrating, right? You can use a new version of the parser command to speed up that view time. As the parser system is a caching system, it is going to do two things: (1) keep the IOS configuration in memory and use more of your memory to do it and (2) be more effective as repetition increases and as the configuration gets larger.

How the parser config cache interface command can help
When you issue a show running-config command, it queries every interface on your router and then compiles all this information into a total configuration. Think about how many times you issue this command. This process, known as nonvolatile generation (NVGEN), polls and retrieves every component and interface and every command.

Based on the size of your router and its interfaces, that show run can take quite a while and possibly slow down your router's performance. The Configuration Generation Performance Enhancement feature cuts this process time down from minutes virtually to seconds because it retrieves only the changes that were made to the configuration file. There are a few things that you will need to be aware of though.

First, you need to be aware that extra memory will be used to do this. Second, you will need to issue the show running-config command and will only see the benefits of the parser cache the second time you issue the command.

Also, each time the configuration is changed, the interface file that you have stored in memory is flushed so you will need to process another show running-config command to cache the most current file.

How do you use the parser config cache interface command?
So, let's go through the process to see how easy it is to configure this feature.

Router# configure terminal
Router(config)# parser config cache interface
Router(config)# exit
Keep in mind that this comm

Router# show parser statistics
Last configuration file parsed:Number of Commands:1484, Time:1272 ms
Parser cache:disabled, 1440 hits, 10 missess