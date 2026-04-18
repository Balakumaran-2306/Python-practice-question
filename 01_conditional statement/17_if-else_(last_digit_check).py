#QUESTION-->WAP TO CHECK CHECK LAST DIGIT OF GIVEN NUMBER IS ODD. IF IT IS TRUE PRINT LAST DIGIT OF NUMBER ELSE PRINT NUMBER AS IT IS.

#ALGORITHM-->
STEP-1:Get the input as integer from the user.
STEP-2:Extract the last digit and check it is even or odd.
STEP-3:If it is odd print the digit. if it is even print the input digit.

#PROGRAM-->
num=int(input("Enter a number:"))
last_digit=num%10
if last_digit%2!=0:
  print(last_digit)
else:
  print(num)
