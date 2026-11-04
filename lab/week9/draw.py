from tkinter import *

window = Tk()

w = Canvas(window, width = 300, height = 200)
w.pack()

w.create_rectangle(50, 25, 200, 100, fill = "blue") #x, y, w, h

i = w.create_rectangle(50, 25, 200, 100, fill = "red")
w.coords(i, 0, 0, 100, 100) # 캔버스 좌표 변경
w.itemconfig(i, fill = "green") #색상 변경

w.delete(i)
w.delete(ALL)

window.mainloop()