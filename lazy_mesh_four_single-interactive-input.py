'''

rnd (* 4 _ ) in (-9 ... 9) as LIST

out: both: sum LIST and LIST as abs _ of LIST

'''

import random

def oSUM():
	LIST = (lambda: [random.choice(range(-9,9)),random.choice(range(-9,9)),random.choice(range(-9,9)),random.choice(range(-9,9))])
	list_holder = LIST()
	SUM = sum(list_holder)
	'''
	times rnd choice pos neg
	'''
	outLIST = [random.choice([1,-1]) * n for n in list_holder]
	return (abs(SUM), tuple(outLIST))

while True:
	oSUMrn = oSUM() 
	print(oSUMrn)

	uInput = input()
	uSet = []
	for n in uInput:
		if n.isdigit():
			uSet.insert(0, int(n))

	try:
		if eval(uInput) == oSUMrn[0] and set(uSet) == set([abs(x) for x in oSUMrn[1]]):
			print('this is a fact ... please go sum more')
		else:
			print('not so')
			break
	except NameError:
		print('not so')
		break




