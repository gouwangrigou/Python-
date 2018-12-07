vacantion_places = {}
while True:
    names = input("your name: ")
    places = input("Place:")
    vacantion_places[names] = places
    control = input("do you want to continue?")
    if control == 'no':
        break
for name, place in vacantion_places.items():
    print("\n" + name+" want to go to "+place)
