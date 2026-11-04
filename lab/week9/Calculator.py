from tkinter import *

def button_click(i):
    if b_text[i] == "C":
        e1.delete(0, END)
        return
    
    e1.insert(END, b_text[i])

window = Tk()
e1 = Entry(window, bg = "yellow", width = 33)
e1.grid(row = 0, column = 0, columnspan = 5)

b_list = []
b_text = ["7", "8", "9", "/", "C",
          "4", "5", "6", "*", "",
          "1", "2", "3", "-", "",
          "0", ".", "=", "+", ""]
row_index = 1
col_index = 0


for i in range(len(b_text)):
    b = Button(window, text = b_text[i], width = 5, command = lambda k = i: button_click(k))
    b.grid(row = row_index, column = col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
    b_list.append(b)

window.mainloop()