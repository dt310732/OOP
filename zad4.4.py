import random
class Student:

    
    added_students = 0
    registry = {}
    @classmethod
    def count_students(cls):
        print(f'Ilość studentów: {cls.added_students}')

    @staticmethod
    def static_count_students():
        print(f'Ilość studentów: {Student.added_students}')

    @classmethod
    def random_student(cls):
        name = ["Jan", "Anna", "Piotr", "Ola"]
        last_name = ["Kowalski", "Nowak", "Zieliński", "Wiśniewska"]

        return cls(
            random.choice(name),
            random.choice(last_name),
            random.randint(1,5),
            round(random.uniform(2,5), 2)

        )
    
    @classmethod
    def exists(cls, student_id):
        if student_id in cls.registry:
            print("Student istnieje.")
            return True
        else:
            print("Student nie istnieje.")
            return False
        #print(f'Student o ID: {student_id} istnieje')
        #return student_id in cls.registry

    
    def __str__(self):
        lines = []
        for key, value in self.__dict__.items():
            pretty = key.replace("_", " ").capitalize()
            lines.append(f"{pretty}: {value}")
        return "\n".join(lines)


    def __init__(self, imie, nazwisko, rok_studiow, srednia_ocen):
        #Student.added_students += 1 
        type(self).added_students += 1
        self.id = type(self).added_students
        Student.registry[self.id] = type(self).added_students
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok_studiow = rok_studiow
        self.srednia_ocen = srednia_ocen

    #def count_students(self):
        #print(f'Ilość studentów: {Student.added_students}')

    def show_student_info(self):
        print(self.__str__())
        #for key, value in self.__dict__.items():
            #print(f"{key}: {value}")
        #print(f'ID: {self.id}')
        #print(f'Imie: {self.imie}')
        #print(f'Nazwisko: {self.nazwisko}')
        #print(f'Rok studiów: {self.rok_studiow}')
        #print(f'Srednia ocen: {self.srednia_ocen}')




class StudentIT(Student):
    added_students = 0
       

#Jan = Student('Jan', 'Nowak', 4,3.4)
#Bartek = Student('Bartek', 'Kowalski', 1,5.2)
#Bartek.show_student_info()
students = [Student.random_student() for _ in range(10)]
for _ in students:
    _.show_student_info()
    print('\n')

Student.exists(2)