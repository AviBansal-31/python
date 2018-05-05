Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add(a,b)
SyntaxError: invalid syntax
>>> def add (a,b):
	x= a+b
	return x
result = add(12.3,85)
SyntaxError: invalid syntax
>>> def add (a,b):
	x= a+b
	return x
result = add(3,5)
SyntaxError: invalid syntax
>>> def add (a,b):
	x= a+b
	return x
add(3,5)
SyntaxError: invalid syntax
>>> def add(a,b):
	x = a + b
	return x
result = add(3,4)
SyntaxError: invalid syntax
>>> def add(a,b):
	x = a + b
	return x
print add(3,4)
SyntaxError: invalid syntax
>>> def add(a,b):
	x = a + b
	return x

>>> print add(3,4)
7
>>> def multiply(arr,num):
	for x in arr:
		x *= num
	return arr

>>> a = [2,4,10,16]
>>> b = multiply(a,5)
>>> print b
[2, 4, 10, 16]
>>> def multiply(arr,num):
	print arr,num
	for x in arr:
		x*=num
		return arr

	
>>> a = [2,4,10,16]
>>> b = multiply(a,5)
[2, 4, 10, 16] 5
>>> print b
[2, 4, 10, 16]
>>> def multiply(arr,num):
	print arr,num
	for x in arr:
		print x
		x*=num
		return arr

	
>>> a = [2,4,10,16]
>>> b = multiply (a,5)
[2, 4, 10, 16] 5
2
>>> print b
[2, 4, 10, 16]
>>> 
>>> def multiply(arr,num):
	print arr, num
	for x in arr:
		print x
		x *= num
		print arr
		return arr

	
>>> a = [2,4,10,16]
>>> b = multiply(a,5)
[2, 4, 10, 16] 5
2
[2, 4, 10, 16]
>>> print b
[2, 4, 10, 16]
>>> def multiply(arr, num):
	for x in range(len(arr)):
		arr[x] *= num
		return arr

	
>>> a [2,4,10,16]

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a [2,4,10,16]
TypeError: list indices must be integers, not tuple
>>> def multiply(arr, num):
	for x in range(len(arr)):
		arr[x] *= num
		return arr

>>> a = [2,4,10,16]
>>> b = multiply(a,5)
>>> print b
[10, 4, 10, 16]
>>> def multiply(arr, num):
	for x in range(len(arr)):
		arr[x] *= num
	return arr

>>> a = [2,4,10,16]
>>> b = multiply(a,5)
>>> print b
[10, 20, 50, 80]
>>> dog = ("bchdsgy","dffff", "ggg", 26)
>>> print dog [2]
ggg
>>> for data in dog:
	print data

	
bchdsgy
dffff
ggg
26
>>> dog = dog + ("yyy")

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dog = dog + ("yyy")
TypeError: can only concatenate tuple (not "str") to tuple
>>> dog = dog + ("yyy",)
>>> print dog
('bchdsgy', 'dffff', 'ggg', 26, 'yyy')
>>> print len(dog)
5
>>> max(dog)
'yyy'
>>> x = (2,5,4,1,3)
>>> max(x)
5
>>> sum(x)
15
>>> sorted(x)
[1, 2, 3, 4, 5]
>>> def get_circle_area (r):
	c = 2* math.pi *r
	a = math.pi *r * r
	return (c,a)

>>> get_cirle_area(3)

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    get_cirle_area(3)
NameError: name 'get_cirle_area' is not defined
>>> get_circle_area(3)

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    get_circle_area(3)
  File "<pyshell#84>", line 2, in get_circle_area
    c = 2* math.pi *r
NameError: global name 'math' is not defined
>>> def get_circle_area (r):
	c = 2* math.pi *r
	a = math.pi *r * r
	return (c,a)

>>> get_circle_area(3)

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    get_circle_area(3)
  File "<pyshell#87>", line 2, in get_circle_area
    c = 2* math.pi *r
NameError: global name 'math' is not defined
>>> weekend = {"sun": "Sunday", "Sat": "Saturday"}
>>> print weekend["sun"]
Sunday
>>> for data in weekend:
	print data

	
sun
Sat
>>> for key in weekend.iterkeys():
	print key

	
sun
Sat
>>> for val in weekend.itervalues():
	print val

	
Sunday
Saturday
>>> for key,data in weekend.iteritems():
	print key, " = ", data

	
sun  =  Sunday
Sat  =  Saturday
>>> len(weekend)
2
>>> str(weekend)
"{'sun': 'Sunday', 'Sat': 'Saturday'}"
>>> type(weekend)
<type 'dict'>
>>> weekend.copy
<built-in method copy of dict object at 0x00000000056958C8>
>>> weekend.copy()
{'sun': 'Sunday', 'Sat': 'Saturday'}
>>> weekend.clear()
>>> context ={
	'questions': [
	{ 'id' : 1, 'content': 'Why?'}
	{ 'id' : 2, 'content': 'when?'}
	
SyntaxError: invalid syntax
>>> context ={
	'questions': [
	{ 'id' : 1, 'content': 'Why?'}
	{ 'id' : 2, 'content': 'when?'}
	
SyntaxError: invalid syntax
>>> context ={
	'ques': [
	{'id' : 1, 'content': 'why?'}
	['id' : 2, 'content': 'when?'}
	
SyntaxError: invalid syntax
>>> context ={
	'ques': [
	{'id' : 1, 'content': 'why?'},
	{'id' : 2, 'content': 'when?'},
	{'id' : 3, 'content': 'where?'}
	]
}
>>> for key,data in context.items():
	for value in data:
		print "question # ", value["id"], ": ", value["content"]
		print "____"

		
question #  1 :  why?
____
question #  2 :  when?
____
question #  3 :  where?
____
>>> 
