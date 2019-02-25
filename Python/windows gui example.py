from tkinter import *

window=Tk()

l1 = label(windows, text="Title")
l1.grid(row=0,column=0)

l1=label(window, text="Author")
lid.grid(row=0,column=2)

l1=label(window,text="Year")
l1.grid(row=1,column=0)

l1=label(window,text="ISBN")
l1.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=ListBox(windows, height=6, width=35)
list1.grid(row=2, column=0, columnspan=2)

sb1 = scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View All", width=12)
b1.grid(row=2,column=3)

windows.mainloop()

