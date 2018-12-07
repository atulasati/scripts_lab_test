import datetime
from employee import Employee

def validate_year_of_birth(year_of_birth):
	return year_of_birth.strip().isdigit() and len(year_of_birth.strip()) == 4

def validate_employee_name(emp_name):
	emp_name = emp_name.replace(" ","")
	return len(emp_name) > 2 and emp_name.isalpha()

def validate_float(hourly_rate):
	try:
		hourly_rate = float(hourly_rate)
	except:
		return False
	return True


class HR(object):
	def __init__(self, name):
		self.name = name
		self.employee_list = []

	def add_employee(self):
		while True:
			emp_name = input ("What is the name of the employee? ")
			if validate_employee_name(emp_name):
				break
			else:
				print ("Invalid Name. ", end=" ")
		while True:
			year_of_birth = input ("What is his/her year of birth (yyyy)? ")
			if validate_year_of_birth(year_of_birth):
				break
			else:
				print ("Invalid Year of Birth. ", end=" ")
		while True:
			hourly_rate = input ("What is his/her hourly rate ($/h)? ")
			if validate_float(hourly_rate):
				break
			else:
				print ("Invalid Rate. ", end=" ")

		employee = Employee(emp_name, year_of_birth, hourly_rate)
		self.employee_list.append(employee)

	def display_employee_salary(self):
		if self.employee_list:
			while True:
				emp_name = input ("Which employee are you looking for? ")
				if not validate_employee_name(emp_name):
					print ("Invalid Name. ", end="")
					continue

				employee = None
				for emp in self.employee_list:
					if emp.name == emp_name:
						employee = emp
						break
				if employee:
					break
				else:
					print ("The Employee doesn't exist in the directory!", end=" ")
					return
			while True:
				hours_worked = input ("How many hours did he/she worked this week? ")
				if validate_float(hours_worked):
					hours_worked = float(hours_worked)
					amount = hours_worked * float(emp.hourly_rate) 
					print ("The salary of %s for %s h is %s" %(emp.name, "%.2f" %hours_worked, "$%.2f" %(amount)))
					return
				else:
					print ("Invalid number of hours. ", end=" ")				
		else:
			print ("There are no employee in this directory.")

	def return_employee_age(self, i_empname=None):
		if self.employee_list:
			while True:
				if not i_empname:
					emp_name = input ("Which employee you are looking for? ")
				else:
					emp_name = i_empname
				for emp in self.employee_list:
					if emp.name == emp_name:
						age = datetime.datetime.today().year - emp.year_of_birth
						if not i_empname:
							print ("The employee %s is %s years old." %(emp.name, age))
						return age
				print ("The employee doesn't exist in the directory!")
				break
		else:
			print ("There are no employee in the directory!")

	def display_all_employees(self):
		if self.employee_list:
			print ("Here is the list of employees contained in the directory:")
			for idx, emp in enumerate(self.employee_list):
				age = self.return_employee_age(emp.name)
				hourly_rate = "$%.2f" %emp.hourly_rate
				emp_details = (idx+1, emp.name, emp.year_of_birth, age, hourly_rate)
				print ("Employee(%s) - Name: %s, YoB: %s, Age: %s, HourlyRate: %s" %emp_details)
			print ("There is/are %s employee(s) in the directory" %len(self.employee_list))
		else:
			print ("There are no employee in the directory!")

print ("Devoir 4 Anthony Ilunga")
print ("Utilisation de classe et module. Script pour manipuler des employé(e)s).\n")


hr_direcotory = HR(name='directory')

while(True):
	command = "\n-------------------------------------------\n"
	command += "1 - Add employees to the directory\n"
	command += "2 - Display employee salary\n"
	command += "3 - Display employee age\n"
	command += "4 - Display all employees\n"
	command += "5 - Quit\n"
	command += "Input a command: "
	command = input (command)

	if command.strip() == "1":
		while True:
			hr_direcotory.add_employee()
			more_employee = input ("Do you want to enter another employee? (y or Y) ")
			if more_employee.strip() != "y":
				break

	elif command.strip() == "2":
		hr_direcotory.display_employee_salary()
	elif command.strip() == "3":
		hr_direcotory.return_employee_age()
	elif command.strip() == "4":
		hr_direcotory.display_all_employees()
	elif command == "5":
			break			
	else:
		print("Invalid command.\n")
input("Press Enter key to exit.")