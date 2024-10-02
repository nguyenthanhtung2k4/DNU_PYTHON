# Tạo một tuple với các thông tin về sinh viên
student_info = ("John", 21, "Computer Science")

# Truy cập phần tử
name = student_info[0]
age = student_info[1]
major = student_info[2]

print(f"Name: {name}, Age: {age}, Major: {major}")

# Sử dụng len()
print("Length of the tuple:", len(student_info))  # Kết quả: 3

# Sử dụng count() và index()
numbers = (10, 20, 20, 30, 40)
print("Số lần xuất hiện của 20:", numbers.count(20))  # Kết quả: 2
print("Vị trí của 30:", numbers.index(30))  # Kết quả: 3

# Sử dụng min() và max()
print("Min:", min(numbers))  # Kết quả: 10
print("Max:", max(numbers))  # Kết quả: 40

# Chuyển đổi từ list sang tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("Tuple từ list:", my_tuple)
