#QUESTION-->wap to count alphabets, digits and special character in a string

#PROGRAM-->
st=input("Enter a string:")
a=0
d=0
s=0
for ch in st:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        a+=1
    elif '0'<=ch<='9':
        d+=1
    else:
        s+=1
print("Alphabet count:",a)
print("Digit count:",d)
print("Special character count:",s)
