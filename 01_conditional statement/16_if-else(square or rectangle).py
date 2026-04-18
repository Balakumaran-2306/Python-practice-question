#QUESTION-->WAP TO CHECK WHETHER GIVEN 4 VALUES REPRESENT PERFECTLY EITHER SQUARE OR RECTANGLE OR NOT. ELSE PRINT INVALID SHAAPE ANGLE

#ALGORITHM-->
STEP-1:Get the 4 input values from the user as integer.
STEP-2:And check whether the value is greater than 0. If it is lesser print invalid angle.
STEP-3:If all the values are equal print it as square else opposite sides are equal print as rectangle.

#PROGRAM-->
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))
d=int(input("Enter number 4:"))
if a<=0 or b<=0 or c<=0 or d<=0:
    print("Invalid Number")
elif a==b and b==c and c==d:
    print("Square")
elif a==c and b==d:
    print("Rectangle")
else:
    print("Invalid Angle")
      
