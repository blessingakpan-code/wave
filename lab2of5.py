elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H','is_noble_gas':'false'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He','is_noble_gas':'true'}}
# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
#hint: After inserting the new entries you should be able to perform these lookups:

#>>>print(elements['hydrogen']['is_noble_gas'])
print(elements['hydrogen']['is_noble_gas'])
#<<< False
#>>> print(elements['helium']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])
#<<< True



