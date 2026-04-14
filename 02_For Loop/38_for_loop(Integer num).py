#QUESTION-->WAP TO PRINT ONLY INTEGER NUMBER FROM THE  HETROGENEOUS LIST WHERE THE NUMBER SHOULD BE GREATER THAN 45.

#ALGORITHM-->
STEP-1:Fetch the item from the hetrogeneous list.
STEP-2:And check whether the item is integer or not.
STEP-3:If it is integer check whether the number is greater than or equal to 45.
  
#PROGRAM-->
li=eval(input("Enter the hetrogeneous list:"))
for num in li:
  if type(num)==int:
    if num>=45:
      print(num)
