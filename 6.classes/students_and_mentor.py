class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if 0 <= grade <= 10:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return f'ОШИБКА: выставляемая лектору {lecturer.surname} оценка - {grade} ' \
                   f'должна быть в пределах от 0 до 10!'

    def sum(self):
        calc=int()
        for course in self.grades.values():
            for grade in course:
                calc += grade
        sum = round(calc/len(course), 1)
        return sum

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.sum()}\
              \nКурсы обучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    
    def sum(self):
        calc=int()
        for course in self.grades.values():
            for grade in course:
                calc += grade
        sum = round(calc/len(course), 1)
        return sum

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.sum()}'
        return res
    def __lt__(self,other):
        return self.sum() > other.sum()

class Reviewer(Mentor):    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
 
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
some_student1 = Student('Ruoy1', 'Eman1', 'your_gender')
some_student1.courses_in_progress += ['Python']
some_student1.courses_in_progress += ['Git']
some_student1.finished_courses += ['Введение в программирование']
some_student2 = Student('Ruoy2', 'Eman2', 'your_gender')
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Git']
some_student2.finished_courses += ['Введение в программирование']

 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer1 = Lecturer('Some1', 'Buddy1')
some_lecturer1.courses_attached += ['Python']
 
some_reviewer.rate_hw(some_student, 'Python', 1)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)  
     
some_student.rate_hw(some_lecturer, 'Python', 44)
some_student.rate_hw(some_lecturer, 'Python', 3)
some_student.rate_hw(some_lecturer, 'Python', 10)   
some_student.rate_hw(some_lecturer1, 'Python', 3)
some_student.rate_hw(some_lecturer1, 'Python', 4)
some_student.rate_hw(some_lecturer1, 'Python', 1) 
# Задание № 3
# 1. Перегрузите магический метод __str__ у всех классов
print(some_reviewer)
print(some_lecturer)
print(some_lecturer1)
print(some_student)
# 2. Реализуйте возможность сравнивать
print(some_lecturer < some_lecturer1)

print(Lecturer.__call__)


