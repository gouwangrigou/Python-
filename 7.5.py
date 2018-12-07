while True:
    age = input("age:\n")
    if age == 'quit':
        break
    else:
        age = int(age)
        if age <= 3:
            print("free")
        elif age <= 12:
            print("10 dollars")
        else:
            print("15 dollars")
