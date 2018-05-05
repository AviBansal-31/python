Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def multiply(arr,num):
	for x in range(len(arr)):
		arr[x] *= num
	return arr

>>> def layered_multiple(arr):
	new_array = []
	for i in range(len(arr)):
		array_1 = []
		for j in range(arr[i]):
			array_1.append(1)
			new_array.append(array_1)
		return new_array

	
>>> x = layered_multiple(multiply([2,4,5],3))
>>> print x
[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
>>> 
