class Dog:
	species = 'caniche'

	def __init__(self, name, age):
	    self.name = name
	    self.age = age

	def get_biggest_number(*age):
	    a=max(age)
	    return a

bambi = Dog("Bambi", 5)
mikey = Dog("Rufus",16)
piolin = Dog("Piolin", 8)
pingu = Dog("Pingu", 10)
doraemon = Dog("Doraemon", 12)


older = Dog.get_biggest_number(bambi.age,mikey.age,piolin.age,pingu.age,doraemon.age)
print("The oldest animal has: {}.".format(older))
print("{} is {} and {} is {} and {} is {} and {} is {} and {} is {}.".format(bambi.name, bambi.age, mikey.name, mikey.age, piolin.name, piolin.age, pingu.name, pingu.age, doraemon.name, doraemon.age))

#print(maxim(bambi.age,mikey.age))

#print (mylist[0].name)


if bambi.species == "caniche":
	print("{0} is a {1}!".format(bambi.name, bambi.species))

