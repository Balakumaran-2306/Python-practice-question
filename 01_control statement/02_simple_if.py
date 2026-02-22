# QUESTION-->WAP TO PRINT REVERSED STRING IF FIRST CHARACTER AND LAST CHARACTER IN THE STRING ARE DIFFERENT

#ALGORITHM-->
#step1:Get the input as string from user.
#step2:Use simple if statement and compare the first and last character.
#step3:if both are different print the reversed string.

#PROGRAM-->
st=input("Enter string:")
if st[0]!=st[-1]:
  print(st[::-1])

