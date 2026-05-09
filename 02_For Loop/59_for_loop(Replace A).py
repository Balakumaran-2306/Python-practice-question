#QUESTION-->WAP TO REPLACE ALL OCCURRENCES OF 'A' WITH '$' IN A STRING.


#PROGRAM-->
st=input('Enter a string:')
out=''
for char in st:
    if char=='A':
        out+='$'
    else:
        out+=char
print(out)
