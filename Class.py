class Employee:
	def __init__(self, pay):


		self.pay = pay
	def apply_raise(self):


		self.pay = self.pay * 0.05
		return self.pay
emp = Employee(2000)

print(emp.apply_raise())


