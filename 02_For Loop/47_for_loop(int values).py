#QUESTION-->WAP TO ADD ALL THE INTEGER VALUES IN A GIVEN LIST AND PRINT FINAL RESULT. 
THEN CHECK WHETHER THE TOTAL VALUE LIES BETWEEN 65 TO 90 OR NOT IF IT IS TRUE PRINT REPECTIVE CHARACTER ELSE IGNORE

#PROGRAM-->
li=eval(input("Enter the list:"))
s=0
for items in li:
    if type(items)==int:
        s+=items
print(s)
if 65<=s<=90:
    print(chr(s))
else:
    print("IGNORE")
