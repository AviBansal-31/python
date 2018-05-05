Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def multiply(arr, num):
	for x in range(len(arr)):
		arr[x] *= num
	return arr

>>> a= [2,4,10,16]
>>> b= multiply(a,5)
>>> print b
[10, 20, 50, 80]
>>> 
