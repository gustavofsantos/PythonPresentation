from fib_rec import fib_rec
from fib_cache import fib_cache
import time

def test_cache(valores):
	tempos = []
	for x in valores:
		t1 = time.time()
		r = fib_cache(x)
		t2 = time.time()
		tempos.append(t2 - t1)
	return tempos


def test_rec(valores):
	tempos = []
	for x in valores:
		t1 = time.time()
		r = fib_rec(x)
		t2 = time.time()
		tempos.append(t2 - t1)
	return tempos
