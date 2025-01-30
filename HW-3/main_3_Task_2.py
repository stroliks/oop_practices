
class Employee:
    def __init__(self, name:str, position: str, department: str, salary: float, expirience: int, projects = None):
        self.__name = name
        self.__position = position
        self.__department = department
        self.__salary = salary
        self.__expirience = expirience
        self.__projects = []
        if projects is not None:
            self.__projects.append(projects)


    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position
    def get_department(self):
        return self.__department
    def get_salary(self):
        return self.__salary
    def get_expirience(self):
        return self.__expirience
    def get_projects(self):
        return self.__projects


    def set_position(self, position: str):
        self.__position = position

    def set_department(self, department: str):
        self.__department = department

    def set_expirience(self, expirience: int):
        self.__expirience = expirience

    def add_projects(self, project: str):
        self.__projects.append(project)

    def remove_projects(self, project: str):
        if project not in self.__projects:
            raise ValueError("акого проекта нет")
        self.__projects.remove(project)

    def increase_salary(self, delta_salary):
        if delta_salary <= 0:
            raise ValueError("олько на увеличение")
        self.__salary += delta_salary


    def __str__(self):
        return f"Имя:,{self.__name} должность:{self.__position}, отдел:{self.__department}, ЗП:{self.__salary}, стаж:{self.__expirience}, Проекты:{self.__projects}"



sotr1 = Employee("Bob","manager", "X", 15215, 15)

sotr2 = Employee("Fred","director", "elite", 150000, 2, "casino")



print(sotr1)
print(sotr2)

sotr1.add_projects("mega")
sotr2.add_projects("NO mega")

print(sotr1)
print(sotr2)

sotr1.increase_salary(300000)
sotr2.remove_projects("casino")

print(sotr1)
print(sotr2)