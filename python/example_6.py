'''
题目：斐波那契数列。
'''

res = [0]

a,b = 0,1

dep = 20 #长度为20

for i in range(dep):
	a,b = b,a+b
	res.append(a)

print('res = ',res)


print(50*'-')

#递归方法实现

def fib_recur(n):

	assert n >= 0

	if n in (0,1):
		return n

	return fib_recur(n-1) + fib_recur(n - 2)

for i in range(20):
	print(fib_recur(i),end=' ')