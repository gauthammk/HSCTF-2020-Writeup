# AP Lab: English Language

Points : 100

## Solution

We can deduce the following:

1. The input should be 23 characters long.
2. The output should be "1dd3|y_3tttb5g`q]^dhn3j".

We see that we have to find a new transpose array to get back the original characters. We can do that with the help of this simple python script.

```python
inp = "abcdefghijklmnopqrstuvw"

# out is the transpose of inp
out = 'lsptirfcmgvawhnoequbdkj'
new_transpose = []
for i in range(23):
    new_transpose.append(out.index(inp[i]))
print(new_transpose)

```

Substituting this new transpose array we can reverse the transpose method. As for the xor method, I just stumbled upon the fact that we could xor the ouput to get the input without making any other changes and hence reverse the xor method too. Code in Reverse.java

Flag : `flag{n0t_t00_b4d_r1ght}`
