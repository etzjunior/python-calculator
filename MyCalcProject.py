num1 = float(input("Enter number: "))

print("Select Operations:")
print("+. Add")
print("-. Subract")
print("/. Divide")
print("*. Multiply")

Choice = input("Enter Your Choice: ")

num2 = float(input("Enter another number: "))

print("First number: ", num1)
print("Second number:", num2)

def calculate(num1, num2, Choice):
    if Choice == '+':
        return num1 + num2
    elif Choice == '-':
        return num1 - num2
    elif Choice == '/':
        if num2 == 0:
            return "Error: Cannot divide by 0"
        return num1 / num2
    elif Choice == '*':
        return num1 * num2
    else:
        return "Invalid input"
    
result = calculate(num1, num2, Choice)
print(result)