import os,sys
try:
     import openpyxl
except:
     print(' dang cai dat thu vien ')
     os.system('pip install openpyxl')


import openpyxl

# Tạo một workbook mới

workbook = openpyxl.Workbook()

# Chọn sheet làm việc mặc định
sheet = workbook.active

# Viết dữ liệu vào các ô
sheet['A1'] = 'Họ và tên';sheet['B1'] = 'Tuổi'
sheet['A2'] = 'Nguyễn Văn A';sheet['B2'] = 30
sheet['A3'] = 'Nguyễn Văn A';sheet['B3'] = 30

# Lưu workbook
workbook.save('./DNU_PYTHON/BTL/THANHTUNG_SHEET.xlsx')