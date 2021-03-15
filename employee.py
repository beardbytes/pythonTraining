class Employee():

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last  + '@gmail.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


	#class methods as alternative constructors
	# cls - convention name of class
	@classmethod
	def set_raise_method(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_string):
		first, last, pay = emp_string.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday == 5 or day.weekday == 6:
			return False
		return True

class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, pay, employee = None):
		super().__init__(first, last, pay)
		if employee is None:
			self.employee = []
		else:
			self.employee = employee

	def add_emp(self, emp):
		if emp not in self.emp:
			self.employee.append(emp)

	def remove_emp(self, emp):
		if emp in self.emp:
			self.employee.remove(emp)

	def print_emp(self):
		for emp in self.employee:
			print('-->', emp.fullname())


dev1 = Developer("Leo", "Messi", 19999, "Python")

manager_1 = Manager('Sue', 'Smith', 90000, [dev1])

print(isinstance(manager_1, Manager))

# print(manager_1.email)

# manager_1.print_emp()

# print(dev1.email)
# print(dev1.prog_lang)

# import datetime
# my_date = datetime.date(2021, 3, 12)

# print(Employee.is_workday(my_date))


# emp1 = Employee("Aditya", "Maheshwari", 50000)
# emp2 = Employee("Logan", "Maverick", 60000)

# emp_string_1 = 'Leo-Messi-10000'
# emp_string_2 = 'CR-7-3000'

# new_emp = Employee.from_string(emp_string_1)

# print(new_emp.email)
# print(new_emp.pay)


# Employee.set_raise_method(1.05)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)


#namespace
#print(emp1.__dict__)
#print(Employee.num_of_emps)