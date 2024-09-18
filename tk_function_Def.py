# ///////////////////////////////// def() khong chuyen tham so
def tung():
     print("khong tham so")
     
     
# def() chuyen tham so
def tung2(a,b):
     return a+b


# ///////////////////////////////////// def() khi khong biet co bao nhieu tham so ta co the kiem tra
def tinh_tong(*so):
  tong = 0
  for so_i in so:
     tong += so_i
  return tong

# Gọi hàm với các số lượng đối số khác nhau
ket_qua1 = tinh_tong(1, 2, 3)
ket_qua2 = tinh_tong(5, 10, 15, 20)
print(ket_qua1)  # Output: 6
print(ket_qua2)  # Output: 50

# ///////////////////////////////////// def() tra ve cung luc nhieu dinh dang
def tung2(i):
     return i,'tung',2.1
print(tung2(2))

# ///////////////////////////////////////// lambda thay the cho  def()
tung=lambda x:x*2
print(tung(2))
#  vd2  kiem tra chan le
nhap=int (input('Nhap: '))
so=lambda x:True if(x%2==0) else False
print(so(nhap))