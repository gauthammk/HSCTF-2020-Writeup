# Comments

Points : 100

## Solution

We can use the `zipdetails` command to find zip file commands in Linux. We can automate the unzipping and searching process with this script below :

```python
import os

os.system("zipdetails Comments.zip | grep Comment")
os.system("unzip Comments.zip")
for i in range(1, 9):
    os.system("zipdetails " + str(i) + ".zip | grep Comment")
    os.system("unzip " + str(i) + ".zip")

```

Flag : `flag{4n6}`
