xujiajie = {'first_name' : 'xu', 'last_name': 'jiajie', 'age': '22', 'city': 'baotou'}
yangxueyun = {'first_name': 'yang', 'last_name': 'xueyun', 'age': '22', 'city': 'eerduosi'}
zhangchenyang = {'first_name': 'zhang', 'last_name': 'chenyang', 'age': '23', 'city': 'beijing'}
peoples = [xujiajie, yangxueyun, zhangchenyang]
for people in peoples:
    print(people)
    for key, value in people.items():
        print('the '+key+" : "+str(value))
    print("\n")
