#QUESTION-->WAP TO CONVERT AND PRINT THE LOWERCASE ALPHABET IF THE GIVEN CHARACTER IS UPPERCASE ALPHABET AND VICE VERSA (OR)PRINT 0 IF THE CHARACTER IS NUMBER(OR) PRINT * IF THE CHARACTER IS SPECIAL SYMBOL.

#ALGORITHM-->
STEP-1:Get the input as character from the user.
STEP-2:Check the character if it is uppercase convert into lowercase and vice versa using build-in functions.
STEP-3:If it is digit print 0 else print asterisk.

#PROGRAM-->
st=input("Enter a character:")
if 'A'<=char<='Z':
  print(chr(ord(char)+32))
elif 'a'<=char<='z':
  print(chr(ord(char)-32))
elif '0'<=char<='9':
  print(0)
else:
  print(*)
