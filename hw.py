# ніби то шаблон
import datetime

class Student:
    def __init__(self,name, surname, birthdate, height=160):
        # ошибка если имя не строка
        if (type(name) != str):
            raise TypeError(f"Name must be str. Not a '{type(name)}'")
        # помилка, якщо surname не є str
        if (type(surname) != str):
            raise TypeError(f"Surname must be str. Not a '{type(surname)}'")
        # помилка, якщо birthdate не є str
        if(type(birthdate) != str):
            raise TypeError(f"Birthdate must be str. Not a '{type(birthdate)}' ")
        try:
            self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
        except ValueError:
            raise ValueError(f"Invalid birthdate format. Expected 'dd.mm.yyyy' but got '{birthdate}'")

        # помилка, якщо birthdate більший ніж поточний день

        if self.birthdate > datetime.datetime.now():
            raise ValueError(f"Birthdate cannot be in the future. Got: {birthdate}")

        # помилка, якщо height не є int/float
        if not isinstance(height, (int, float)):
            raise TypeError(f"Height must be int or float. Not a '{type(height)}'")
        # помилка, якщо height менший або дорівнює нулю
        if height <= 0:
            raise ValueError(f"Height must be a positive number. Got: {height}")



        self.name = name
        self.surname = surname
        # 25.10.2006
        self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
        self.height = height
        print(f"I am {self.name}")

    def printStudent(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Birthdate: {self.birthdate.strftime('%d.%m.%Y')}")
        print(f"Height: {self.height}")

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nBirthdate: {self.birthdate.strftime('%d.%m.%Y')}\nHeight: {self.height}\n"

    def __int__(self):
        age = (datetime.datetime.now()-self.birthdate)
        return int(age.days / 365)



# створення об'єкта
first_student = Student('vlad', 'karlinskij', '25.10.2006',186)

first_student.printStudent()

print('------------------------------')

# 1. Неправильний тип для name (не рядок)
try:
    student1 = Student(123, 'Karlinskij', '25.10.2006', 180)
except Exception as e:
    print(f"Error: {e}")

# 2. Неправильний тип для surname (не рядок)
try:
    student2 = Student('Vlad', 123, '25.10.2006', 180)
except Exception as e:
    print(f"Error: {e}")

# 3. Неправильний тип для birthdate (не рядок)
try:
    student3 = Student('Vlad', 'Karlinskij', 25102006, 180)
except Exception as e:
    print(f"Error: {e}")

# 5. Неправильний тип для height (не число)
try:
    student5 = Student('Vlad', 'Karlinskij', '25.10.2006', 'tall')
except Exception as e:
    print(f"Error: {e}")

# 6. Нульовий або від'ємний зріст
try:
    student6 = Student('Vlad', 'Karlinskij', '25.10.2006', 0)
except Exception as e:
    print(f"Error: {e}")

try:
    student7 = Student('Vlad', 'Karlinskij', '25.10.2006', -170)
except Exception as e:
    print(f"Error: {e}")