def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name)


describe_pet(pet_name='harry')
describe_pet(pet_name='harry', animal_type='cat')
