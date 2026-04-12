#QUESTION-->WAP TO PRINT ASCII VALUE OF ALL CHARACTER IN A STRING

#ALGORITHM-->
STEP-1:Get the input as string from the user.
STEP-2:Fetch the character and print the ascii value for it

#PROGRAM-->
st=input("Enter a string:")
for char in st:
  print(ord(char))
