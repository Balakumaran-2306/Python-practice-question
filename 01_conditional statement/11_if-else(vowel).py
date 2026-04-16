#QUESTION-->WAP TO CHECK GIVEN CHARACTER IS VOWEL OR CONSONANT

#ALGORITHM-->
STEP-1:Get the input from the user as string and fetch the character.
STEP-2:And check whether the character is present in vowel characters
STEP-3:If it is not present print it is consonant.


#PROGRAM-->
ch=input("Enter a character:")
if ch in 'AEIOUaeiou':
    print("vowel")
else:
    print("consonant")
