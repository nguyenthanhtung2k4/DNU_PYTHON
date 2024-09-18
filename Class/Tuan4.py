import os,sys
from pystyle import System
def nhap_(type,text):
     while True:
               try:
                    nhap = type(input(text).upper())
                    break;
               except ValueError:
                    nhap='Nhap lai so:'
     return nhap          
def bai1():
     tuan = [];tong = 0
     for x in range(2, 9, 1):
          if x == 8:
            x = 'Chủ Nhật'
          while True:
               try:
                    nhap = float(input(f'Nhập doanh thu ngày {x}: '))
                    break;
               except ValueError:
                    print('Nhap lai so:')
          tuan.append(nhap)
          tong += nhap
     print("Doan thu trong tuan la: \n\n")
     for i,tien in enumerate(tuan):
        x = i - 2
        if i == 8:
            i = 'Chủ Nhật'
        print(f'\tNgày {i} là: {tien}')

     print(f'Tổng là: {tong}')


def bai3():
     rain=[];tong=0;lon=0;nho=0
     for x in range(1,13,1):
          input=(f'Luong mua thang {x}: ')
          nhap=nhap_(float,input)
          rain.append(nhap);
          tong+=nhap;
     print(rain)
     for i,thang in enumerate(rain):
          n=min(rain)
          l=max(rain)
          if n==thang:
               nho=i
          if l==thang:
               lon=i
          
     print(f'Tong mua: {tong:.2f}\nTb mua: {tong/12}\nThang cao nhat: {lon}\nThang thap nhat: {nho}')
          
def bai5():
     file = "D:\CODE\DNU_PYTHON\Class\charge_accounts.txt"
     nhap=input('Nhap so can tim: ')
     with open(file, 'r') as f:
          for line in f:
               if nhap in line:
                    print(True)
                    break
          else:
               print(False)
def bai7():
     dung=0;a='truot';sai=[];sv=[]
     an=['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
     tong=len(an)
     # an=['A','C','A','A']
     file = "D:\CODE\DNU_PYTHON\Class\diemNhap.txt"
     # with open(file,'w+') as f:
          # for x in range(1,len(an),1):
          #      i=0
          #      text=f'Nhap dap an {x}: '
          #      nhap=nhap_(str,text)
          #      f.write(f'{nhap}\n')
          #      if nhap==an[i]:
          #           dung+=1
                    
          # f.close()
     with open(file,'r') as r:
          for i in r:
               sv.append(i.strip().upper())
          r.close()
          if tong> len(sv):
               
               for i  in range(tong-len(sv)):
                    sv.append(None)
          for x,an in enumerate(an):

                    if an== sv[x]:
                         dung+=1
                    else:
                         sai.append(x)
     if dung>=15:
          a='do'
     print(f'Sv {a}\nTong dung: {dung}\nTong Sai: {tong-dung}')
     print(f'\n\tCau sai: \n')
     for x in sai:
          an=['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A'] 
          print(f'Cau: {x+1} \n\tDapSai: {sv[x]} | DapDung: {an[19]}')

def bai8():
     file2="D:\CODE\DNU_PYTHON\Class\BoyNames.txt"
     file="D:\CODE\DNU_PYTHON\Class\GirlNames.txt"
     def name(file,nhap):
          with open(file,'r') as f:
               a=False
               for name in  f:
                    name=name.upper()
                    if nhap in name:
                         a="popular"
               f.close()
          return a
             
     nhapName=input("NHap Name: ").upper()
     a=name(file,nhapName)
     if(a):
          print(f'Name {nhapName} ==> {a} Girl')
     else:
          a=name(file2,nhapName)
          if(a==False):
               print(f'Name {nhapName} ==>Not popolar')
          else:
               print(f'Name {nhapName} ==> {a} Boy')
     # else:
            
def bai9():
     # /// Cach1 
     print(f'\n\nCach1\n')
     nam = 0
     nho = float('inf') # vo cung lon 
     lon = float('-inf') #vo cung nho
     tong = 0

     file = r"D:\CODE\DNU_PYTHON\Class\USPopulation.txt"
     with open(file, 'r') as f:
          for line in f:
               data = int(line.strip())
               nho = min(nho, data)
               lon = max(lon, data)
               tong += data
               nam += 1

     trung_binh = tong/nam
     print(f"""Mức tăng trung bình trong {nam} năm: {trung_binh:.2f}
Mức tăng cao nhất là: {lon}
Mức tăng thấp nhất là: {nho}""")
     # /// Cach2
     print('\n\n\n Cach2')
     tong=0;arr=[];m=0;M=0;nam=0
     with open(file,'r') as file:
          for file in  file:
               data=int(file.strip())
               tong+=data
               m=min(m,data)
               M=max(M,data)
               nam+=1
     trung_binh = tong/nam
     print(f"""Mức tăng trung bình trong {nam} năm: {trung_binh:.2f}
Mức tăng cao nhất là: {lon}
Mức tăng thấp nhất là: {nho}""")
          
               
def maTrix():
     maTran=[]
     for x in range(3): 
          row=[]
          for i in range(3): 
               System.Clear()
               print(f'Col[{x+1}]]  - Row[{i+1}]\n\n')
               num=nhap_(int,'Nhap number:')
               row.append(num)
          maTran.append(row)
     return maTran
def bai11():
     maTran=maTrix()
     sumRow=sum(maTran[0])
     for ma in maTran:
          if sumRow != sum(ma):
               return False
     
          
     # for x in range(3):
     #      for i in range(3):
     #           print(f'|{maTran[x][i]}| ',end='')
     #      print('\n',end='')
     
# https://gemini.google.com/app/4fd79a7643d5e9d9?hl=vi   
bai11()