class Student:
    def __init__(self, name, surname, gender):
        self.name = name  # Имя студента
        self.surname = surname  # Фамилия студента
        self.gender = gender  # Пол студента
        self.finished_courses = []  # Список завершенных курсов
        self.courses_in_progress = []  # Список курсов, на которых студент обучается в данный момент
        self.grades = {}  # Оценки студента

class Mentor:
    def __init__(self, name, surname):
        self.name = name  # Имя преподавателя
        self.surname = surname  # Фамилия преподавателя
        self.courses_attached = []  # Список курсов, которые преподаватель ведет

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            # Проверяем, что переданный объект является экземпляром класса Student,
            # курс преподавателя прикреплен к студенту и студент обучается на этом курсе
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}  # Оценки за лекции

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            # Проверяем, что переданный объект является экземпляром класса Student,
            # курс проверяющего прикреплен к студенту и студент обучается на этом курсе
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')  # Создание объекта студента
best_student.courses_in_progress += ['Python']  # Добавление курса в список курсов студента

cool_mentor = Mentor('Some', 'Buddy')  # Создание объекта преподавателя
cool_mentor.courses_attached += ['Python']  # Добавление курса в список курсов преподавателя

cool_mentor.rate_hw(best_student, 'Python', 10)  # Выставление оценки студенту
cool_mentor.rate_hw(best_student, 'Python', 10)  # Выставление оценки студенту
cool_mentor.rate_hw(best_student, 'Python', 10)  # Выставление оценки студенту

print(best_student.grades)
