#QUESTION-->WAP TO CHECK GIVEN NUMBER IS VALID PHONE NUMBER OR NOT

#ALGORITH-->
#step1:Get the input from the user as integer.
#step2:Check whether the entered value consist of 10 numbers.
#step3:And also check whether the number starts with 6,7,8,9.

#PROGRAM--->(without using build in functions)
num=int(input("Enter a phone number:"))
if 6000000000<=num<=9000000000:
  print("Valid phone number")
else:
  print("Invalid phone number")

#PROGRAM--->(using build in functions)
num=int(input("Enter a phone number:"))
if len(str(num)==10) and str(num)[0] in 6789:
   print("Valid phone number")
else:
   print("Invalid phone number")
