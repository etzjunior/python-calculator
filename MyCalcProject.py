def calculate(num1, num2, Choice):
    valid_choices = ['+', '-', '*', '/']
    if Choice not in valid_choices:
        return "Invalid Input"
    
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

calculator_active = True
continuing = False

while calculator_active:
    if continuing:
        num1 = Current_result
        continuing = False
    else:
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
    
    result = calculate(num1, num2, Choice)
    print(result)
     
    Current_result = result
    print("Do you wanna continue calculating?")
    Choice2 = input("input y/n: ")

    if Choice2 == "y":
        continuing = True

        
