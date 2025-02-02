
class Student:
    def __init__(self, first_name, last_name, age, avg_ball):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__avg_ball = avg_ball

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    def get_avg_ball(self):
        return self.__avg_ball

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_age(self, age):
        self.__age = age

    def set_avg_ball(self, avg_ball):
        self.__avg_ball = avg_ball

    def __str__(self):
        return f"Имя: {self.__first_name}, Фамилия:{self.__last_name}, Возраст:{self.__age}, Средний балл:{self.__avg_ball}"

    def __eq__(self, other):
        if self.__avg_ball == other.__avg_ball:
            return True
        return False

    def __lt__(self, other):
        if self.__avg_ball < other.__avg_ball:
            return True
        return False

    def __le__(self, other):
        if self.__avg_ball <= other.__avg_ball:
            return True
        return False


    # прочитал что можно переопределить только 3 метода. остальные Питон автоматически переопределит сам
    # def __ne__(self, other):
    #     return not self.__avg_ball == other.__avg_ball

    # def __gt__(self, other):
    #     return not self.__avg_ball < other.__avg_ball
    #
    # def __ge__(self, other):
    #     return not self.__avg_ball <= other.__avg_ball

man1_ = Student("Bob", "Bobov", 21, 3.5)
man2_ = Student("Pop", "Popov", 12, 4.5)
man3_ = Student("Kot", "Kotov", 15, 3.5)
man4_ = Student("Pit", "Pitov", 19, 5.6)

print(man1_==man2_)
print(man1_!=man3_)
print(man3_<man4_)
print(man3_<=man4_)
print(man3_>man4_)
print(man3_>=man4_)