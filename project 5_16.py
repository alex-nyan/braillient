from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lb1 = Label(win, text = "Enter your first number").place(x = 50, y = 50)
        self.lb2 = Label(win, text = "Enter your second number").place(x = 50, y = 100)
        self.lb3 = Label(win, text = "Result").place(x = 50, y = 200)
        self.ent1 = Entry(bd=3)
        self.ent2 = Entry()
        self.ent3 = Entry()
        self.btn1 = Button(win, text = "Add", command=self.add).place(x = 100, y = 150)
        self.btn2 = Button(win, text = "Sub")
        self.btn2.bind('<Button-1>',self.sub)
        self.ent1.place(x=200, y = 50)
        self.ent2.place(x=200, y = 100)
        self.ent3.place(x=200, y = 200)
        self.btn2.place(x=200, y = 150)
    def add(self):
        self.ent3.delete(0,'end')
        n1 = int(self.ent1.get())
        n2 = int(self.ent2.get())
        result = n1 + n2
        self.ent3.insert(END,result)
    def sub(self):
        self.ent3.delete(0,'end')
        n1 = int(self.ent1.get())
        n2 = int(self.ent2.get())
        result = n1 - n2
        self.ent3.insert(END,result)
window = Tk()
window.geometry('400x300')
window.title("Python Tk")
mywin = MyWindow(window)
window.mainloop()