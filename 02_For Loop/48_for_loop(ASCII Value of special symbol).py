#QUESTION-->WAP TO ADD THE ASCII VALUE OF ALL THE SPECIAL SYMBOLS IN A GIVEN INPUT STRING.

#PROGRAM-->
st=input("Enter a string:")
s=0
for char in st:
    if not('a'<=char<='z' or 'A'<=char<='Z' or '0'<=char<='9'):
        s+=ord(char)
print(s)
    
