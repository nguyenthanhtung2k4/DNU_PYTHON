def bai3():
     tien=int(input('Nhap so tien: '))
     chi=int(input('So tien chi: '))
     while chi!= 0:
          chi=int(input('So tien chi: '))
          tien-=chi
     if tien>=0:
          print('Duoi  ngan sach!')
     else:
          print('Vuot qua danh sach!')
          
def bai5():
     nam=int(input('Nhap so nam: '))
     tong=0
     for x  in range(1,nam+1):
          print('Du lieu nam ',x)
          for i in range(1,13):
               data=float(input(f'Nhap luong mua thang {i}: '))
               tong+=data
     print(f'Tong luong mua: {tong}\nLuong mua trung binh: {tong/(nam*12)}\n')

def bai10():
     phi=8000;
     for x in  range(1,6):
          print(f'Nam {x}\nHoc phi: {phi}')
          phi+=phi*0.03

def bai13():
     sv=2 
     for x in range( 1,11):
          print(f'{x}\t\t{sv}')
          sv+=sv*0.3
          
def bai14():
     for x in range(7,0,-1):
          print()
          for i in range(x,0,-1):
               print('*',end='')
     for x in range(7):
          print()
          for i in range(x+1,0,-1):
               print('*',end='')
          
bai14()