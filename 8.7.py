def make_album(singer, name, number=' '):
    if number == ' ':
        sing = {'singer': singer, 'name': name}
    else:
        sing = {'singer': singer, 'name': name, 'number': number}
    return sing


sing = make_album('xusong', 'sugelameiyoudi')
print(sing)
sing = make_album('zhoujielun', 'mojiezuo', number='10')
print(sing)
