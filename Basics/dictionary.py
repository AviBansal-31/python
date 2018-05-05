Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_dict={
	'name': 'Anagha',
	'age': 25,
	'birth_P': 'India',
	'fav_lang': 'Python'
}
>>> def me():
	print """
	My name is %s
	My age is %s
	My country of birth is %s
	My favorite language is %s
	""" % (my_dict['name'], my_dict['age'], my_dict['birth_P'], my_dict['fav_lang'])

	
>>> me()

	My name is Anagha
	My age is 25
	My country of birth is India
	My favorite language is Python
	
>>> 
