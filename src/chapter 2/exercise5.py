temperature = float(input('Enter a value you want to convert: '))
choice = input('Entered valus is in (F) or (C) please select: ')
if choice.upper() == "F":
	degreecl = ((temperature - 32) * (5 / 9))
	print('Temperature in degrees C is: ', degreecl)
elif choice.upper() ==" C":
	degreef = ((temperature + 32) * (9 /5))	
	print('Temperature in degrees F is: ', degreef)
else:
	print('wrong input')	