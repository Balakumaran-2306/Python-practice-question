#QUESTION-->WAP TO FIND SUM OF EVEN INTEGER NUMBER AND PRODUCT OF ODD INTEGER IN GIVEN HETROGENEOUS LIST.


#PROGRAM-->
li=eval(input("Enter the hetrogeneous list:")
sum=0
product=1
for item in li:
  if type(item)==int:
    if item%2==0:
      sum=sum+item
    else:
      product=product*item
print("Sum of even integer is:",sum)
print("Product of odd integer is:",product)

