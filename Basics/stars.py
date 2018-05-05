Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def stars(arr):
	for i in range(len(arr)):
		print ("*" * arr[i])
	return

>>> stars([4,6,1,3,5,7,25])
****
******
*
***
*****
*******
*************************
>>> def stars_2(arr):
	for i in arr:
		if isinstance(i,int):
			print ("*" * i)
		elif isinstance(i,str):

			char = i[0].lower()
			print char * len(i)

			
>>> stars_2([4, "Tom", 1, "Michael", 5,7, "Jimmy Smith"])
****
ttt
*
mmmmmmm
*****
*******
jjjjjjjjjjj
>>> 
