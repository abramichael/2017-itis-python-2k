#import my_classes
#from my_classes import *
from my_classes import Car, TeslaCar

a = Car("Mokryj Asfalt", "VAZ2107", 1979)
#print a
#print Car

#list of all methods
#print dir(a)

#all vars of program from current scope
#print globals()

print a.__dict__
#a.number_of_wheels = 4
#print a.__dict__
#print a.__secret_code - not working

a.start()
print str(a)

b = TeslaCar("Red", "Tesla", 2016)
print b
print b.electricity

print Car.n
print a.n
print b.n

#check attribute
print hasattr(a, "brand")
#get attribute
print getattr(a, "brand", "TAZ2109")


print a + b