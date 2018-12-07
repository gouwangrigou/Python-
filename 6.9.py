favorite_places = {
    'xu': ['baotou', 'xian', 'lanzhou'],
    'yang': ['eerduosi', 'guangzhou', 'chongqing'],
    'zhang': ['beijing', 'datong']
}
for name, places in favorite_places.items():
    print(name.title()+" :")
    for place in places:
        print(place.title())
    print("\n")
message = input("press enter continue")
