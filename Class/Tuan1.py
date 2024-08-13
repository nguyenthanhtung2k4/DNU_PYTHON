#  B1
def bai1():
     print("Họ và tên: Nguyễn Thanh Tùng\nSĐT: 095332211\nChuyên Ngàng: Công Nghệ Thông Tin")

# b2
# tien=float(input("Nhập doanh số:"))
# doanhSo=(tien*0.23)
# print(f"Lợi nhuận là: {doanhSo}")


# b3
# pound=float(input("Nhập Pound:"))
# kg=(pound*0.454)
# print(f"Kilogam là: {kg}")

# b4
# Tong =0;
# for x in range(5):
#      Tien=float(input(f"So tien sp{x+1}: "))
#      Tong+=Tien;
# print(f"Tong so tien: {Tong}")
# thue=Tong*0.07;
# print(f"Thuế: {thue}")
# print(f"Tổng+Thuế: {Tong+thue}")


# b5
def bai5():
     h=[6,10,15]
     for  hour in h:
          print(f"Khoảng cách {hour} giờ là:{70*hour}")


# b6
# Tien=float(input(f"Nhập số tiền mua hàng: "))
# lan=float(input(f"Nhập số lần buy: "))
# thue=Tien*0.05
# tong=thue+Tien
# print(f'Tổng tiền: {tong}')
# print(f'Số tiền mỗi lần: {tong/lan}')


#  b7
# dam=float(input(f"Nhập dặm: "))
# gallo=float(input(f"Nhập gallo: "))
# print(f'MPG là: {round(dam/gallo,2)}')

#  b8
def bai8():
     tien=float(input(f"Số tiền thanh toán: "))
     print(f"Tip: {round(tien*0.18,2)}")
     print(f"Thuế: {round(tien*0.07,2)}")
     print(f"Tổng tiền: {tien+(tien*0.18)+(tien*0.07)}")


# b9
def bai11():
     nam=int(input('Nam: '))
     nu=int(input('Nu: '))
     tong=nam+nu
     print(f'Nam chiem {(round((nam/tong)*100,2))}%')
     print(f'Nu chiem {(round((nu/tong)*100,2))}%')


# b14
def bai14():
     goc=float(input("Số tiền gốc ban đầu: "))
     lai=int(input("Lãi suất hàng năm: "))
     n=float(input(" Số lần lãi suất được cộng vào mỗi năm: "))
     nam=float(input(" Số năm mà tài khoản sẽ để kiếm lãi."))
     # innam=int(input("So nam chi dinh: "))
     congThuc=goc(1+(lai/100)/n)**(n*nam)
     print(f"Số năm được chỉ định: {congThuc}")
bai14()
# tren ban 1
# a=int(input('Nhập a: '))
# b=int(input('Nhập b: '))
# mu=a**b
# print('KQ: ',mu)

# tren ban 2
# sp=int(input('Sản phẩm: '))
# tong=0
# arr=[]
# for x in range(sp):
#      gia=int(input(f'--------------------------\nGiá Sản phẩm {x+1}: '))
#      thue=gia*0.1
#      tong+=gia+thue
#      arr.append(gia*thue)
# for i, gia_thue in enumerate(arr):
#     print(f'Sản phẩm {i} giá thuế là: {gia_thue}')

# print(f'\n--------------------------\nTổng số tiền là: {tong}')


