def make_great(magicians):
    current_magician = []
    for magician in magicians:
        magician = 'The Great ' + magician.title()
        current_magician.append(magician)
    return current_magician


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['you', 'me', 'him']
show_magicians(make_great(magicians[:]))
print(magicians)
