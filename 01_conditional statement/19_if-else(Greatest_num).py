#QUESTION-->WAP TO FIND GREATEST NUMBER AMONG FOUR NUMBERS

#PROGRAM-->
Num1=int(input("Enter number 1:"))
Num2=int(input("Enter number 2:"))
Num3=int(input("Enter number 3:"))
Num4=int(input("Enter number 4:"))
if Num1>Num2 and Num1>Num3 and Num1>Num4:
  print("Num1 is greater")
elif Num2>Num3 and Num2>Num4:
  print("Num2 is greater")
elif Num3>Num4:
  print("Num3 is greater")
else:
  print("Num4 is greater")
