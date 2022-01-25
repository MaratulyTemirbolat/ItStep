import random
def foo(bar,baz):
	array = [0]*10
	index = 0
	while index < 10:
		array[index] = random.randint(-5,5)
		index += 1
	return array
print('Сумма двух чисел =',foo(5,5))
a = 5.03
b = 8.56
print('Сумма двух переменных =', foo(a,b))

sum_a = foo(a,b)
sum_b = foo(6,4.5)

print('Сумма 4-х чисел = ',sum_a + sum_b)