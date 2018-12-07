class Employee(object):
	def __init__(self, name, year_of_birth, hourly_rate):
		self.name = name
		self.year_of_birth = int(year_of_birth)
		self.hourly_rate = float(hourly_rate)

	def __str__(self):
		return "<Employee:%s>" %self.name

