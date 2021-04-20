from tkinter import *
window = Tk()
window.config(background = "black")    
def from_kg():
    gram = float(e2.get())*1000
    pound = float(e2.get())*2.20462
    ounce = float(e2.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)

e0=Label(window,text="Weight Converter",font="times 30",bg="black",fg="gold")
e0.grid(row=0,column=0,columnspan=4)

e1 = Label(window, text="Input the weight in KG :",bg="black",fg="#fda50f",font="17")
e1.grid(row=1, column=1)

e2 = Entry(window, textvariable=StringVar(),fg="black",bg="gold",width=40)
e2.grid(row=1, column=2)

e3 = Label(window, text="Gram",bg="black",fg="gold",font="15")
e3.grid(row=2, column=1)

e4 = Label(window, text="Pound",bg="black",fg="gold",font="15")
e4.grid(row=2, column=2)

e5 = Label(window, text="Ounce",bg="black",fg="gold",font="15")
e5.grid(row=2, column=3)

t1 = Text(window, height=2, width=30,fg="black",bg="#fda50f",font = ("times"))
t1.grid(row=3, column=1)
t2 = Text(window, height=2, width=30,fg="black",bg="#fda50f",font = ("times"))
t2.grid(row=3, column=2)
t3 = Text(window, height=2, width=30,fg="black",bg="#fda50f",font = ("times"))
t3.grid(row=3, column=3)

b1 = Button(window, text="CONVERT", command=from_kg,fg="black",bg="#db9200",width=10,font = ('bold'))
b1.grid(row=1, column=3)

Exit = Button(window, text = "EXIT", fg = "White", bg = "red", width=12,font = ("times",15,"bold"),command = exit)     
Exit.grid(row = 4, column=0,columnspan=4,pady=10)   

window.mainloop()
