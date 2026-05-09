#QUESTION-->WAP TO EXTRACT VOWEL AND CONCONENT CHARACTERS FROM THE GIVEN STRING.
#PROGRAM-->
st=input("Enter a character:")
out=''
con=''
for char in st:
    if 'A'<=char<='Z' or 'a'<=char<='z' or '0'<=char<='9':
        if char in 'AEIOUaeiou':
            out+=char
        else:
            con+=char
print("Vowels:",out)
print("consonants:",con)
        
    
        
