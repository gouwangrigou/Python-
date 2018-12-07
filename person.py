def build_person(firest_name, last_name):
    """返回一个字典，包含一个人的信息"""
    person = {'first': firest_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
