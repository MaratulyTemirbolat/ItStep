print('\t\t\t\t\t\t\t\tHello! Welcome to the system.\n It takes the circle radius',end = ' ')
print('including the square\'s side, calculates their areas respectively', end = ' ')
print('and estimates those quantities in order to show which one is bigger.')

circle_radius = float(input('Please, type the radius of your circle: '))
square_side = float(input('Please, type the legth of your square\'s side: '))

PI = 3.14

circle_area = PI*(circle_radius**2) 
square_area = square_side*square_side

print('Calculations are over...')
print('The area of the CIRCLE is {} and SQUARE is {} respectively.'.format(circle_area,square_area))
if(circle_area > square_area):
	print('Oh. After some simple math procedures we obtain', end = ' ')
	print('that the area of the circle is higher than square\'s one.')
elif(circle_area == square_area):
	print('Well. The areas of the circle and square are exactly the same!')
else:
	print('Wow, the area of your circle is less than square\'s area.')
print('That\'s all. Thank you for usage. Good Buy!')