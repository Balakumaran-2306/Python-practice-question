#QUESTION-->WAP TO DISPLAY "HELLO" IF A NUMBER ENTERED BY USER IS MULTIPLE OF 5 OTHERWISE PRINT "BYE"

#ALGORITHM-->
#step1:Get the input as integer from the user.
#step2:check if the number is multiple of 5 if condition satisfies print "HELLO"
#step3:Else print "BYE".


PROGRAM-->
num=int(input("Enter a number:"))
if num%5==0:
  print("HELLO")
else:
  print("BYE")
