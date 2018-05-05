Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> sI = 45
>>> mI = 100
>>> bI = 455
>>> eI = 0
>>> spI = -23
>>> sS = "Rubber baby buggy bumpers"
>>> mS = "Experience is simply the name we give our mistakes"
>>> bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
>>> eS = ""
>>> aL = [1,7,4,21]
>>> mL = [3,5,7,34,3,2,113,65,8,89]
>>> lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
>>> eL = []
>>> spL = ['name','address','phone number','social security number']
>>> x = bS
>>> x_type = type(x)
>>> if x_type is int:
	if x >= 100:
		print "This is an big number"
		else:
			
SyntaxError: invalid syntax
>>> if x_type is int:
	if x>= 100:
		print "Big number"
	else:
		print "Small number"
    elif x_type is str:
	    
  File "<pyshell#25>", line 7
    elif x_type is str:
                      ^
IndentationError: unindent does not match any outer indentation level
>>> if x_type is int:
	if x>= 100:
		print "Big number"
	else:
		print "Small number"
elif x_type is str:
	if len(x) >= 50:
		print "Long string"
	else:
		print "short string"
elif isinstance(x, list):
	if len(x) >= 10:
		print "Long list"
	else:
		print "short list"

		
Long string
>>> 
