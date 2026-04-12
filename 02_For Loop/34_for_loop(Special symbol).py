#QUESTION-->WAP TO PRINT ALL THE SPECIAL SYMBOLS FROM THE STRING

#ALGORITHM-->
STEP-1:Fetch the character from the string.
STEP-2:And check whether the character is uppercase. lowercase or numbers.
STEP-3:If it is not print the special character.

#PROGRAM-->
st=input("Enter a string:")
for char in st:
  if not('A'<=char<='Z' or 'a'<=char<='z' or '0'<=char<='9'):
      print(char)
