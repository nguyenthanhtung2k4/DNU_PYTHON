def bai1():
  nhap=int(input('Nhap: '));
  if 8>nhap>0:
    ngay=['thu2','thu3','thu4','thu5','thu6','thu7','chu nhat']
    print(f'Ngay hom nay la: {ngay[nhap-1]}')
  else:
    print('error')
    
def bai7():
  mau1=input('Mau1: ').lower()
  mau2=input('Mau2: ').lower()
  if(mau1=="đỏ" and mau2=='xanh dương'):
    print('tím')
  elif(mau1=='đỏ' and mau2== 'vàng'):
    print('cam')
  elif(mau1=='xanh dương' and mau2== 'vàng'):
    print('Xanh lá')
  else:
    print('Lỗi trọn màu!')

def bai9():
  nhap=int(input('Nhap: '))
  for x in range(36):
    if nhap ==0:
      print('xanh lá cây')
      break
    elif 11<= nhap <=18:
      if(nhap%2==0):
        print('do')
        break
      else:
        print('den')
        break
    elif 19<= nhap <=28:
      if(nhap%2==0):
        print('den')
        break
      else:
        print('do')
        break
    elif 29<= nhap <=36:
      if(nhap%2==0):
        print('do')
        break
      else:
        print('den')
        break
    else:
      print('Loi nguoi  dung!')
        
        
bai9()