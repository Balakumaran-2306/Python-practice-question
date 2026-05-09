#QUESTION-->WAP TO CHECK THE GIVEN STRING IS PALINDROME OR NOT.

#PROGRAM-->
st=input("Enter a string:")
out=''
for char in st:
  out=char+out
if st==out:
  print("Palindrome")
else:
  print("Not a Palindrome")
