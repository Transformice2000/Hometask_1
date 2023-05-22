class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self, course):
        if course in self.grades:
            course_grades = self.grades[course]
            return sum(course_grades) / len(course_grades)
        else:
            return 0

    def __str__(self):
        avg_grade = sum(self.average_grade(course) for course in self.grades.keys()) / len(self.grades)
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def average_grade(self, course):
        if course in self.lecture_grades:
            lecture_grades = self.lecture_grades[course]
            return sum(lecture_grades) / len(lecture_grades)
        else:
            return 0

    def __str__(self):
        avg_grade = sum(self.average_grade(course) for course in self.lecture_grades.keys()) / len(self.lecture_grades)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"


def calculate_average_student_grade(students, course):
    total_grade = sum(student.average_grade(course) for student in students)
    average_grade = total_grade / len(students)
    return average_grade


def calculate_average_lecture_grade(lecturers, course):
    total_grade = sum(lecturer.average_grade(course) for lecturer in lecturers)
    average_grade = total_grade / len(lecturers)
    return average_grade


# Пример использования

# Создаем список студентов и добавляем оценки
students = [
    Student('Ruoy', 'Eman', 'your_gender'),
    # Другие студенты...
]

# Создаем список лекторов и добавляем оценки за лекции
lecturers = [
    Lecturer('Some', 'Buddy'),
    # Другие лекторы...
]

# Рассчитываем среднюю оценку за домашние задания по всем студентам в рамках курса 'Python'
course_name = 'Python'
average_student_grade = calculate_average_student_grade(students, course_name)
print(f"Средняя оценка за домашние задания по курсу '{course_name}': {average_student_grade:.1f}")

# Рассчитываем среднюю оценку за лекции всех лекторов в рамках курса 'Python'
average_lecture_grade = calculate_average_lecture_grade(lecturers, course_name)
print(f"Средняя оценка за лекции по курсу '{course_name}': {average_lecture_grade:.1f}")
