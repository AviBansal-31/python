Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
>>> favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
>>> def make_dict(L1,L2):
	new_dict = zip(L1, L2)
	return new_dict

>>> make_dict(name, favorite_animal)
[('Anna', 'horse'), ('Eli', 'cat'), ('Pariece', 'spider'), ('Brendan', 'giraffe'), ('Amy', 'ticks'), ('Shane', 'dolphins'), ('Oscar', 'llamas')]
>>> 
>>> 
>>> name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
>>> favorite_animal = ["horse", "cat", "spider", "giraffe"]
>>> def make_dict(L1,L2):
	new_dict = zip(L1, L2)
	return new_dict

>>> make_dict(name, favorite_animal)
[('Anna', 'horse'), ('Eli', 'cat'), ('Pariece', 'spider'), ('Brendan', 'giraffe')]
>>> 


>>> 

>>> 
