Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> def coin_toss(num):
	recordList = []
	attempt = 0
	heads =0
	tails =0
	for i in range(num):
		flip = random.randint(0, 1)
		attempt += 1
		if (flip == 0):
			print "It's heads"
			recordList.append("Heads")
		else:
			print "It's Tails"
			recordList.append("Tails")
		print "Attempt # " + str(attempt) + " Throwing a coin...Got " + str(recordList.count("Heads"))+ " heads and "+ str(recordList.count("Tails")) + " tails so far..!"

>>> coin_toss(10)
It's Tails
Attempt # 1 Throwing a coin...Got 0 heads and 1 tails so far..!
It's Tails
Attempt # 2 Throwing a coin...Got 0 heads and 2 tails so far..!
It's Tails
Attempt # 3 Throwing a coin...Got 0 heads and 3 tails so far..!
It's Tails
Attempt # 4 Throwing a coin...Got 0 heads and 4 tails so far..!
It's heads
Attempt # 5 Throwing a coin...Got 1 heads and 4 tails so far..!
It's heads
Attempt # 6 Throwing a coin...Got 2 heads and 4 tails so far..!
It's Tails
Attempt # 7 Throwing a coin...Got 2 heads and 5 tails so far..!
It's Tails
Attempt # 8 Throwing a coin...Got 2 heads and 6 tails so far..!
It's heads
Attempt # 9 Throwing a coin...Got 3 heads and 6 tails so far..!
It's heads
Attempt # 10 Throwing a coin...Got 4 heads and 6 tails so far..!
>>> 
