class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

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


class Lecturer(Mentor):
    grades = {}
    
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
 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
 
some_reviewer.rate_hw(some_student, 'Python', 1)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)  
     
some_student.rate_hw(some_lecturer, 'Python', 8)
some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(some_lecturer, 'Python', 10)   
# Задание № 3
# 1. Перегрузите магический метод __str__ у всех классов
print(some_reviewer)
print(some_lecturer)
print(some_student)
# 2. Реализуйте возможность сравнивать
print(some_lecturer < some_student)