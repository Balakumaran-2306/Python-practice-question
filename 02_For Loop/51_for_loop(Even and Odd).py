#QUESTION-->WAP TO COUNT EVEN AND ODD NUMBERS IN A HOMOGENOUS LIST.

#PROGRAM-->
li=eval(input("Enter the homogeneous list:"))
eve=0
od=0
for item in li:
  if item%2==0:
    eve+=1
  else:
    od+=1
print(eve)
print(od)
    
  


