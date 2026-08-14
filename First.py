num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose (+, -, *, /): ")

if operation == "+":
    print("Answer:", num1 + num2)

elif operation == "-":
    print("Answer:", num1 - num2)

elif operation == "*":
    print("Answer:", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Answer:", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operation")
# Enter first number: 20
# Enter second number: 5
# Choose (+, -, *, /): /
# Answer: 4.0
# Enter first number: 20
# Enter second number: 0
# Choose (+, -, *, /): /
# Cannot divide by zero