
class Phong:
     def __init__(self, so_phong, loai_phong, gia, trang_thai):
          self.so_phong = so_phong
          self.loai_phong = loai_phong
          self.gia = gia
          self.trang_thai = trang_thai

     def dat_phong(self):
          if self.trang_thai == "Trống":
               self.trang_thai = "Đã đặt"
               print("Đặt phòng thành công!")
          else:
               print("Phòng đã được đặt!")

     def tra_phong(self):
          if self.trang_thai == "Đã đặt":
               self.trang_thai = "Trống"
               print("Trả phòng thành công!")
          else:
               print("Phòng chưa được đặt!")
     def view_phong(self):
          print( f"Phong: {self.so_phong}\nGia: {self.gia}")

# Tạo một đối tượng phòng
phong1 = Phong(101, "Deluxe", 1000000, "Trống")

# Đặt phòng
print(f'Đặt phòng:')
phong1.dat_phong()
# Xem  phong
print(f'\nXem phòng:')
phong1.view_phong()
# Tra phòng
print(f'\ntra phòng:')
phong1.tra_phong()