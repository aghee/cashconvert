
#1 usd=0.7620euros
#1 euro=1.3140 usd
def currencyconvert():
	userchoice=raw_input("what do you want to convert?\n1.usd to euro \n2.euro to usd\n")
	if userchoice=='1':
		userusd=input("enter the usd amount you wish to convert\n")
		euro=userusd*0.7617
		print "$ %0.2f"%userusd,"=%0.2f"%euro,"euros"
		doagain()
	elif userchoice=="2":
		usereuro=input("enter amount in euro you wish to convert\n")
		usd=usereuro*1.3138
		print"%0.2f" %usereuro,"=%0.2f"%usd,"usd"
		doagain()
	else:
		print("wrong input.please try again")
		currencyconvert()
def doagain():
	doagain=raw_input("Want to repeat the conversion?\n1.YES PLEASE\n2.NO THANK YOU\n")
	if doagain=="1":
		currencyconvert()
	elif doagain=="2":
		print('THANK YOU FOR USING MY SCRIPT.')
	else:
		print('wrong input.please retry!!!')
		currencyconvert()
currencyconvert()

