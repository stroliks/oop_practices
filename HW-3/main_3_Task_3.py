

class Robot:
    def __init__(self, number:int, model: str, batary_level: float, status="break", task=None):
        self.__number = number
        self.__model = model
        self.__task = task
        self.__batary_level = batary_level
        self.__status = status


    def get_number(self):
        return self.__number
    def get_model(self):
        return self.__model
    def get_task(self):
        return self.__task
    def get_batary_level(self):
        return self.__batary_level
    def get_status(self):
        return self.__status


    def set_number(self, number: int):
        self.__number = number

    def set_model(self, model: str):
        self.__model = model

    def new_task(self, task: str):
        if task != self.__task:
            self.__task = task

    def change_level_batary(self, delta_level: float):
        self.__batary_level += delta_level

    def work(self):
        self.__status = "в работе"

    def break_(self):
        self.__status = "перерыв"

    def __str__(self):
        return f"Номер:,{self.__number} модель:{self.__model}, задача:{self.__task}, заряд:{self.__batary_level}, состояние:{self.__status}"



robot1 = Robot("peek","458623", 51, "в работе")

robot2 = Robot("bib","01", 95, )

print(robot1)
print(robot2)

robot1.break_()
robot1.new_task("feel")
robot2.change_level_batary(-25)

print(robot1)
print(robot2)