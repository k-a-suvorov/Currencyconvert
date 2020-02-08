#First simple version currency converter
try:

	print('''This program can to view rubles in to the some currencies
	Now you can a view some \"US"\, \"GB\", \"Eur\" currencies.''')


	#Block of input of user values
	Roubles = int(input('How many rubles do You have now? '))
	Roubles = float(Roubles)

	us = 65
	gbr = 86
	eur = 72


	def convertRoubles(Roubles, a):
		convert = round((Roubles / a), 2)
		return convert

	print('In US You have a ', convertRoubles(Roubles, us))
	print('In GBR You have a ', convertRoubles(Roubles, gbr))
	print('In Euro You have a', convertRoubles(Roubles, eur))

	#Block of proccesing data
	#Block of print data


except ValueError:
    print("You have some mistake of userinput current float Value")
except TypeError:
    print("You have some mistake of userinput float Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!" )

