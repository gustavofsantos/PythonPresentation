def fib_rec(x):
	if x >= 0 and x < 2:
		return x
	else:
		return fib_rec(x - 1) + fib_rec(x - 2)