ALL_COURSES = [
    "Data Science",
    "Software Engineering",
    "DevOPS",
    "Cyber Security",
    "AI Engineering",
    "High School Bootcamp",
    "Product Design",
    "Data Analytics",
    "Data Analytics for HR Professionals",
]


class Student:
    student_count = 0
    all_students = []

    def __init__(
        self, first_name, last_name, age, gender, student_id, course, instructor
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student_id = student_id
        self.course = course
        self.instructor = instructor
        Student.student_count += 1
        Student.all_students.append(self)

    # getter method for the course
    @property
    def course(self):
        return self._course

    # setter method
    @course.setter
    def course(self, course):
       
        if course in ALL_COURSES:
            self._course = course
        else:
            raise ValueError(f"Course '{course}' is not in the allowed courses list.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 18:
            self._age = age
        else:
            raise ValueError("Age must be 18 or older to enroll.")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        valid_genders = ["Male", "Female"]
        if gender in valid_genders:
            self._gender = gender
        else:
            raise ValueError(f"Gender must be one of {valid_genders}.")


    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    @classmethod
    def total_students(cls):
        return f"The total number of students is: {cls.student_count}"

    @classmethod
    def student_list(cls):
        names_array = [
            f"{student.first_name} {student.last_name}" for student in cls.all_students
        ]
        return names_array

    @classmethod
    def student_list_2(cls):
        return [student.fullname() for student in cls.all_students]

    @staticmethod
    def reverse_name(first_name, last_name):
        return f"{last_name} {first_name}"


# Student Objects
student1 = Student(
    "Bradley", "Murimi", 40, "Male", "MSS-1234", "Software Engineering", "Fainus Mudahe"
)
student2 = Student(
    "Mariam",
    "Rashid",
    20,
    "Female",
    "MSS-1428",
    "Software Engineering",
    "Julius Mutindwa",
)
student3 = Student(
    "Fredrick",
    "Rangara",
    50,
    "Male",
    "MSS-1480",
    "Software Engineering",
    "Julius Mutindwa",
)
# student4 = Student(
#     "Adonis",
#     "Pierre",
#     30,
#     "Male",
#     "MSS-3445",
#     "Bio Tech",
#     "Julius Mutindwa",
# )


print(f"Student age: {student1.age}")
print(f"Student gender: {student3.gender}")
print(f"Student course: {student1.course}")
