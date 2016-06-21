number = int(raw_input("Enter a number: "))
check = int(raw_input("Enter a check: "))

if number % 4 == 0:
    print str(number) + " is a multiple of four."
elif number % 2 == 0:
    print str(number) + " is an even number."
else:
    print str(number) + " is an odd number."

if number % check == 0:
    print str(number) + " divides evenly by, " + str(check)
else:
    print str(number) + " doesn't divide evenly by, " + str(check)