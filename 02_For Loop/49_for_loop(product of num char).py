#QUESTION-->WAP TO FIND PRODUCT OF NUMBER CHARACTERS FROM THE GIVEN STRING

#PROGRAM-->
ch=input("Enter a string:")
s=1
for char in ch:
  if '0'<=char<='9':
    s=s*char
print(s)
    
