while True:
    age = int(input("Enter your age(years):"))
    weight = float(input("Enter your weight(kg):"))
    height = float(input("Enter your height(cm):"))
    sex = (input("Enter your gender(m/f)"))
    activity = input("Enter activity on a scale of 5, where 0 equals BMR, 1 equals sedentary and 5 equals very active:")

    result = 10*weight + 6.25*height-5*age
    
    if sex == "m":
        BMR = result + 5
    elif sex == "f": 
        BMR = result - 161
    else:
        print("Invalid gender")
        continue

    if activity == "0":
            result = BMR*1
    elif activity == "1":
        result = BMR*1.2
    elif activity == "2":
        result = BMR*1.375
    elif activity == "3":
        result = BMR*1.55
    elif activity == "4":
        result = BMR*1.725
    elif activity == "5":
        result = BMR*1.9
    else:
        print("Error: wrong activity level")
        continue

    print(f"Your daily calorie intake is: {int(result)}" )
    goal = input("Do you want to lose or gain weight(l/g)? ")

    if goal == "l":
        amount = input("How much weight do you want to lose per week(0.25/0.5/0.75/1)")

        if amount == "0.25":
            result = result - 250
        elif amount == "0.5":
            result = result - 500
        elif amount == "0.75":
            result = result - 750
        elif amount == "1":
            result = result - 1000
        else:
            print("Wrong value")
    elif goal == "g":
        amount = input("How much weight do you want to gain per week(0.25/0.5/0.75/1)")

        if amount == "0.25":
            result = result + 250
        elif amount == "0.5":
            result = result + 500
        elif amount == "0.75":
            result = result + 750
        elif amount == "1":
            result = result + 1000
        else:
            print("Wrong value")
    print(f"Your daily calorie intake is: {int(result)}")


    again = input("Do you want another calculation?(y/n):")
    if again.lower() != "y":
        break
