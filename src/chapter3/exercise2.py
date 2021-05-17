try:
	hours = int(input ('Enter hours: '))
	rate = float(input('Enter rate: '))
	pay = hours * rate
	print('pay: ', pay)
except:
	print('error, please put numeric inputs')	