import tkinter as tk

def change_window():
    # Ẩn nút "Tùng"
    button_tung.pack_forget()
    # Hiển thị label "nguyenthanh tung"
    label_name.pack()
    # Hiển thị nút "Back"
    button_back.pack()

def back_to_normal():
    # Ẩn label và nút "Back"
    label_name.pack_forget()
    button_back.pack_forget()
    # Hiển thị lại nút "Tùng"
    button_tung.pack()

# Tạo cửa sổ chính
root = tk.Tk()

# Tạo các widget
button_tung = tk.Button(root, text="Tùng", command=change_window)
label_name = tk.Label(root, text="nguyenthanh tung")
button_back = tk.Button(root, text="Back", command=back_to_normal)

# Ban đầu chỉ hiển thị nút "Tùng"
button_tung.pack()

root.mainloop()

# ///////////////////////////// cửa sổ nhỏ 

# import tkinter as tk

# def create_toplevel():
#     # Tạo một cửa sổ Toplevel
#     new_window = tk.Toplevel(root)
#     new_window.title("Cửa sổ con")

#     # Thêm các widget vào cửa sổ con
#     label = tk.Label(new_window, text="Đây là một cửa sổ con")
#     label.pack()

# # Tạo cửa sổ chính
# root = tk.Tk()
# root.title("Cửa sổ chính")

# # Tạo nút để mở cửa sổ con
# button = tk.Button(root, text="Mở cửa sổ con", command=create_toplevel)
# button.pack()

# root.mainloop()