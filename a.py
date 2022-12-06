import os

s = ''
for a in os.listdir('./'):
    print(
        a)
    s += a

print(s)