import os
from cryptography.fernet import Fernet


files=[]
for file in os.listdir():
    if file == "ransom.py":
        continue
    if file == "thekey.key":
        continue
    if file == "decrypter.py":
        continue
    files.append(file)


for file in files:
    with open("thekey.key","rb") as thekey:
        key= thekey.read()
    with open(file,"rb") as thefile:
        thefiler=thefile.read()
        encrypter=Fernet(key)
        encrypted_msg=encrypter.decrypt(thefiler)
    with open(file,"wb") as thefile1:
        thefile1r=thefile1.write(encrypted_msg)
