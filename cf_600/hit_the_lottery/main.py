bills = 0
den = [100, 20, 10, 5, 1]
n = int(input())
for d in range(len(den)):
	b = n // den[d]
	if b > 0:
		bills += n // den[d]
		n = n % den[d]
print(int(bills))
