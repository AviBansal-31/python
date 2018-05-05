Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list_one = [1,2,3]
>>> list_two = [1,2,3]
>>> if cmp(list_one,list_two) == 0:
	print "these two lists are equal"
else:
	print "these two strings are not egual"

	
these two lists are equal
>>> list_one = ['hi','how', 'are', 'you?']
>>> list_two = ['Hi,','how', 'are', 'you?']
>>> if cmp(list_one,list_two) == 0:
	print "these two lists are equal"
else:
	print "these two strings are not egual"

	
these two strings are not egual
>>> list_one = [1,3,'coding']
>>> list_two = [[1,3,'coding']]
>>> if cmp(list_one,list_two) == 0:
	print "these two lists are equal"
else:
	print "these two strings are not egual"

	
these two strings are not egual
>>> def cmp_lists(list_one, list_two:
	      
SyntaxError: invalid syntax
>>> def cmp_lists(list_one,list_two):
	if list_one == list_two:
		print "these two strings are identical"
	else:
		print "these two strings are different"
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
SyntaxError: invalid syntax
>>> def cmp_lists(list_one,list_two):
	if list_one == list_two:
		print "these two strings are identical"
	else:
		print "these two strings are different"
list_one = [1,2,5,6,2]
SyntaxError: invalid syntax
>>> def cmp_lists(list_one,list_two):
	if list_one == list_two:
		print "these two strings are identical"
	else:
		print "these two strings are different"

		
>>> list_one = [1,2,5,6,2]
>>> list_two = [1,2,5,6,2]
>>> cmp_lists(list_one, list_two)
these two strings are identical
>>> list_one = [1,2,5,6,5]
>>> list_two = [1,2,5,6,5,3]
>>> cmp_lists(list_one, list_two)
these two strings are different
>>> list_one = [1,2,5,6,5,16]
>>> list_two = [1,2,5,6,5]
>>> cmp_lists(list_one, list_two)
these two strings are different
>>> list_one = ['celery','carrots','bread','milk']
>>> list_two = ['celery','carrots','bread','cream']
>>> cmp_lists(list_one,list_two)
these two strings are different
>>> 
