from random import *

print('Здравствуйте! Добро пожаловать в программу, которая заполняет ',end = "")
print('список расстояниями, которые путешественник проделал ',end = "")
print('за каждый определенный день в течении 5 недель.')
print('Предельное расстояние у путешественника за 1 день может быть 35 км.')

MAX_DISTANCE = 35

traveler_distances = [12.0]

LAST_DAY_TRAVEL = 35

current_day_travel = 1

TEN_PERCENT = 1.1

INDEX_STEP = 1

print('\nНа 1-й день путешествия было проделано',traveler_distances[0],end = " ")
print('км.')
while(current_day_travel < LAST_DAY_TRAVEL):
	new_day_distance = (traveler_distances[current_day_travel - INDEX_STEP]*TEN_PERCENT)
	if(new_day_distance <= MAX_DISTANCE): 
		traveler_distances.append(new_day_distance)
	else:
		traveler_distances.append(MAX_DISTANCE)
	print('На {}-й день путешествия было проделано {} км.'.format(current_day_travel + INDEX_STEP,traveler_distances[current_day_travel]))
	current_day_travel += INDEX_STEP
print('\nСпасибо за использование программы! До свидания!')
