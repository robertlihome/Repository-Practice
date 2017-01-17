#/usr/bin/env python

#get user input
user_in = input("Type Something ")

#repeat until a 'q' appears
while user_in.find("q")==-1:
#determine if it's a single character or string
	if len(user_in)<1:
		print ("Empty")
	elif len(user_in)<2:
		print ("It's a character")
	else: 
		print ("It's a string")
	
#print each character
	for i in range(len(user_in)):
		print ("user_in[" + str(i) + "] = " + user_in[i])	
#ask user again
	user_in=input("Type Something Again ")

print ("Quit")
