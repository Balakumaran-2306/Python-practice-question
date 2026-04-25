#QUESTION-->WAP TO COUNT POSITIVE AND NEGATIVE NUMBERS IN A HETEROGENOUS LIST.

#PROGRAM-->
li=eval(input("Enter hetrogeneous list:"))
p=0
n=0
for item in li:
  if type(item)==int:
    if item>=0:
      p+=1
    else:
      n+=1
print("positive:",p)
print("negative:",n)
