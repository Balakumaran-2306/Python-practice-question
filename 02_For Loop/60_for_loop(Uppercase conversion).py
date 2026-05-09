#QUESTION-->WAP TO CONVERT STRING TO UPPERCASE


#PROGRAM-->
st=input('Enter a string:')
out=''
for char in st:
    if 'a'<=char<='z':
        out=out+chr(ord(char)-32)
    else:
        out+=char
print("UPPERCASE:",out)
