import time

def benchmark(method, x, eps):
	'''
	Calls method with arguments x and eps.
	Returns timing data along with output, and runs the method
	multiple times automatically if the initial call was too fast.
	'''

	dt = 0
	looper = 1
	while dt < 1e-2:

		start = time.clock()
		for _ in range(looper):			
			b = method(x, eps)
		end = time.clock()

		dt = end - start
		looper *= 10

	return dt * 10 / looper, b
