# My First Calculator

Points : 100

## Solution

Referring to this article : https://medium.com/swlh/hacking-python-applications-5d4cd541b3f1, I understood that the input(), eval() and exec() methods in python2 were vulnerable. In the provided code, there is an input method and we can most definitely execute malicious code from here. So just adding this code in the prompt(when the code is running on the server, obviously) would give us a shell.

```python
__import__('os').system('bash -i')
```

We find a flag.txt file in the current directory and upon futher investigation, we find that it contains the flag.

Flag : `flag{please_use_python3}`
