class Account:
    def __init__(self, balance):
        self.__balance = balance  # Thuộc tính private để lưu số dư

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Gửi tiền thành công!")
        else:
            print("Số tiền gửi phải lớn hơn 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Rút tiền thành công!")
        else:
            print("Số tiền rút không hợp lệ.")
            
account = Account(1000)  # Tạo một tài khoản với số dư ban đầu là 1000
print(account.get_balance())  # In ra số dư hiện tại
account.deposit(500)  # Gửi thêm 500 vào tài khoản
account.withdraw(200)  # Rút 200 khỏi tài khoản
print(account.get_balance())  # In ra số dư mới




#  Cách truy vấn và thay đôi  Private  trong python  ở bên ngoài  Class
# account = Account(1000)
account._Account__balance = 2000  # Truy cập trực tiếp vào thuộc tính private
print(account.get_balance())  # Sẽ in ra 2000