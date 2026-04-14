#QUESTION-->WAP TO PRINT ALL THE ODD NUMBERS FROM THE HETROGENEOUS LIST.

#ALGORITHM-->
step-1:Fetch the item from the hetrogeneous list
step-2:And check whether the item is integer or not.
step-3:If it is integer check the item is odd number or not. If odd print the number.

#PROGRAM-->
li=eval(input("Enter the hetrogeneous list:"))
for item in li:
  if type(item)==int:
    if item%2!=0:
      print(item)
