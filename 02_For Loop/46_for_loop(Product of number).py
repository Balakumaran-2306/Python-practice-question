#QUESTION-->WAP TO FIND PRODUCT OF ALL NUMBERS IN A LIST.

#PROGRAM-->
li=eval(input("Enter the list:"))
s=1
for char in li:
    if type(char)==int:
        s=s*char
print(s)
