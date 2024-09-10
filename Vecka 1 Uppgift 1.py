import math

# print title
print('Hot Dog Planner')
print('--------------------')

# collect info
print('How many students want:')
two_regular_hotdogs = int(input('Two ordinary hotdogs? '))
three_regular_hotdogs = int(input('Three regular hotdogs? '))
two_vegan_hotdogs = int(input('Two vegan hotdogs? '))
three_vegan_hotdogs = int(input('Three vegan hotdogs? '))

# calculate prices
quantity_regular_hotdogpacks = math.ceil((two_regular_hotdogs * 2 + three_regular_hotdogs * 3)/8)
quantity_vegan_hotdogpacks = math.ceil((two_vegan_hotdogs * 2 + three_vegan_hotdogs * 3)/4)
price_regular_hotdogs = round(quantity_regular_hotdogpacks * 20.95, 2)
price_vegan_hotdogs = round(quantity_vegan_hotdogpacks * 34.95, 2)
quantity_drinks = two_regular_hotdogs + three_regular_hotdogs + two_vegan_hotdogs + three_vegan_hotdogs
price_drinks = round(quantity_drinks * 13.95, 2)
total_cost = round(price_regular_hotdogs + price_vegan_hotdogs + price_drinks, 2)

# print results
print('---------------------')
print(quantity_regular_hotdogpacks,'packs of regular hotdogs cost', price_regular_hotdogs,'kr')
print(quantity_vegan_hotdogpacks, 'packs of vegan hotdogs cost', price_vegan_hotdogs,'kr')
print(int(quantity_drinks), 'drink/drinks cost', price_drinks,'kr')
print('---------------------')
print('Total cost is:', total_cost,'kr')