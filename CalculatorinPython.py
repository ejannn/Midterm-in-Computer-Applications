num1 = int(input("Enter your first number:  "))
num2 = int(input("Enter your second number:  "))

sum = num1 + num2
difference = num1 - num2
if num2 != 0:
    quotient = num1 / num2
else:
    print("Error: Division by zero is not allowed.")
    quotient = None
product = num1 * num2


print("\nThe sum of", num1, "and", num2, "is:", sum)
print("The difference between", num1, "and", num2, "is:", difference)
if quotient is not None:
    print("The quotient of", num1, "and", num2, "is:", quotient)
print("The product of", num1, "and", num2, "is:", product)
