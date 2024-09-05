import math

# print title
print('Hot Dog Planner')
print('--------------------')

# collect info
print('How many students want:')
två_vanliga_korvar = float(input('Two ordinary hotdogs? '))
tre_vanliga_korvar = float(input('Three regular hotdogs? '))
två_veganska_korvar = float(input('Two vegan hotdogs? '))
tre_veganska_korvar = float(input('Three vegan hotdogs? '))

# calculate prices
antal_vanliga_korvpaket = math.ceil((två_vanliga_korvar * 2 + tre_vanliga_korvar * 3)/8)
antal_veganska_korvpaket = math.ceil((två_veganska_korvar * 2 + tre_veganska_korvar * 3)/4)
pris_vanliga_korvar = antal_vanliga_korvpaket * 20.95
pris_veganska_korvar = antal_veganska_korvpaket * 34.95
antal_drickor = två_vanliga_korvar + tre_vanliga_korvar + två_veganska_korvar + tre_veganska_korvar
pris_drickor = antal_drickor * 13.95
total_kostnad = pris_vanliga_korvar + pris_veganska_korvar + pris_drickor

# print results
print('---------------------')
print(antal_vanliga_korvpaket,'packs of regular hotdogs cost', pris_vanliga_korvar,'kr')
print(antal_veganska_korvpaket, 'packs of vegan hotdogs cost', pris_veganska_korvar,'kr')
print(int(antal_drickor), 'drink/drinks cost', pris_drickor,'kr')
print('---------------------')
print('Total cost is:', total_kostnad,'kr')