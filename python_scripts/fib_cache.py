from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cache(x):
	if x >= 0 and x < 2:
		return x
	else:
		return fib_cache(x - 1) + fib_cache(x - 2)
