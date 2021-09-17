# TODO : yield keyword
"""
	* The yield keyword can turn any function into generator
	* yield acts similar like return keyword but it always returns generator object
	* Function can have multiple calls to the yield keyword
"""

def gendays(index):
	weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
	yield weekdays[index]
	yield weekdays[index+1]

days = gendays(0)
print(next(days))
print(next(days))