# -*- coding: UTF-8 -*-
'''
模拟linux用户登录
'''

import time

global user,name

user = {'111':'3243'}

def login():
	global name
	name = input('Username: ')
	pswd = input('Password: ')
	if name not in user:
		return False
	return user[name] == pswd

while (login()):
	time.sleep(3) #暂停3秒
	print('Authentication failure')

print('{}@localhost:~$'.format(name))