import random

def Coin():
	results = ['heads', 'tails']
	return results[random.randrange(0,2)]

def Experiment():
	heads = 0 
	counter = 1
	while heads < 3:
		result = Coin()
		counter += 1
		if result == 'heads':
			heads += 1
		else:
			heads = 0

	#print "It took %d flips to get 3 heads in a row." % counter
	return counter


run_experiment = 1000

results = []
for i in range(0, run_experiment):
	r = Experiment()
	results.append(r)

average = sum(results) / run_experiment
print "Experiment ran %d times. Average flips to get 3 heads was %d" % (run_experiment, average)
    