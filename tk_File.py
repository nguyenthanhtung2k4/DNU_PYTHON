import os

# kiem tra file
if os.path.exists('tung.txt'):
     print('file ton tai')
else:
     print('file khong ton tai')

# doc file:
with open('tung.text','r') as f:
     data=f.read()
     f.close()
print(data)

# viet file:
with open('tung.text','r') as f:
     f.write('thanhtung')
     f.close()  

#  lọc dữ liệu file:
def bai5():
    file = "D:\CODE\DNU_PYTHON\Class\charge_accounts.txt"
    nhap=input('Nhap so can tim: ')
    with open(file, 'r') as f:
        for line in f:
            if nhap in line: # tim kiem ki  tu trong file
                print(True)
                break
        else:
            print(False)

bai5()