#QUESTION-->WAP TO FIND THE TOTAL OCCURENCE OF A GIVEN CHARACTER IN A STRING

#PROGRAM-->
st=input('Enter a string:')
ch=input('Enter a character:')
c=0
for char in st:
    if ch==char:
        c+=1
print(c)

Sample output:
st='Malayalam'
ch='a'
output=4
