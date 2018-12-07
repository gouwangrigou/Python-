promot = "\nPlease enter the name of a city you have visited:"
promot += "\n(Enter 'quit' when you are finished)"

while True:
    city = input(promot+"\n")
    if city == 'quit':
        break
    else:
        print("I'd like to go to "+city.title()+"!")
