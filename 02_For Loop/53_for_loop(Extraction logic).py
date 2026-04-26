#WAP TO EXTRACT ALPHABET, DIGIT, AND NUMBER CHARACTER FROM THE GIVEN STRING

#PROGRAM-->
st=input("Enter a string:")
Alpha=''
Digit=''
Spec=''
for char in st:
  if 'A'<=char<='Z':
    Alpha+=1
  elif '0'<=Digit<='9':
    Digit+=1
  else:
    Spec+=1
print("Alphabet:",Alpha)
print("Digits:",Digit)
print("Special characters:",Spec)
