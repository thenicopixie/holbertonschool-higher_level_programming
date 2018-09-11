#!/usr/bin/python3
letters = ""
for i in range(97, 122):
    if i != 101:
        if i != 113:
            letters += chr(i)
print(letters, end="")
