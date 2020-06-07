inp = "abcdefghijklmnopqrstuvw"
out = 'lsptirfcmgvawhnoequbdkj'
new_transpose = []
for i in range(23):
    new_transpose.append(out.index(inp[i]))
print(new_transpose)
