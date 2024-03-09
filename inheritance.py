class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)


class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    # overwriting __str__
    def __str__(self):
        text = super(Worker, self).__str__()
        text += ", Salary {}".format(self.salary)
        return text

    def calc_yearly_salary(self):
        return self.salary * 12


worker_1 = Worker("Sparrow", 40, 176, 3000)
print(worker_1)
print(f'Yearly Salary: {worker_1.calc_yearly_salary()}')
