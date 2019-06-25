'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

attr_num = input('请输入3个数字: ')

num = attr_num.split(',')

for i in range(len(num)):
	num[i] = int(num[i])

#num.sort(reverse=False)

num = sorted(num,reverse=True)

#print('排序结果: \n' + str(num))

print('排序结果: \n' + str(num))

'''
def sort(self, key=None, reverse=False):
key:是排序的条件,可以是：key=int，key=len(按照长度排序)，key=str.lower(忽略大小写) key=lambda..
reverse:表示是否反序，默认从小到大，默认为Flase
一个list调用sort方法后，对原list进行排序
'''

'''
def sorted(*args, **kwargs):
sorted(L)返回一个排序后的L，不改变原始的L；
L.sort()是对原始的L进行操作，调用后原始的L会改变，没有返回值。【所以a = a.sort()是错的啦！a = sorted(a)才对！
sorted()适用于任何可迭代容器，list.sort()仅支持list（本身就是list的一个方法）

'''