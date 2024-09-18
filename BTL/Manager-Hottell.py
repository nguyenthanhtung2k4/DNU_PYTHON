from tkinter import ttk
import tkinter as tk
import csv
from PIL import Image, ImageTk  # Import for icon handling

def room(title,status,w,h):
     view=tk.Toplevel(window)
     view.title(title)
     img=Image.open(icon)
     photo=ImageTk.PhotoImage(img)
     view.iconphoto(False,photo)
     if status== True:
          view.geometry(f'{w}x{h}')
     return view
          
     
def menu4():
     width = 600 
     height = 400
     view=room('View Room',False,width,height)
     
     # Tạo Treeview widget để hiển thị bảng
     tree = ttk.Treeview(view, columns=("Số phòng", "Loại", "Giá", "Trạng thái"), show="headings")
     tree.heading("Số phòng", text="Số phòng")
     tree.heading("Loại", text="Loại")
     tree.heading("Giá", text="Giá")
     tree.heading("Trạng thái", text="Trạng thái")

     # Đặt chiều rộng cho từng cột
     tree.column("Số phòng", width=100)
     tree.column("Loại", width=150)
     tree.column("Giá", width=100)
     tree.column("Trạng thái", width=150)
     with open(file_phong, 'r', encoding='utf-8') as r:
          reader = csv.DictReader(r)
          for row in reader:
               room_number = row["Số phòng"]
               room_type = row['Loại']
               room_price=row['Giá']
               room_status=row['Trạng thái']
               # print( room_number)
          # Sử dụng grid để đặt kích thước và vị trí
               tree.insert("", tk.END, values=(room_number, room_type, room_price, room_status))
               tree.pack()

     view.mainloop()  # Start the event loop for the Toplevel window

def menu1():
     view=room('Add Room',True,400,150)
     global entry
     #  fame tao 2 cot
     def fame(view,row,column):
          fame = tk.Frame(view)
          fame.grid(row=row, column=column, padx=5, pady=5)
    
          fame2 = tk.Frame(view)
          fame2.grid(row=row, column=column + 1, padx=5, pady=5)
    
          entry = tk.Entry(fame2)
          entry.pack()
    
          return fame, fame2, entry

     def tung():
          results = []
          for entry in bienLabel:
               results.append(entry.get())  # Lấy dữ liệu từ các Entry
               result_label.config(text=f"Kết quả: {', '.join(results)}")  # Hiển thị kết quả

     #  thay  doi  fame  ben duoi 
     label=['so','loai','gia','status']
     bienLabel=['so','loai','gia','status']
     for i in range(4):
          f1,f2,entry=fame(view,i,0)
          tk.Label(f1,text=label[i]).pack()
          bienLabel.append(entry)
          
          
     button = tk.Button(view, text='Click', command=tung)
     button.pack(pady=10)

     result_label = tk.Label(view, text="")
     result_label.pack()

     view.mainloop()
def main(menu):
     global window
     window = tk.Tk()

    # Set window title
     window.title('Manager-Hottell')

    # Set window size (consider using a fixed size for readability)
     width = window.winfo_screenwidth() // 2
     height = window.winfo_screenheight() // 2
     window.geometry(f"{width}x{height}")

    # Set icon (optional)
     # try exxpect
     image = Image.open(icon)
     photo = ImageTk.PhotoImage(image)
     window.iconphoto(False, photo)
   

    # title
     title_label = tk.Label(window, text="Manager-Hottell", background="yellow")
     title_label.pack()

    # cua so nho
     print(menu[1])
     tk.Button(window,text=menu[1],command=lambda: menu1()).pack()
     tk.Button(window,text=menu[4],command=lambda: menu4()).pack()
     

    # Run the main loop
     window.mainloop()

if __name__ == '__main__':
     global icon,file_phong,menu
     icon = 'logo.jpg'
     file_phong = 'D:\CODE\DNU_PYTHON\BTL\phòng.csv'
     menu = {
        1: 'Add Phong',
        4: 'View Phong'
     }

     main(menu)