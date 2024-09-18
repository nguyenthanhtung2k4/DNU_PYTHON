# //////////////////////////// tai anh  len lam  bg


# import tkinter as tk
# from PIL import Image, ImageTk

# # Tạo cửa sổ
# window = tk.Tk()

# # Tải hình ảnh
# image = Image.open("logo.jpg")
# photo = ImageTk.PhotoImage(image)

# # Tạo label để hiển thị hình ảnh
# label = tk.Label(window, image=photo)
# label.pack()

# # Thay đổi kích thước hình ảnh (ví dụ)
# new_size = (200, 100)
# image = image.resize(new_size)
# photo = ImageTk.PhotoImage(image)
# label.config(image=photo)

# window.mainloop()





# //////////////////////////// icon logo
# import tkinter as tk
# from PIL import Image, ImageTk

# # Tạo cửa sổ
# window = tk.Tk()

# # Tải icon
# icon_path = "path/to/your/icon.png"  # Thay thế bằng đường dẫn đến icon của bạn
# icon = Image.open(icon_path)
# photo = ImageTk.PhotoImage(icon)

# # Gán icon cho cửa sổ
# window.iconphoto(False, photo)

# # Thêm các widget khác vào cửa sổ (nếu cần)
# # ...

# # Hiển thị cửa sổ
# window.mainloop()



#  /////////////// kich thuoc man  hinh
# import tkinter as tk

# # Lấy kích thước màn hình
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# # Tính toán kích thước cửa sổ (ví dụ: chiếm 80% chiều rộng và 60% chiều cao màn hình)
# window_width = int(screen_width * 0.8)
# window_height = int(screen_height * 0.6)

# # Đặt vị trí cửa sổ ở giữa màn hình
# x = int((screen_width - window_width) / 2)
# y = int((screen_height - window_height) / 2)

# window.geometry(f"{window_width}x{window_height}+{x}+{y}")


import tkinter as tk

# Tạo cửa sổ chính
window = tk.Tk()

# Tạo hai frame
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)

# Sắp xếp các frame theo lưới
frame1.grid(row=2, column=0)
frame2.grid(row=0, column=1)

# Thêm các widget vào các frame
label1 = tk.Label(frame1, text="Frame 1")
label1.pack()

button1 = tk.Button(frame2, text="Button 1")
button1.pack()

window.mainloop()