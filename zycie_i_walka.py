import random
import os

class Character:
	hp = 100
	exp = 0
	damage = 0
	dead = False

	def __init__(self, name):

		self.name = name


	def info(self):
		print("Character name: " + self.name)
		print("HP: " + str(self.hp))
		print("Exp.: " + str(self.exp))


	def fight(self):

		self.damage = random.randint(1,100)
		print("You recieved " + str(self.damage) + " damage.")

		if self.damage >= self.hp:
			self.dead = True
			print("\nYou are dead.")

		else:
			self.hp -= self.damage
			self.exp += 100


	def heal(self):
		self.hp = 100


def clear():
	os.system("cls")

def restart():
	character.dead = False
	character.hp = 100
	character.exp = 0

clear()
character = Character(input("Enter your name:"))
clear()

while True:
	print("\nPress F to fight.")
	print("\nPress H to heal.")
	print("\nPress I to see stats.")
	print("\nPress X to exit.")
	c = input("\nWhat you choose?: ")


	if c == "F" or c == "f":
		clear()
		character.fight()

		if character.dead == True:
			c = input("\nTry again? (y/n): ")

			if c == "Y" or c == "y":
				clear()
				restart()

			if c == "N" or c == "n":
				clear()
				print("Thank you for playing. Goodbye.")
				break

	if c == "H" or c == "h":
		clear()
		character.heal()
		print("You've healed yourself.")

	if c == "I" or c == "i":
		clear()
		character.info()

	if c == "X" or c == "x":
		clear()
		c = input("Are you sure you want to exit? (y/n): ")

		if c == "Y" or c == "y":
			clear()
			print("Thank you for playing. Goodbye.")
			break

		elif c == "N" or c == "n":
			clear()
			continue

	if character.exp >= 1000:
		clear()
		print("You have recieved 1000 exp. and won this game! congratulations!")
		c = input("\nDo you want to play again? (y/n): ")

		if c == "N" or c == "n":
			clear()
			print("Thank you for playing. Goodbye.")
			break

		elif c == "Y" or c == "y":
			clear()
			restart()
			continue