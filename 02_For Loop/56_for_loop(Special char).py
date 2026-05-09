#QUESTION-->WAP TO EXTRACT SPECIAL CHARACTER FROM THE GIVEN STRING.

#PROGRAM-->
st=input("Enter a string:")
out=''
for char in st:
    if not('A'<=char<='Z' or 'a'<=char<='z' or '0'<=char<='9'):
        out=out+char
print(out)
