import tkinter as tk
#from tkinter import *

window = tk.TK()
window.title("Hello 임정아")
window.geometry("400x200") #사이즈 변경

label = tk.Label(window, text = "Hello, GUI!")
label.pack()

window.mainloop()   # 사용자 동작 대기