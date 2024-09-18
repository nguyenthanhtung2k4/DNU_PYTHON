# //////////////////////////////////////VD1 :  SỬ DỤNG OPP

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} generic sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # Gọi phương thức make_sound() của lớp cha
        print("Woof!")

dog=Dog('cho')
print(dog.make_sound())


# ////////////////////////////////////// VD: SỬ DỤNG OPP:

class A:
    def __init__(self):
        print("A is initialized")

class B:
    def __init__(self):
        print("B is initialized")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C is initialized")

# Tạo đối tượng C
c = C()



# //////////////////////////////////////VD 3 : SỬ DỤNG  OPP  NÂNG CAO:

class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
    def get_person(self):
        return f"Ten sinh vien la: {self.name} | Phone la: {self.phone}"

class Employee(Person):
    def __init__(self, name, age, address, phone, salary):
        super().__init__(name, age, address, phone)
        self.salary = salary

class Student(Person):
    def __init__(self, name, age, address, phone, major, year):
        super().__init__(name, age, address, phone)
        self.major = major
        self.year = year

# Tạo đối tượng sinh viên
student = Student("Nguyễn Văn A", 20, "Hà Nội", "0987654321", "Công nghệ thông tin", 2023)

# In thông tin sinh viên
print("Tên:", student.name)
print("Tuổi:", student.age)
print("Địa chỉ:", student.address)
print("Số điện thoại:", student.phone)
print("Ngành học:", student.major)
print("Năm nhập học:", student.year)
print('\nStudent: ',student.get_person())