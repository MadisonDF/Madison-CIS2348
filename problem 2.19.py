# Madison Fletcher
# 1868748
lemon_juice = int(input('Enter amount of lemon juice (in cups):\n'))
water = int(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = int(input('How many servings does this make?\n\n'))
print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar\n')
new_servings = int(input('How many servings would you like to make?\n\n'))
# Inputs the new amount of servings the user wants
print('Lemonade ingredients - yields', '{:.2f}'.format(new_servings), 'servings')
lemon_juice2 = new_servings / 3  # Gives the new number of cups of lemon juice
# for every 6 servings there is 2 cup of lemon juice (6 divided by 2 is 3)
water2 = new_servings / 0.375  # Gives the new number of cups of water
# for every 6 servings there is 16 cups of water (6 divided by 16 is 0.375)
agave_nectar2: float = new_servings / 2.4  # Give new number of cups of agave nectar
# for every 6 servings there is 2.5 cups of agave nectar (6 divided by 2.5 is 2.4)
print('{:.2f}'.format(lemon_juice2), 'cup(s) lemon juice')
print('{:.2f}'.format(water2), 'cup(s) water')
print('{:.2f}'.format(agave_nectar2), 'cup(s) agave nectar\n')
print('Lemonade ingredients - yields', '{:.2f}'.format(new_servings), 'servings')
lemon_juice3 = lemon_juice2 / 16  # Converts lemon_juice2 from cups to gallons
water3 = water2 / 16  # Converts water2 from cups to gallons
agave_nectar3: float = agave_nectar2 / 16  # Converts agave_nectar2 from cups to gallons
print('{:.2f}'.format(lemon_juice3), 'gallon(s) lemon juice')
print('{:.2f}'.format(water3), 'gallon(s) water')
print('{:.2f}'.format(agave_nectar3), 'gallon(s) agave nectar')
