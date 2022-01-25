print('Здравсвтуйте! Добро пожаловать в программу, которая принимает ',end = '')
print('время в минутах, прошедшего времени и определяет какая программа идет.')
minute_passed = int(input('Пожалуйста, напечатайте количество прошедшего времени в минутах: '))
MINUTES_PER_HOUR = 60
ZERO = 0
if(minute_passed > MINUTES_PER_HOUR and minute_passed % MINUTES_PER_HOUR != ZERO):
	minute_passed %= MINUTES_PER_HOUR
elif(minute_passed > MINUTES_PER_HOUR and minute_passed % MINUTES_PER_HOUR == ZERO):
	minute_passed = MINUTES_PER_HOUR
NEWS_DURATION = 5
ADVERTISMENT_DURATION = 5
SHOW_PROGRAMM_DURATION = 20
MUSIC_BLOCK_DURATION = 20
news_advertisment_show_duration = NEWS_DURATION + ADVERTISMENT_DURATION + SHOW_PROGRAMM_DURATION
news_advertisment_show_advertisment_dur = news_advertisment_show_duration + ADVERTISMENT_DURATION
if(minute_passed<=NEWS_DURATION):
	print('Сейчас идут новости.')
elif((minute_passed > NEWS_DURATION and minute_passed <= NEWS_DURATION + ADVERTISMENT_DURATION) or
 (minute_passed > news_advertisment_show_duration and minute_passed <= news_advertisment_show_advertisment_dur) or
 (minute_passed > news_advertisment_show_advertisment_dur  + MUSIC_BLOCK_DURATION and 
 	minute_passed <= news_advertisment_show_advertisment_dur  + MUSIC_BLOCK_DURATION + ADVERTISMENT_DURATION)):
	print('Сейчас идет реклама.')
elif(minute_passed > NEWS_DURATION + ADVERTISMENT_DURATION and minute_passed <= news_advertisment_show_duration):
	print('Сейчас идет шоу-программа.')
else:
	print('Сейчас идет Музыкальный Блок.')
print('Спасибо за использование! До свидания!')
