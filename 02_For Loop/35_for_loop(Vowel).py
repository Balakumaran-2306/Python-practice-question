#QUESTION-->WAP TO PRINT VOWEL CHARACTERS FROM THE STRING

#ALGORITH-->
STEP-1:Fetch the character from the string.
STEP-2:And check whether the character is present in vowels.
STEP-2:if it is print the characters

#Program-->
st=input("Enter a string:")
for char in st:
  if char in 'AEIOUaeiou':
    print(char)
