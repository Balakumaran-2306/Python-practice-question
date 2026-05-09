#QUESTION-->WAP TO TOGGLE CHARACTERS CASE IN A STRING.

#PROGRAM-->
st=input("Enter a string:")
u=''
for char in st:
        if 'A'<=char<='Z':
            u+=chr(ord(char)+32)
        elif 'a'<=char<='z':
            u+=chr(ord(char)-32)
        else:
            u+=char
print(u)

        
