Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> words = "It's Thanksgiving day. It's my birthday, too!"
>>> words.find("day")
18
>>> words.replace("day", "month")
"It's Thanksgiving month. It's my birthmonth, too!"
>>> x= [2,54,-2,7,12,98]
>>> x.min()

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.min()
AttributeError: 'list' object has no attribute 'min'
>>> min(x)
-2
>>> max(x)
98
>>> x= ["hello",2,54,-2,7,12,98,"world"]
>>> x.len()

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x.len()
AttributeError: 'list' object has no attribute 'len'
>>> len(x)
8
>>> first_ele = x[0]
>>> print first_ele
hello
>>> last_ele = x[8]

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    last_ele = x[8]
IndexError: list index out of range
>>> last_ele= x[7]
>>> print last_ele
world
>>> x= [19,2,54,-2,7,12,98,32,10,-3,6]
>>> x.sort()
>>> print x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> def split_into_half:
	
SyntaxError: invalid syntax
>>> def split_into_half(x):
	half = len(x)/2
	return x[:half], x[half:]

>>> 
>>> x=[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> def split_into_half(x):
	half = len(x)/2
	return x[:half], x[half:]
x=[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
SyntaxError: invalid syntax
>>> 
>>> print x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> half = len(x)/2
>>> x1=[:half]
SyntaxError: invalid syntax
>>> x1 = x[:half]
>>> print x1
[-3, -2, 2, 6, 7]
>>> x2 = x[half:]
>>> print x2
[10, 12, 19, 32, 54, 98]
>>> x2.insert(0,x1)
>>> print x2
[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
>>> 
