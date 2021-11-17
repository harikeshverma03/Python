def fib(n,memo):
	if memo[n-1]!=None:
		return memo[n-1]
	else:
		if n==1 or n==2:
			result = 1
		else:
			result = fib(n-1,memo) + fib(n-2, memo)
		memo[n-1] = result
		return result 
def fib_2(n):
	memo = [None] * (n)
	return fib(n,memo)
def fib_bottom_up(n):
	if n==1 or n==2:
		return 1
	bottom_up = [None] * (n+1)
	bottom_up[1] = bottom_up[2] = 1
	for i in range(3,n+1):
		bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
	
	return bottom_up[n]



n = int(input("Enter a Number N   \n"))
if n > 990:
	fib = fib_bottom_up(n)
else:
	fib = fib_2(n)
print(f'The {n} number in fibonacci Series is {fib}')