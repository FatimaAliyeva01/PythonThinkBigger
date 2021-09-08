#exploreObject(obj) adında bir metod yazın. Bu metod argument olaraq verilən istənilən 
#obyektin bütün xüsusiyyətlərini
#hansı property-ləri olduğunu və onların value-sunu
#hansı metodlarının olduğunu və nə return etdiyini

class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def word():
        print("Hello Fatima Aliyeva")
    def word1():
        print("Backend Developer")


def exploreObject(obj):
    for property, value in vars(obj).items():
        print(property, ":", value)
    method_list = [method for method in dir(Student) if method.startswith('__') is False]
    print (method_list)

user = Student("Fatima", "Aliyeva", 20)
exploreObject(user)


