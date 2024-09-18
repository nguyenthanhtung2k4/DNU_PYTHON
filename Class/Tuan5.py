def bai1():
     file=r"D:\CODE\DNU_PYTHON\Class\Numbers.txt"
     with open (file,'r') as file:
          read=file.read()
          file.close()
          print(read)
     
def bai2():
     nhap=input('Nhap file:')
     nhap=(f"D:\CODE\DNU_PYTHON\Class\{nhap}")
     with open (nhap,'r') as file:
          re=file.readlines()
          dem=0
          for file in re:
               if dem==5:
                    break;
               print(file.strip())
               dem+=1
def bai4():
     file=(r"D:\CODE\DNU_PYTHON\Class\Names.txt")
     with open (file,'r') as file:
          re=file.readlines()
          dem=0
          for file in re:
               # print(file.strip())
               dem+=1
     print('So luong name: ',dem)     

def bai5():
     tong=0
     file=(r"D:\CODE\DNU_PYTHON\Class\Numbers.txt")
     with open (file,'r') as file:
          for tung in file:
               # print(tung.strip())
               num=tung.strip()             
               num=int(num)
               tong+=num
     print(tong)


def bai9():
     pass

def bai10():
     nhap=int(input('Nhap so doi: '))
     a=0;arr=[]
     with open('golf.txt','w')as f:
          while a<nhap: 
               a+=1
               while True:
                    try:
                         Ten=input('Ten : ')
                         diem=int(input('Nhap diem: '))
                         break
                    except ValueError:
                         print('Nhap lai !')
               f.write(f'{Ten}\n{diem}\n')
     with open('golf.txt','r',encoding='utf-8')as r:
          for data in r:
               arr.append(data.strip())
     # print(arr)
     for i in  range(0,len(arr),2):
          print(f'Diem: {arr[i]} | Ten: {arr[i+1]}')

bai10()

def bai11():
     name=input('Nhap Name: ')
     mota=input('Nhap Mota: ')
     file=r"D:\CODE\DNU_PYTHON\Class\bai9.html"
     with open(file,'w+') as file:
          html=f'''
<html> 
     <head> 
     </head> 
     <body> 
          <center> 
               <h1>{name}</h1> 
          </center> 
          <hr />{mota}
          <hr />
     </body>
</html>
          '''
          file.write(html)
          file.close()
     print('Sucsse')

def bai12():
     pass