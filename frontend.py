"""
A app that stores books information:
Title, Author
Year, ISBN

User can:
View all entry
Search entry
Add new entry
Update entry
Delete entry
Close app
"""
from tkinter import *
import backend

window = Tk()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text=StringVar
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar
e1=Entry(window, textvariable=author_text)
e1.grid(row=0, column=3)

year_text=StringVar
e1=Entry(window, textvariable=year_text)
e1.grid(row=1, column=1)

isbn_text=StringVar
e1=Entry(window, textvariable=isbn_text)
e1.grid(row=1, column=3)

list1=Listbox(window, height=10, width=40)
list1.grid(row=2, column=0, rowspan=7, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
#TODO: add comment param to button
b1=Button(window, text="View All", width=12)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()