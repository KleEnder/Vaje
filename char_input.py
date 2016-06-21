from datetime import date
name = raw_input("Enter your name: ")
age = raw_input("Enter your age: ")

ages = date.today().year - int(age) + 100

print "Your name is " + name + '\n'
print "Your age is " + age + '\n'
print "You will be 100 years old in " + str(ages)
