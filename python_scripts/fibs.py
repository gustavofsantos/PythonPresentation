import sys

def fib(x):
	if x < 2 and x >= 0:
		return x
	else:
		return fib(x - 1) + fib(x - 2)

if __name__ == '__main__':
	v = sys.argv[1]
	v = int(v)
	print(fib(v))