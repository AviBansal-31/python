Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l = ['magical unicorns', 19,'hello',98.98,'world',[1,2,3]]
>>> print [n for n in l if type(n) is str]
['magical unicorns', 'hello', 'world']
>>> print [n for n in l if type(n) is int]
[19]
>>> print [n for n in l if type(n) is float]
[98.98]
>>> print [n for n in l if type(n) is list]
[[1, 2, 3]]
>>> if all(isinstance(n,int) for n in l):
	print "the list your entered is of integer type"
elif all(isinstance(n,str) for n in l):
	print "the list you entered is for string type"
elif all(isinstance(n,list) for n in l):
	print "the list you entered is of list type"
elif all(isinstance(n,float) for n in l):
	print "the list you entered is of float type"
else:
	print "the list you entered is of mixed type"

	
the list you entered is of mixed type
>>> 
