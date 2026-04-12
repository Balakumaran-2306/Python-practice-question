#QUESTION-->WAP TO PRINT SQUARE OF ALL EVEN INTEGER NUMBER IN A GIVEN HETROGENEOUS LIST

#ALGORITHM-->
STEP-1:Fetch the item from user given list.
STEP-2:To check the item is integer or not
STEP-3:If it is integer check whether it is even or odd.
STEP-4:If it is even square the number else ignore it.

#PROGRAM-->
Li=eval(input("Enter the list:"))
for items in li:
  if type(items)==int:
    if items%2==0:
      print(items**2)
