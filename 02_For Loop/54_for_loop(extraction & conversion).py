#QUESTION-->WAP TOCONVERT AND EXTRACT UPPERCASE ALPHABET TO LOWERCASE ALPHABET IF THE GIVEN CHARACATER IS UPPERCASE ALPHABET AND VICE VERSA. OR EXTRACT 0 IF CHARACTER IS NUMBER OR EXTRACT ASTERISK IF CHARACTER IS SPECIAL SYMBOL

#PROGRAM-->
st=input("Enter a string:")
out=''
for char in st:
  if 'A'<=char<='Z':
    out+=chr(ord(char)+32)
  elif 'a'<=char<='z':
    out+=chr(ord(char)-32)
  elif '0'<=char<='9':
    out+='0'
  else:
    out+='*'
print(out)
