def make_album(singer, name, number=' '):
    if number == ' ':
        sing = {'singer': singer, 'name': name}
    else:
        sing = {'singer': singer, 'name': name, 'number': number}
    return sing


while True:
    singer = input("Please input singer: ")
    if singer == 'q':
        break
    name = input("Please input name: ")
    if name == 'q':
        break
    number = input("Please input number(don't konow input ' ')")
    if number == 'q':
        break
    sing = make_album(singer=singer, name= name, number=number)
    print(sing)

