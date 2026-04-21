# second conditional statement in python

#The "if else" conditional statement1
#variable creation and assignment and input call

number=int(input("Enter a number; "))

#conditional statement

if number>=10:
    print("number is greater than or equal to 10")
else:
   print("The number is less than 10")

#another example

age=int(input("enter your age; "))

if age>=18:
    print("You are an Adult")
elif age>=5:  #else ifconditional statement
    print("you are a child")
else:
    print("You are a baby")