# print(f"Ngay:\t\tDanSO:")
# dan=2
# for x in range(1,11):
#      print(f"{x}\t\t{dan:.2f}")
#      dan+=dan*0.3



# tong=0;tb=0;i=1;thang=12
# nam=int(input("Nam: "))
# soNam=nam
# while(nam>0):
#      print(f'Luong mua Nam {i}')
#      for m in range(1,13):
#           rain=int(input(f'Nhap luong mua thang {m}: '))
#           tong+=rain
#      i+=1;nam-=1
# tb=tong/(soNam * thang)
# print(f"Tong mua: {tong}")
# print(f"TB mua: {tb}")

# ngansach=float(input('Ngan Sach: '))
# tien=0;i=1
# while True:
#      chiphi=float(input('Chi phi {i}: '))
#      if(chiphi==0):break
#      tien+=ngansach-chiphi
#      i+=1
# chi=tien-ngansach
# if(tien>ngansach):
#      print(f'\n\nVuot ngan sach')
#      print(f'So Tien vuot la: {chi}\n')
# elif(ngansach==tien):
#      print('Chi phi == ngan sach\n')
# else:
#      print('Duoi ngan sach')


# nam=5;phi=8000;tang=0.03
# for x in range(1,nam+1):
#      print(f"Nam {x} : {phi:.2f}")
#      phi+=phi*tang

total = 0

for i in range(1, 31):

    total += 1/i

print(round(total, 2))
