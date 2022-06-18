''' user input a character
a->"you have enter a"
b->"you have enter b"
c->"you have enter c"
->Invalid character
'''
char = input("Enter Char between A to C : ")

if char == 'a' or char == 'A':

    print("You have enter a...!!")

elif char == 'b' or char == 'B':

    print("You have enter b...!!")

elif char == 'c' or char == 'C':

    print("You have enter c...!!")

else:
    print("Invaild character Entered...!!!")
