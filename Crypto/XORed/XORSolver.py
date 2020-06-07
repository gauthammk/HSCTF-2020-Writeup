def hexxor(a, b):
    return hex(int(a, 16) ^ int(b, 16))[2:]


# Key3 = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(Key1, s1))
Key1 = '5dcec311ab1a88ff66b69ef46d4aba1aee814fe00a4342055c146533'
s1 = '9a13ea39f27a12000e083a860f1bd26e4a126e68965cc48bee3fa11b'
Key3 = hexxor(Key1, s1)
print(Key3)
s2 = '996e59a867c171397fc8342b5f9a61d90bda51403ff6326303cb865a'
Key4 = hexxor(Key3, s2)
print(Key4)
Key1XORKey4 = hexxor(Key1, Key4)
print(Key1XORKey4)
s3 = '7b33428eb14e4b54f2f4a3acaeab1c2733e4ab6bebc68436177128eb'
Key5 = hexxor(Key1XORKey4, s3)
print(Key5)
Key3XORKey5 = hexxor(Key3, Key5)
print(Key3XORKey5)
s4 = '557ce6335808f3b812ce31c7230ddea9fb32bbaeaf8f0d4a540b4f05'
Key2 = hexxor(Key3XORKey5, s4)
print(Key2)
s5 = '306d34c5b6dda0f53c7a0f5a2ce4596cfea5ecb676169dd7d5931139'
AllKeyXOR = hexxor(Key2, hexxor(Key1XORKey4, Key3XORKey5))
print(AllKeyXOR)
Flag = hexxor(AllKeyXOR, s5)
print('Flag : ', bytes.fromhex(Flag).decode('ASCII'))
