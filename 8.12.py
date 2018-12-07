def make_sandwish(items):
    sandwish = []
    for item in items:
        sandwish.append(item)
        print(item)
    return sandwish


my_sandwish = ['rou', 'dan', 'nai']
my_sandwish = make_sandwish(my_sandwish)
print(my_sandwish)
