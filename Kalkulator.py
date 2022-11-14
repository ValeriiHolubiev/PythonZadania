while True:

	try:
		a = int(input('\nPodaj pierwsza liczbe: '))
		b = int(input('\nPodaj druga liczbe: '))
	except:
		print("\nPodalesz zla liczbe.")
		continue

	y = input('\nPodaj znak: ')

	print()

	if b == 0 and y == '/':
		print("Nie mozna delic na 0!")
		continue

	if y == '+':
		print(a, "+", b, "=", a+b)

	elif y == '-':
		print(a, "-", b, "=", a-b)

	elif y == '*':
		print(a, "*", b, "=", a*b)

	elif y == '/':
		print(a, "/", b, "=", a/b)

	elif y == '%':
		print(a, "%", b, "=", a%b)

	elif y == '//':
		print(a, "//", b, "=", a//b)

	elif y == '**':
		print(a, "**", b, "=", a**b)

	else:
		print("Podalesz zly znak.")
		continue

	print()

	x = input('Kontynujemy?(y/n): ')

	if x == 'y':
		print()
		continue

	elif x == 'n':
		break
