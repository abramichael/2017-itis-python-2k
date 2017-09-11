import random
from abc import abstractmethod

class Car(object):
	n = 0
	def __init__(self, color, brand, year):
		self.color = color
		self.brand = brand
		self.year = year
		self.__secret_code = random.random()
		Car.n += 1
		
	def start(self):
		print "Bibika is starting"

	def __str__(self):
		return "%s %s, %s" % (self.color, self.brand, self.year)
	
	@staticmethod
	def get_car_number():
		return Car.n
		
	@classmethod
	def get_new_instance(cls):
		return Car(None, None, None)
		
	@abstractmethod
	def ride(self):
		pass

	def __add__(self, car2):
		return Car(self.color + car2.color,
			self.brand + car2.brand,
			(self.year + car2.year) / 2)

class TeslaCar(Car):
	def __init__(self, color, brand, year):
		super(TeslaCar, self).__init__(color, brand, year)
		self.electricity = True
		
	
#Python's main
if __name__ == "__main__":
	print "My Classes file"