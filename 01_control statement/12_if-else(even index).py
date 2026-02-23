#QUESTION-->WAP TO PRINT EVEN INDEX ITEMS FROM THE STRING IF THE LENGTH OF THE STRING IS ODD ELSE PRINT ODD INDEX ITEMS.

#ALGORITHM-->
#step1:Get the input as string from the user.
#step2:Check the length of the string and use % operator to check whether it is divisible or not.
#step3:if it is odd print even characters and vice versa.

PROGRAM-->
str=input('Enter a string:')
if len(str)%2!=0:
    print(str[0::2])
else:
     print(str[1::2])
