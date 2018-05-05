Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
>>> for x in users:
	print x
	for i in range(len(users[x])):
		print (i+1), " - ", users[x][i]['first_name'], users[x][i]['last_name'], " - ", len(users[x][i]['first_name'])+ len(users[x][i]['last_name'])

		
Students
1  -  Michael Jordan  -  13
2  -  John Rosales  -  11
3  -  Mark Guillen  -  11
4  -  KB Tonel  -  7
Instructors
1  -  Michael Choi  -  11
2  -  Martin Puryear  -  13
>>> 
