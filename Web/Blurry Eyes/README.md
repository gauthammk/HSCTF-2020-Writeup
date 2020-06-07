# Blurry Eyes

Points : 100

Problem Statement :
I can't see :(

https://blurry-eyes.web.hsctf.com

## Solution

Exploring the source of the web page leads us to find some text blurred using css. Opening the css styles file and searching for that specific class gives us the flag with a few ' \" ' characters in between. It is then just matter extracting the flag from the mess. A simple script in python would be as follows :

```python
flag = '"f" "l" "a" "g" "{" "g" "l" "a" "s" "s" "e" "s" "_" "a" "r" "e" "_" "u" "s" "e" "f" "u" "l" "}"'

final_flag = flag.replace('"', '').replace(' ', '')
```

Flag : `flag{glasses_are_useful}`
