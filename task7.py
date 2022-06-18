'''

user input a number positive number odd number perform addition with an integer constant
even number perform multiplication with an floating point constant

negative number odd number perform subtraction with an integer constant
even number perform division with an floating point constant

'''

no = float(input("Enter the Number : "))

if no > 0:

    print("{} is Positive Number".format(no))

    if no % 2 == 0:

        print("{} Even Number".format(no))

        c = 3.21
        ans = no * c

        print("Answer is : ",ans)

    else:

        print("{} Odd number".format(no))

        c = 5
        ans = no + c

        print("Answer is : ", ans)

elif no == 0:

    print("Number is Zero")


else:

    print("{} Negative Number".format(no))

    if no % 2 == 0:

        print("{} Even Number".format(no))

        c = 3.21
        ans = no / c

        print("Answer is : ", ans)

    else:

        print("{} Odd number".format(no))

        c = 5
        ans = no - c

        print("Answer is : ", ans)