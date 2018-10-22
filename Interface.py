from tkinter import *

class Application:
    def __init__(self,master=None):
        self.diIFario = Frame(master)
        self.diIFario.pack()
        self.msg = Label(self.diIFario, text="diIFario")
        self.msg.pack()
        self.logarN = Label(master,text="nome")
        self.logarN.pack(side=LEFT)
        self.logarN1 = Entry(master)
        self.logarN1["width"] = 30
        self.logarN1.pack(side=LEFT)
        self.logarS = Label(master,text="senha")
        self.logarS.pack(side=LEFT)
        self.logarS1 = Entry(master)
        self.logarS1["width"] = 30
        self.logarS1.pack(side=LEFT)
        self.login = Button(master)
        self.login["text"] = "Logar"
        self.login["width"] = 12
        self.login.pack()

root = Tk()
Application(root)
root.mainloop()
