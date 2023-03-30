from tkinter import *

def defiks():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1600x900")
    root.configure(bg="#FF9700")

    c=Canvas(root,bg="crimson",height=10,width=20)
    filename=PhotoImage(file="дефицивчик.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()

    back=StringVar()
    back_button=Button(text="Назад",width="15",bg="#EEE0CC", command=rec,font="Arial 15")
    back_button.place(relx=.1, rely=.1 ,anchor="c")

    root.mainloop()

def vegans():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1600x900")
    root.configure(bg="#FF9700")

    c=Canvas(root,bg="yellow",height=10,width=20)
    filename=PhotoImage(file="веганчик.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
    

    back=StringVar()
    back_button=Button(text="Назад",width="15",bg="#EEE0CC", command=rec,font="Arial 15")
    back_button.place(relx=.1, rely=.1 ,anchor="c")

    root.mainloop()
    
def profiks():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1600x900")
    root.configure(bg="#FF9700")

    c=Canvas(root,bg="lime",height=10,width=20)
    filename=PhotoImage(file="профицивчик.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()

    back=StringVar()
    back_button=Button(text="Назад",width="15",bg="#EEE0CC", command=rec,font="Arial 15")
    back_button.place(relx=.1, rely=.1 ,anchor="c")

    root.mainloop()

def delp():
    global root
    menu()
def delp1():
    global root
    rec()

def resept():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1600x900")
    root.configure(bg="#16BE1B")

    back=StringVar()
    back_button=Button(text="Назад", width="15", bg="#EEE0CC", command=delp,font="Arial 15")
    back_button.place(relx=.1, rely=.1 ,anchor="c")

    root.mainloop()

def kkal():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1600x900")
    root.configure(bg="#D696D8")
    
    poetry = "Главная"
    label2 = Label(text=poetry, justify=LEFT, bg="#D696D8",fg="#D696D8", font="Arial 30")
    label2.grid (row=3, column=5, sticky=W)

    header = Label(text="Вы занимаитесь спортом?", padx=15, pady=10,bg="#D696D8",font="Arial 15")
    header.grid(row=5, column=8, sticky=W)
    sportall = IntVar()
    sport = Radiobutton(text="Да",value=1, variable=sportall,bg="#D696D8",font="Arial 15")
    sport.grid(row=5, column=8, sticky=W)
    nosport= Radiobutton(text="Нет",value=2, variable=sportall,bg="#D696D8",font="Arial 15")
    nosport.grid(row=6, column=8, sticky=W)

    eats = Label(text="Kак часто вы кушаете?", padx=15, pady=10, bg="#D696D8",font="Arial 15")
    eats.grid(row=6, column=8, sticky=W)
    allf = IntVar()
    one= Radiobutton(text="1", value=1, variable=allf, bg="#D696D8",font="Arial 15")
    one.grid(row=7, column=8, sticky=W)
    two = Radiobutton(text="2", value=2, variable=allf, bg="#D696D8",font="Arial 15")
    two.grid(row=8, column=8, sticky=W)
    three = Radiobutton(text=3, value=3, variable=allf, bg="#D696D8",font="Arial 15")
    three.grid(row=9, column=8, sticky=W)
    more = Radiobutton(text=">3", value=4, variable=allf, bg="#D696D8",font="Arial 15")
    more.grid(row=10, column=8, sticky=W)
    back = StringVar()
    back_button = Button(text="Назад", width="15", bg="#EEE0CC", command=delp)
    back_button.place(relx=.1, rely=.1, anchor="c")


    root.mainloop()

def rec():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1600x900")
    root.configure(bg="#c98842")

    c=Canvas(root,bg="crimson",height=60,width=800)
    filename=PhotoImage(file="sidor.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
    
    defik=StringVar()
    defik_button=Button(text="Дефицит",width="45",bg="#eb3434", command=defiks,font="Arial 15")
    defik_button.place(relx=.5, rely=.2 ,anchor="c")

    vegan=StringVar()
    vegan_button=Button(text="Веган",width="45",bg="#f5f507", command=vegans,font="Arial 15")
    vegan_button.place(relx=.5, rely=.3 ,anchor="c")

    profik=StringVar()
    profik_button=Button(text="Профицит",width="45",bg="#16BE1B", command=profiks,font="Arial 15")
    profik_button.place(relx=.5, rely=.4,anchor="c")

    back=StringVar()
    back_button=Button(text="Назад",width="15",bg="#EEE0CC", command=delp,font="Arial 15")
    back_button.place(relx=.1, rely=.1 ,anchor="c")

    root.mainloop()

def eelse():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1600x900")
    root.configure(bg="#D7CCEE")

    c=Canvas(root,bg="gray",height=10,width=20)
    filename=PhotoImage(file="ehitaja.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()

    back=StringVar()
    back_button=Button(text="Назад",width="15",bg="#EEE0CC", command=delp,font="Arial 15")
    back_button.place(relx=.1, rely=.1 ,anchor="c")
    root.mainloop()

root=Tk()
def menu():
    global root
    root.destroy()
    root = Tk()
    root.geometry("1600x900")
    root.configure(bg="#EEE0CC")

    c=Canvas(root,bg="crimson",height=60,width=800)
    filename=PhotoImage(file="aboba.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()

    poetry ="Калькулятор еды"
    label2 = Label(text=poetry, justify=LEFT,bg="#50C2F3",font="Arial 30")
    label2.place(x=650,y=50)

    recept=StringVar()
    recept_button=Button(text="   + Новый рацион    ",bg="#16BE1B", command=resept,font="Arial 20")
    recept_button.place(relx=.5, rely=.2 ,anchor="c")

    kal=StringVar()
    kal_button=Button(text="Калькулятор калорий",bg="#D696D8",command=kkal,font="Arial 20")
    kal_button.place(relx=.5, rely=.3 ,anchor="c")

    recept2=StringVar()
    recept2_button=Button(text="      Доп. Рецепты       ",bg="#FF9700", command=rec,font="Arial 20")
    recept2_button.place(relx=.5, rely=.4 ,anchor="c")

    elsy=StringVar()
    elsy_button=Button(text="            Другое            ",bg="#D7CCEE",command=eelse,font="Arial 20")
    elsy_button.place(relx=.5, rely=.5 ,anchor="c")
    root.mainloop()

menu()
