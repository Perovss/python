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
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and\
                   course in self.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
                return f'Оценка лектору добавлена: {lecturer.surname} {lecturer.name}, ' \
                       f'курс "{course}" оценка - {grade}.'
            else:
                return f'ОШИБКА: студент {self.surname}{" " if course in self.courses_in_progress else " не "}' \
                       f'учится на данном курсе, a лектор {lecturer.surname}' \
                       f'{" " if course in lecturer.courses_attached else " не "}преподает указанный курс.'
        else:
            return f'ОШИБКА: выставляемая лектору {lecturer.surname} оценка - {grade} ' \
                   f'должна быть в пределах от 0 до 10!'

    def average_grade(self):
        sum_grades=int()
        index = 0
        for course in self.grades.values():
            for grade in course:
                sum_grades += grade
                index +=1
        res = round(sum_grades/index, 1)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.average_grade()}\
              \nКурсы обучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res
    
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        sum_grades=int()
        index = 0
        for course in self.grades.values():
            for grade in course:
                sum_grades += grade
                index +=1
        res = round(sum_grades/index, 1)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_grade()}'
        return res
        
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

class Reviewer(Mentor):    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return f'Оценка лектору добавлена: {student.surname} {student.name}, ' \
                   f'курс "{course}" оценка - {grade}.'
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
   
# Ввод исходных данных студентов
students = [Student('Вася', 'Петров', 'М'),
            Student('Саша', 'Белкин', 'М'),
            Student('Карина', 'Соскина', 'Ж')]
students[0].courses_in_progress += ['Python']
students[0].finished_courses += ['GitHub']
students[1].courses_in_progress += ['GitHub']
students[2].courses_in_progress += ['GitHub', 'Python']
students[2].finished_courses += ['English', 'Flask']

# Исходные данные лекторов
lecturers = [Lecturer('Кирилл', 'Григорьев'),
             Lecturer('Петр', 'Пивоваров')]
lecturers[0].courses_attached += ['Python', 'GitHub']
lecturers[1].courses_attached += ['GitHub']

# Исходные данные проверяющих
reviewers = [Reviewer('Константин', 'Гусейкин'),
             Reviewer('Владислав', 'Мечет')]
reviewers[0].courses_attached += ['Python', 'GitHub']
reviewers[1].courses_attached += ['English', 'GitHub']


# Выставление оценок студентам
print('ОЦЕНКИ СТУДЕНТАМ ЗА ДОМАШНИЕ ЗАДАНИЯ:')
print(reviewers[0].rate_hw(students[0], 'Python', 5))
print(reviewers[0].rate_hw(students[0], 'Python', 4))
print(reviewers[0].rate_hw(students[0], 'Python', 3))
print(reviewers[1].rate_hw(students[1], 'GitHub', 8))
print(reviewers[1].rate_hw(students[1], 'GitHub', 3))
print(reviewers[1].rate_hw(students[1], 'GitHub', 2))
print(reviewers[0].rate_hw(students[2], 'GitHub', 4))
print(reviewers[0].rate_hw(students[2], 'Python', 3))
print(reviewers[1].rate_hw(students[2], 'GitHub', 5))

# Выставление оценок лекторам
print('\nОЦЕНКИ ЛЕКТОРАМ СТУДЕНТАМИ:')
print(students[0].rate_hw(lecturers[0], 'Python', 9))
print(students[1].rate_hw(lecturers[0], 'Python', 7))
print(students[2].rate_hw(lecturers[0], 'Python', 10))
print(students[2].rate_hw(lecturers[1], 'GitHub', 7))
print(students[2].rate_hw(lecturers[0], 'GitHub', 10))
print(students[1].rate_hw(lecturers[1], 'GitHub', 20))

print('\nСПИСОК СТУДЕНТОВ:')
print(students[0])
print(students[1])
print(students[2])
print('\nСПИСОК ЛЕКТОРОВ:')
print(lecturers[0])
print(lecturers[1])
print('\nСПИСОК ПРОВЕРЯЮЩИХ:')
print(reviewers[0])
print(reviewers[1])

# Проверка работоспособности операторов < >
print('\n --- ПРОВЕРКА ОПЕРАТОРОВ СРАВНЕНИЯ С ОПИСАННЫМИ КЛАССАМИ ---')
print(students[0] < students[1])
print(lecturers[0] < lecturers[1])

