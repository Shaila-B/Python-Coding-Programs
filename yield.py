def testgen(index):
	weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
	yield[index]
	yield[index+1]

day=testgen(0)
print(next(day))
print(next(day))