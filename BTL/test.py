from tkinter import ttk
import tkinter as tk
import csv
from PIL import Image, ImageTk  # Import for icon handling

def room(title, status, w, h):
    view = tk.Toplevel(window)  # Tạo cửa sổ mới
    view.title(title)
    view.geometry(f"{w}x{h}")
    return view

def menu1():
    view = room('Add Room', True, 400, 150)  # Tạo cửa sổ phụ
    bienLabel = []  # Khởi tạo danh sách để lưu các Entry

    # Hàm tạo frame với 2 cột
    def fame(view, row, column):
        fame = tk.Frame(view)
        fame.grid(row=row, column=column, padx=5, pady=5)
    
        fame2 = tk.Frame(view)
        fame2.grid(row=row, column=column + 1, padx=5, pady=5)
    
        entry = tk.Entry(fame2)
        entry.pack()
    
        return fame, fame2, entry

    # Hàm xử lý sự kiện bấm nút
    def tung():
        results = []
        for entry in bienLabel:
            results.append(entry.get())  # Lấy dữ liệu từ các Entry
        result_label.config(text=f"Kết quả: {', '.join(results)}")  # Hiển thị kết quả

    # Tạo nhãn và entry cho mỗi thuộc tính
    label = ['Số', 'Loại', 'Giá', 'Trạng thái']
    for i in range(4):
        f1, f2, entry = fame(view, i, 0)
        tk.Label(f1, text=label[i]).pack()
        bienLabel.append(entry)  # Lưu Entry vào danh sách

    # Nút bấm và nhãn kết quả
    buttonFame=tk.Frame(view)
    buttonFame.grid(row=6,column=5)
    button = tk.Button(buttonFame, text='Click', command=tung)
    button.pack(pady=10)

    label_text=tk.Frame(view)
    label_text.grid(row=7,column=5)
    result_label = tk.Label(label_text, text="")
    result_label.pack()

def main(menu):
    global window
    window = tk.Tk()

    # Set window title
    window.title('Manager-Hottell')

    # Set window size
    width = window.winfo_screenwidth() // 2
    height = window.winfo_screenheight() // 2
    window.geometry(f"{width}x{height}")

    # Set icon (optional)
    try:
        image = Image.open(icon)
        photo = ImageTk.PhotoImage(image)
        window.iconphoto(False, photo)
    except Exception as e:
        print(f"Error loading icon: {e}")

    # Title label
    title_label = tk.Label(window, text="Manager-Hottell", background="yellow")
    title_label.pack(pady=10)

    # Buttons to open other windows
    tk.Button(window, text='Add Phong', command=menu1).pack(pady=5)
    # Bạn có thể thêm hàm cho View Phong nếu cần
    # tk.Button(window, text='View Phong', command=menu4).pack(pady=5)

    window.mainloop()

if __name__ == '__main__':
    global icon, file_phong, menu
    icon = 'logo.jpg'
    file_phong = 'D:\CODE\DNU_PYTHON\BTL\phòng.csv'
    menu = {
        1: 'Add Phong',
        4: 'View Phong'
    }

    main(menu)
