import math
from pystyle import System
def chanle():
     so=int(input('Nhập số: '))
     if(so%2==0 ):
          print(f"Số {so} là chẵn")
     else:
          print(f"Số {so} là lẻ")

def  chia_bay():
     so=int(input('Nhập số: '))
     if(so%2==1 and so%7==0):
          print(f"Số {so} là lẻ chia hết cho bảy")
     elif(so%2==1):
          print(f"Số {so} là lẻ")
     else:
          print(f"Số {so} Không chia hết cho  bảy")

def pt1():
     a=float(input('Nhập a:'))
     b=float(input('Nhập b:'))
     if(a!=0):
          x=-b/a
          print(f"Phương trình có nghiệm duy nhất:\n X={x}")
     else:
          print(f"Phương trình không phải là bậc nhất! ")


def pt2():
     a=float(input('Nhập a:'))
     b=float(input('Nhập b:'))
     c=float(input('Nhập c:'))
     Den=(b*b)-4*a*c
     if(a!=0):
          if(Den>0):
               x1=(-b+ math.sqrt(Den))/(2*a)
               x2=(-b-math.sqrt(Den))/(2*a)
               print(f'Phuon trinh 2 nghiem:\n X1={x1}\n X2={x2}')
          elif(Den==0):
               x3  = -b/2*a
               print(f"Phương trình ngiệm kép:\n X={x3}")
          else:
               print(f"Phương trình vô số nghiệm.")     
     else:
          print(f"Phương trình không phải bậc hai! ")
               
a='''

[1]Chắn lẻ
[2]Chẵn lẻ và chia 7
[3]Phương trình bậc nhất
[4]Phương trình bậc 2
'''
System.Clear();
while(True):
     print(f'\n===================================\nVui lòng lựa chọn\n{a}')
     nhap=int(input('Nhập: '))
     if(nhap==1):
          System.Clear();
          print('Tính chẵn lẻ\n\n')
          chanle();
     elif(nhap==2):
          System.Clear();
          print('Tính chẵn lẻ chia hết cho bảy\n\n')
          chia_bay();
     elif(nhap==3):
          System.Clear();
          print('Bậc nhất\n\n')
          pt1();
     elif(nhap==4):
          System.Clear();
          print('Bậc hai\n\n')
          pt2();
     else:
          System.Clear();
          print('kết thúc chương trình!')
          exit();