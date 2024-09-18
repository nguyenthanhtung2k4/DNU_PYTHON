# def tron_mau(mau1, mau2):
#   """Hàm trộn hai màu cơ bản

#   Args:
#     mau1: Màu cơ bản thứ nhất.
#     mau2: Màu cơ bản thứ hai.

#   Returns:
#     Màu kết quả sau khi trộn.
#   """

#   mau_ket_qua = {
#     ("đỏ", "xanh dương"): "tím",
#     ("đỏ", "vàng"): "cam",
#     ("xanh dương", "vàng"): "xanh lá cây",
#     ("vàng", "đỏ"): "cam",
#     ("xanh dương", "đỏ"): "tím",
#     ("vàng", "xanh dương"): "xanh lá cây"
#   }

#   mau1 = mau1.lower()
#   mau2 = mau2.lower()

#   if (mau1, mau2) in mau_ket_qua:
#     return mau_ket_qua[(mau1, mau2)]
#   else:
#     return "Màu nhập vào không hợp lệ"

# # Nhập liệu từ người dùng
# mau1 = input("Nhập màu thứ nhất: ")
# mau2 = input("Nhập màu thứ hai: ")

# # Gọi hàm trộn màu và in kết quả
# ket_qua = tron_mau(mau1, mau2)
# print("Màu kết quả:", ket_qua)



# tung={
#     ( 'tung','thanh'):'mau',
#      'class':'tung',
#      'cntt':'17-15'
# }
# so={
#      1:'mot',
#      2:'hia',
#      10:'muoit10'
# }
# print(tung['tung','thanh'],'\n\n')
# for  ob in  so:
#      print(ob['1'])






# nhap=23
# color_map = {
#         0: "xanh lá cây",
#         11: "đỏ" if nhap % 2 == 0 else "đen",
#         19: "đen" if nhap % 2 == 0 else "đỏ",
#         29: "đỏ" if nhap % 2 == 0 else "đen"
#      }
# for start_range in color_map:
#      print(start_range)
#      print(start_range <= nhap <= start_range + 7)
#      print(color_map[start_range])
#      if start_range <= nhap <= start_range + 7:
#           print(color_map[start_range])
# print("Lỗi người dùng!")


# arr=['0','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']

# nhap=int(input('Nhap: '))
# if(len(arr)>=nhap>=1):
#      print(f'So la Ma: [{arr[nhap-1]}]')
# else:
#      print(f'Nhap khong hop le! ')
     


# tuoi=int(input('tuoi: '))
# # tuoi=10
# ob={
#      0:'so sinh' if tuoi else 'deo  co',
#      1: 'tre em' if tuoi  else 'khog biet',
#      13: 'thieu nien' if tuoi else 'khong biet',
#      20: ' nguoi  lon' if tuoi else 'khong phai ng lon',
# }
# for x  in ob:
#      # print(x<=tuoi<=x+7)
#      if x<=tuoi <=x+7:
#           print(ob[x])
#           break


# mau1=input('Mau1:')  
# mau2=input('Mau2:')  
# arr=['tim','cam','xanh la cay','blue']
# if mau1=='xanhduong' and  mau2=='do' :
#      print(arr[0])
# elif mau1=='do' and mau2=='vang':
#      print(arr[1])
# elif mau1=='xanh' and mau2=='vang':
#      print(arr[2])
# else:
#      print('buoi ')
     
mau1=input('mau').lower()
mau2=input('mau').lower()
ob={
     ('nam','tung'): 'vang',
     ('xanh','do'):'tim', 
     ('vang','tim'):'cam',
}

