my_dict = {'Vasy': 1998, 'Pety': 2000, 'Katy': 1999, 'Masha': 2001}
print(my_dict)
my_dict['Leo'] = 1978
print(my_dict['Masha'])
print(my_dict)
del my_dict['Vasy']
print(my_dict)
my_dict.update({'Ivan': 1996,
                'Dasha': 2003})
print(my_dict)
del my_dict['Ivan']
print(my_dict)


my_set = {1, 3, 2, 'Klava', 'Ivan', 40.45, 40.45, 1, 2, 3, 1, 1, 1}
print(my_set)
my_set.add(32)
my_set.add((1, 2, 2, 3))
my_set.remove('Klava')
print(my_set)


