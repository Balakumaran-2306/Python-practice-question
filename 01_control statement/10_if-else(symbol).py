#QUESTION-->WAP TO CHECK THE GIVEN CHARACTER IS SPECIAL SYMBOL OR NOT

#ALGORITHM-->
#step1:Get the input character from the user.
#step2:check the character in three conditions using operators(>< , or)(upper and lower case alphabet)
#step3:Else print as special symbol.

PROGRAM-->
ch=input("Enter a character:")
if('a'<=ch<='z') or ('A'<=ch<='Z') or ('0'<=ch<='9'):
  print("Not a special symbol")
else:
  print("Special Symbol")
