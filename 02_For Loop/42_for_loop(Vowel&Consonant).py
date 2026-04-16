#Question-->WAP TO COUNT VOWELS AND CONSONANTS IN A STRING

#PROGRAM-->
st=input("Enter a character:")
v=0
c=0
for char in st:
    if char in 'AEIOUaeiou':
        v=v+1
    else:
        c=c+1
print("vowels:",v)
print("consonants:",c)
