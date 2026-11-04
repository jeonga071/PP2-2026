from tkinter import *

def process():
    tf = float(e1.get())    #textbox 값 가져오기
    tc = (tf - 32.0) * 5.0 / 9.0
    e2.delete(0, END)   #기존 값 삭제
    e2.insert(0, str(tc))

window = Tk()

Label(window, text = "화씨").grid(row = 0, column = 0) # 변경 사항이 없을 경우
Label(window, text = "섭씨").grid(row = 1, column = 0)
e1 = Entry(window)  #textbox
e2 = Entry(window)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

Button(window, text = "화씨->섭씨", command = process).grid(row = 2, column = 1)

window.mainloop()