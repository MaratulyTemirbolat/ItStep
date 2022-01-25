print('Здравсвтуйте! Эта программа подскажет может ли Вася ',end = ' ')
print('пролезть через окно, зная его длину и ширину, а также диаметр своей головы.')
length_window = float(input('Напечатайте пожалуйста длину форточки (А) в см : '))
width_window = float(input('Напечатайте пожалуйста ширину форточки (Б) в см : '))
head_diametr = float(input('Напечатайте пожалуйста диаметр головы Васи в см : '))
EMTPY_ZAZOR = 2
if(length_window >= (head_diametr + EMTPY_ZAZOR) and width_window >= (head_diametr + EMTPY_ZAZOR) ):
	print('Вася сможет пролезть в форточку')
else:
	print('Вася не сможет пролезть в форточку')
print('Спасибо за Использование! До свидания!')
