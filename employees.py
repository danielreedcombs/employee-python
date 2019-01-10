#Create a class that contains information about employees of a company
# and define methods to get/set employee name, job title,
# and start date.
class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""
        return self.company_name
#Consider the concept of aggregation,
#and modify the Company class so that you assign employees to a company.
    def __str__(self):
        return f" The Company {self.company_name} was founded in {self.date_founded}. The current employees are {self.employees}"
    pass

Dillards = Company("Dillars", "1/24/1992")
print(Dillards)

#Create a company, and three employees,
Dillards.employees.add("Zac")
Dillards.employees.add("Daniel")
Dillards.employees.add("Ousama")
print(Dillards)


#and then assign the employees to the company.