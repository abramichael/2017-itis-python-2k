def tell_the_date(day=1, month=1, year=2017):
	#print "Today is %s of month %s of year %s." % (day, month, year)
	print "Today is {day} of month {month} of year {year}.".format(
		day=day, month=month, year=year
	)
	

tell_the_date(11,9,2017)
tell_the_date()
tell_the_date(year=2016)
tell_the_date(year=2015, month=12)