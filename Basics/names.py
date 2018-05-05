Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
>>> for i in students:
	print i['first_name'], i['last_name']

	
Michael Jordan
John Rosales
Mark Guillen
KB Tonel
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
>>> for x in range(len(users)):
	print "Students"
	for i in range(len(users['Students'])):
		print (i+1), " - ", users['Students'][i]['first_name'], users['Students'][i]['last_name'], " - ", len(users['Students'][i]['first_name'])+ len(users['Students'][i]['last_name'])
	print "Instructors"
	for i in range(len(users['Instructors'])):
		print (i+1), " - ", users['Instructors'][i]['first_name'], users['Instructors'][i]['last_name'], " - ", len(users['Instructors'][i]['first_name'])+ len(users['Instructors'][i]['last_name'])

		
Students
1  -  Michael Jordan  -  13
2  -  John Rosales  -  11
3  -  Mark Guillen  -  11
4  -  KB Tonel  -  7
Instructors
1  -  Michael Choi  -  11
2  -  Martin Puryear  -  13
Students
1  -  Michael Jordan  -  13
2  -  John Rosales  -  11
3  -  Mark Guillen  -  11
4  -  KB Tonel  -  7
Instructors
1  -  Michael Choi  -  11
2  -  Martin Puryear  -  13
>>> 
