print("Simple Calculator")
while True:
    num1 = float(input("Enter number: "))
    operator1 = input("Enter operator (+, -, *, /, ^):")
    num2 = float(input("Enter number: "))
    
    if operator1 == "+":
        result = num1 + num2 
    elif operator1 == "-":
        result = num1 - num2
    elif operator1 == "*":
        result = num1*num2 
    elif operator1 == "/":
        result = num1/num2
    elif operator1 == "^":
        result = num1**num2

    more = input("Do you want to add more?(y/n):")
    if more.lower() == "y":
        operator2 = input("Enter second operator (+, -, *, /, ^):")
        num3 = float(input("Enter number: "))
         
        if operator2 == "+":
            result = result + num3
        elif operator2 == "-":
            result = result - num3
        elif operator2 == "*":
            result = result*num3
        elif operator2 == "/":
            result = result/num3
        elif operator2 == "^":
            result = result**num3
    
    print("Result:", result)
    again = input("Do you want another calculation?(y/n):")
    if again.lower() != "y":
        break



    