#writing a calculator program in python
print("Welcome to calculator \n Here are some of the operators -,*+/ \n")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter the operator: ")

#getting stated in this case using the if statements
if operator =="+":
    print(num1 + num2)
elif operator =="*":
    print(num1 * num2)
elif operator=="/":
    print(num1 / num2)

elif operator=="-":
    print(num1 -num2)

else:
    print("invalid operator")
    


