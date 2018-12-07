def get_formatted_name(first_name, last_name, middle_name=' '):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musian = get_formatted_name('jimi', 'lee', 'hendrix')
print(musian)
musian = get_formatted_name('jimi', 'hendrix')
print(musian)
