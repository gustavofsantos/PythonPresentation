def fatorial(x):
	if x < 0:
		return None
	elif x < 2:
		return x
	else:
		return x*fatorial(x-1)