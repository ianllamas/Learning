#Front End

from tkinter import*
import tkinter.messagebox

#import stdDatabase

class Student:

    def __init__(self,root):
        self.root =root 
        self.root.title("Student Database Management Systems")
        self.root.geometry("1350x750+0+0") 
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        FirstName = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Address = StringVar()
        Mobile = StringVar()

# ====FRAME====
        MainFrame = Frame (self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd =2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font = ('arial',47, 'bold'), text="Student Database Management Systems", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame =Frame(MainFrame, bd=2, width=1350, height=70, padx=18,pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)


if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()



