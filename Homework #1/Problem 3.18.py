# Madison Fletcher
# 1868748
import math

height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))
area = height * width
print('Wall area:', area, 'square feet')
paint_gallon = 350
paint_needed = area / paint_gallon
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')
cans_needed = math.ceil(paint_needed)
print('Cans needed:', cans_needed,'can(s)\n')
can_color = str(input('Choose a color to paint the wall:\n'))
paint_cost = {'red':'$35', 'blue': '$75', 'green': '$23'}
print('Cost of purchasing', can_color, 'paint:',paint_cost[can_color])
