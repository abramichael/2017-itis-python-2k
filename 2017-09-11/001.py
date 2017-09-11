#encoding: utf-8

def f1(st):
	s = 0
	lst = st.split()
	for item in lst:
		s += int(item)
	return s

# [] - список/list, () - кортеж/tuple

def f2(lst):
	s = 0
	for item in lst:
		s += item
	return s
	
# *args

def f3(*args):
	s = 0
	for item in args:
		s += item
	return s	
	
print f3(1,2,3)
print f3(10,20,50,20)
	
# **kwargs

def f4(**kwargs):
	for key, value in kwargs.iteritems():
		print(key, value)
		
f4(student='Zarina', course='Informatika', teacher='Khasianov', mark='5')

	