Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from random import randint
>>> score = randint(60,101)
>>> if score >= 90:
	print "Score: ", score,"; Your grade is A"
elif score >= 80:
	print "Score: ", score,"; Your grade is B"
elif score >= 70:
	print "Score: ", score,"; Your grade is C"
else:
	print "Score: ", score,"; Your grade is D"

	
Score:  100 ; Your grade is A
>>> 
