import random

def Czy_zgadles(a):

	if a == random.randint(0, 10):
		return True

	else:
		return False


x = False

while x == False:

	try:
		a = int(input("Podaj liczbe: "))

	except:
		print("Podales zla liczbe.")
		continue

	x = Czy_zgadles(a)

if x == True:

	print("Zgadłeś!")