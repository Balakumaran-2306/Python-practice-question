#QUESTION-->WAP TO PRINT ALL THE POSITIVE NUMBERS IN A LIST

#ALGORITHM-->
STEP-1:Fetch the item from the list
STEP-2:And check whether the number is greaater than 0.
STEP-3:if it is greater print positive number

#PROGRAM-->
li=eval(input("Enter the list:"))
for item in li:
  if item>0:
    print(item)
