def format(s, **kwargs):
	for k, v in kwargs.iteritems():
		s = s.replace("{" + k + "}", v)
	return s
	
print format("Student: {firstname} {lastname}", 
			firstname='Bulat', lastname='Giniatullin')
			
