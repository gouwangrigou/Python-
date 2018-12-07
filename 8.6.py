def city_country(citys, countrys):
    city_country_class = citys.title() + ', ' + countrys.title()
    return city_country_class


city_countrys = city_country('beijing', 'china')
print(city_countrys)
city_countrys = city_country('chongqing', 'china')
print(city_countrys)
city_countrys = city_country('kuala lamper', 'malaysia')
print(city_countrys)
