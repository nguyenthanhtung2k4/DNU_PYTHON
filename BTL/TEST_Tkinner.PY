import tkinter as tk

def calculate():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 * num2
    result_label.config(text=f"Kết quả: {result}")

window = tk.Tk()
window.title("Máy tính đơn giản")

label1 = tk.Label(window, text="Nhập số thứ nhất:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Nhập số thứ hai:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window, text="Tính", command=calculate)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()