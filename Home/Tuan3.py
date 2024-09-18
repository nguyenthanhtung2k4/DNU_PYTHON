def bai1():
     print('Chuyển đổi Kilomet --> dặm')
     km=float(input('Nhập Km: '))
     dam=km*0.6214
     print(f'Dặm: {dam:.2f}')
     
     
     
def bai12():
     a=int(input('input a:'))
     b=int(input('input b:'))
     if(a>b):
          print(f'Giá trị lớn nhất là: {a}')
     else:
          print(f'Giá trị lớn nhất là: {b}')
def calc_average():
     tb=0
     for x in range(5):
          diem=float(input(f'Diem {x}'))
          tb+=diem
     return tb/5
def determine_grade():
     tb =calc_average()
     print(f'tb: {tb}')
     ob={
          90:'A' ,
          80:'B',
          70:'C',
          60:'D',
          0:'F',
     }
     for x in ob:
          if 0<=tb<=60:
               return ob[0]
          
          if(x<= tb<=x+10):
                   return ob[x]
          
     else:
               return 'Diem khong dat tieu chuan!'
              
     
def bai15():
     print(determine_grade())
     
     
def bai19():
     P=float(input('Tien hien co: '))
     i=float(input('Lai hang thang: '))
     t=int(input('So thang: '))
     F=P*(1+(i/100))**t
     print(f'Gia tri tuong lai la: {F:.2f}')
