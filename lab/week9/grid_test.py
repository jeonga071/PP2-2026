from tkinter import *

window = Tk()

Label(window, text = "너비").grid(row = 0, column = 0)  #0이면 생략 가능?
Label(window, text = "높이").grid(row = 1, column = 0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

Button(window, text = "이미지 저장").grid(row = 2, column = 1)

photo = PhotoImage()
Label(window, image = photo).grid(row = 0, column = 2, columnspan = 2, rowspan = 2) # span: 여러 칸을 하나로 합쳐서 사용

Button(window, text = "확대").grid(row = 2, column = 2)
Button(window, text = "축소").grid(row = 2, column = 3)


window.mainloop()