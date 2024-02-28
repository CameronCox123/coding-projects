#  File: EmployeeSalaries.py
#  Student Name: Cameron Cox
#  Student UT EID: cpc2526

# Creates several classes and subclasses revolving around employees. Uses kwargs to get around empty inputs.
# Cal_salaries is in the Employee class because each subclass inherits from Employee and needs to access that function. 2z

# Our super class that all other classes will inherit from. cal_salaries is here so everyone can calculate their salaries 
class Employee:
    # Initializing our variables using kwargs
    def __init__(self, **kwargs):
        name = kwargs.get('name')
        id = kwargs.get('id')
        base_salary = kwargs.get('salary')

        self.name = name
        self.id = id
        self.salary = float(base_salary)

    # Getters and setters for all employees
    def get_name(self):
        return(self.name)

    def get_id(self):
        return(self.id)

    def set_name(self, name):
         self.name = name
         return(self.name)
    
    def set_id(self, id):
        self.id = id
        return(self.id)

    # Formatted string just for Employees
    def __str__(self):
        return(f'Employee \n{self.name},{self.id},{self.salary}')
    
    # One massive function that calculates the salaries for each employee
    def cal_salary(self):
        final_salary = self.salary
        # Testing for benefits
        try: 
            if self.benefits == None:
                pass
            elif self.benefits == ['health_insurance']:
                final_salary = self.salary * 0.9
            elif self.benefits == ['retirement']:
                final_salary = self.salary * 0.8
            else:
                final_salary = self.salary * 0.7
        except:
             pass

        # Testing for employees who are paid hourly and then adding trips if necessary
        try: 
            final_salary = self.hours * self.salary
            if self.travel != None:
                temp = self.travel * 1000
                final_salary += temp
        except:
            pass

        # Testing if an employee has a bonus
        try:
            if self.bonus != None:
                 final_salary += self.bonus
        except: 
             pass
        
        return final_salary


############################################################
############################################################
############################################################
class Permanent_Employee(Employee):
    # Inherits from Employee class
    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        benefits = kwargs.get('benefits')
        self.benefits = benefits

    # Gets and sets benefits
    def get_benefits(self):
        return(self.benefits)

    def set_bonus(self, bonus):
         self.bonus = bonus
         return(self.bonus)

    # Formatted string just for Permanant Employees
    def __str__(self):
            return(f'Permanent Employee \n{self.name},{self.id},{self.salary},{self.benefits}')


############################################################
############################################################
############################################################
class Manager(Employee):
    # Also inherits from the Employee Class
    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        bonus = kwargs.get('bonus')
        self.bonus = bonus
    
    # Get and set bonus
    def get_bonus(self):
        return(self.bonus)
    
    def set_bonus(self, bonus):
         self.bonus = bonus
         return(self.bonus)

    # Formatted string just for Managers
    def __str__(self):
            return(f'Manager \n{self.name},{self.id},{self.salary},{self.bonus}')        


############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    # Also inherits from the Employee Class
    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        hours = kwargs.get('hours')
        self.hours = hours

    # Gets and sets hours
    def get_hours(self):
        return(self.hours)
    
    def set_hours(self, hours):
         self.hours = hours
         return(self.hours)

    # Formatted string just for Temporary Employees    
    def __str__(self):
            return(f'Temporary Employee \n{self.name},{self.id},{self.salary},{self.hours}')        


############################################################
############################################################
############################################################
class Consultant(Temporary_Employee):
    # Inherits from the Temporary Employee class who inherits from the Employee Class
    def __init__(self, **kwargs):
        Temporary_Employee.__init__(self, **kwargs)
        travel = kwargs.get('travel')
        self.travel = travel

    # Gets and sets travel
    def get_travel(self):
         return(self.travel)
    
    def set_travel(self, travel):
         self.travel = travel
         return(self.travel)

    # Formatted string just for Consultants
    def __str__(self):
            return(f'Consultant \n{self.name},{self.id},{self.salary},{self.hours},{self.travel}')       

############################################################
############################################################
############################################################
class Consultant_Manager(Consultant, Manager):
    # Inherits from both Manager and Consultant classes
    def __init__(self,  **kwargs):
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)

    # Formatted string just for Consulatant Manager. Break line for readability
    def __str__(self):
            return(f'Consultant Manager \n{self.name},{self.id},{self.salary},{self.hours},{self.travel},Consultant_Manager \
                   \n{self.name},{self.id},{self.salary},{self.bonus}')       
        

############################################################
############################################################
############################################################

def calculate_total_salaries(employee_list):
    total_salaries = 0
    for employee in employee_list:
         total_salaries += employee.cal_salary()

    return total_salaries

def calculate_manager_salaries(employee_list):
    total_salaries = 0
    for manager in employee_list:
         total_salaries += manager.cal_salary()

    return total_salaries


''' ##### DRIVER CODE #####
    ##### Do not change. '''

# create employees
chris = Employee(name="Chris", id="UT1", salary=80000)
emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)

# print employees
print(chris, "\n")
print(emma, "\n")
print(sam, "\n")
print(john, "\n")
print(charlotte, "\n")
print(matt, "\n")

# calculate and print salaries
print("Check Salaries")
print("Emma's Salary is:", emma.cal_salary())
emma.benefits = ["health_insurance"]
print("Emma's Salary is:", emma.cal_salary())
emma.benefits = ["retirement", "health_insurance"]
print("Emma's Salary is:", emma.cal_salary())
print("Sam's Salary is:", sam.cal_salary())
print("John's Salary is:", john.cal_salary())
print("Charlotte's Salary is:", charlotte.cal_salary())
print("Matt's Salary is:",  matt.cal_salary())