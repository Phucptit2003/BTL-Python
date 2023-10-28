import tkinter as tk
from tkinter import *
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title("Translate")
root.geometry("720x480")
root.resizable(False, False)

#tạo nền
framel = Frame(root, width = 720, height = 480, relief=RIDGE, bg="#F0EDE6")
framel.place(x = 0, y = 0)

#tạo khung label
Label(root, text="Translator", font=("Helvetica 20"), fg = "#2C323E", bg = "#FAF4F6").pack(pady = 10)

#khung nhập văn bản dịch
text_entry1 = Text(framel, width = 25, height = 6, borderwidth = 2, relief=GROOVE, font=("verdana", 15))
text_entry1.place(x = 10, y = 80)

text_entry2 = Text(framel, width = 25, height = 6, borderwidth = 2, relief=GROOVE, font=("verdana", 15), bg = "#F5F5F5")
text_entry2.place(x = 380 , y = 80)

#nút dịch
btn1 = Button(framel, text = " ", relief=RAISED, font=("verdana", 10, "bold"), bg = "#248AA2", fg = "white", cursor="hand2")
btn1.place(x = 350, y = 140)
#nút dịch tôi đang tính để hình cái icon mũi tên

#nút clear
btn2 = Button(framel, text = "Xóa", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg = "#248AA2", fg = "white", cursor="hand2")
btn2.place(x = 290, y = 250)

# Tạo nút "Phát Tiếng" và "Thu Âm"
play_button = Button(framel, text = "Phát Tiếng", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg = "#248AA2", fg = "white", cursor="hand2")
play_button.place(x = 380, y = 250)

record_button = Button(framel, text = "Thu Âm", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg = "#248AA2", fg = "white", cursor="hand2")
record_button.place(x = 10, y = 250)

# Tạo lịch sử lịch
history_label = tk.Label(root, text="Lịch Sử Dịch:")
history_label.pack()
history_label.place(x = 320, y = 290)

history_text = tk.Text(root, height = 8, width = 48)
history_text.pack()
history_text.place(x = 170, y = 310)

root.mainloop()