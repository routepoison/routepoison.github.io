# Python

## reviewing scripts

A review of the following simple code block that prints or echos your 'ifconfig' settings.

```python
import subprocess

subprocess.run(
	["ifconfig", "eth0"],
	shell=True,
)
```

This function requires a  list of commands. The other parameter, __shell=true__, means that we want to see the output printed to the console.

---
