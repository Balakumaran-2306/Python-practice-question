#QUESTION-->WAP TO FIND THE GIVEN FLOAT NUMBER IS MORE THAN OF PI VALUEE OR NOT. IF IT IS TRUE SUBTRACT THE GIVEN NUMBER FROM THE PI. ELSE CONVERT INTO INTEGER DATATYPE VALUE

#ALGORITHM-->
#step1:Get the input as float value from the user.
#step2:Assign pi value in one variable.
#step3:If float value is greater than pi value subtract and print it.
#step4:Else convert the input value as integer and print it.

PROGRAM-->
num=float(input('Enter a float value:'))
pi=3.14
if (num>pi):
  print(num-pi)
else:
  print(int(num))
