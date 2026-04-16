#QUESTION-->WAP TO FIND SUM OF AALL NUMBERS IN A LIST


#PROGRAM-->
li=eval(input("Enter the list:"))
s=0
for char in li:
    if type(char)==int:
        s=s+char
print(s)
