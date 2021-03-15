class Dog():
	species = "Canis familiaris"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	# description
	#  returns a string displaying the name and age of the dog.
	def __str__(self):
		return f'{self.name} is {self.age} years old'

	#has one parameter called sound and returns a string containing the dog’s name and the sound the dog makes.	
	def sound(self, sound):
		return f'{self.name} barks: {sound}'

class Jack(Dog):
	
	#Method overriding
	def sound(self, sound="Arrf"):
		return super().sound(sound)

	# When you call super().speak(sound) inside JackRussellTerrier, 
	# Python searches the parent class, Dog, for a .speak() method and calls it with the variable sound.

class Dack(Dog):
	pass

class BullDog(Dog):
	pass

buddy = Dack("Buddy", 9)
miles = Jack("Miles", 4)

print(buddy.name)
print(buddy.sound("Woof"))
print(miles.sound())

# Methods => __init__ and __str__ are dundler methods becuase they begin and end with underscore
# isinstance() => checks if child is an instance of the parent class