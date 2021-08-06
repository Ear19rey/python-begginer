from tkinter import *

window = Tk()
window.title("♠BlackJack")
window.geometry("300x300")
#window.maxsize(600,600)
window.resizable(0,0)
lab1 = Label(window,text="Let's play!!!",
              font="Courier 12 bold italic")

lab2 = Label(window,text="START",
             bg="grey",fg="white",width=6,
             font="Courier 12 bold italic",relief="raised")

lab3 = Label(window,text="RULE",
             bg="grey",fg="white",width=6,
             font="Courier 12 bold italic",relief="raised")

"""
lab1.grid(row=0,column=2)
lab2.grid(row=1,column=1)
lab3.grid(row=1,column=3)

lab1.place(x=75,y=0)
lab2.place(x=25,y=50)
lab3.place(x=175,y=50)
"""

def msgShow():
    label["text"] = "Author:Bob"
    label["bg"] = "pink"
    label["fg"] = "black"
    label["font"] = "bold"

def bcolor(bgColor):
    window.config(bg=bgColor)
    lab1["bg"] = bgColor
    label["bg"] = bgColor

label =Label(window)
credit = Button(window, text="Credit",bg="grey",fg="white",width=6,font="Courier 12 bold italic",command=msgShow)
exit = Button(window, text="Exit",bg="grey",fg="white",width=6,font="Courier 12 bold italic",command=window.destroy)

pink = Button(window, text="Pinky",bg="grey",fg="white",command=lambda:bcolor("pink"))
green = Button(window, text="Green",bg="grey",fg="white",command=lambda:bcolor("green"))

lab1.pack(pady=30)
lab2.pack()
lab3.pack(pady=5)
credit.pack()
exit.pack(pady=5)
label.pack()
pink.pack(anchor=S,side=RIGHT,padx=5)
green.pack(anchor=S,side=RIGHT)

window.mainloop()