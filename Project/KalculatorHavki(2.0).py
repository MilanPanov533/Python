from tkinter import *

def defiks(): #если ты толстый
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

def vegans(): #если ты специфик
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
    
def profiks(): #если ты худыш
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

    c=Canvas(root,bg="crimson",height=60,width=800)
    filename=PhotoImage(file="baza.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()

    back=StringVar()
    back_button=Button(text="Назад", width="15", bg="#EEE0CC", command=delp,font="Arial 15")
    back_button.place(relx=.1, rely=.1 ,anchor="c")

    root.mainloop()
def mid():
    global root
    root=Tk()
    root.geometry("1600x900")
    root.configure(bg="#c98842")
    c=Canvas(root,bg="gray",height=10,width=20)
    filename=PhotoImage(file="kalk.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
    back = StringVar()
    back_button = Button(text="Назад", width="15", bg="#EEE0CC", command=delp)
    back_button.place(relx=.1, rely=.1, anchor="c")

    poetry ="         Вам нужен ДЕФИЦИТ!!!!!\nЧтобы ознакомиться с подробной\n информацией нажми на кнопку!"
    label2 = Label(text=poetry, justify=LEFT,bg="#50C2F3",font="Arial 30")
    label2.place(x=480,y=50)
    defik=StringVar()
    defik_button=Button(text="Дефицит",width="45",bg="#eb3434", command=defiks,font="Arial 15")
    defik_button.place(relx=.5, rely=.3 ,anchor="c")
    poetry ="также ознакомтесь..."
    label3 = Label(text=poetry, justify=LEFT,bg="#50C2F3",font="Arial 30")
    label3.place(relx=.5, rely=.6 ,anchor="c")
    vegan=StringVar()
    vegan_button=Button(text="Веган",width="45",bg="#f5f507", command=vegans,font="Arial 15")
    vegan_button.place(relx=.5, rely=.7 ,anchor="c")
    root.mainloop()
def mid2():
    global root
    root=Tk()
    root.geometry("1600x900")
    root.configure(bg="#c98842")
    c=Canvas(root,bg="gray",height=10,width=20)
    filename=PhotoImage(file="kalk.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
    back = StringVar()
    back_button = Button(text="Назад", width="15", bg="#EEE0CC", command=delp)
    back_button.place(relx=.1, rely=.1, anchor="c")
    poetry ="         Вас нужен ПРОФИЦИТ!!!!!\nЧтобы ознакомиться с подробной\n информацией нажми на кнопку!"
    label2 = Label(text=poetry, justify=LEFT,bg="#50C2F3",font="Arial 30")
    label2.place(x=480,y=50)
    profik=StringVar()
    profik_button=Button(text="Профицит",width="45",bg="#16BE1B", command=profiks,font="Arial 15")
    profik_button.place(relx=.5, rely=.3,anchor="c")
    poetry ="также ознакомтесь..."
    label3 = Label(text=poetry, justify=LEFT,bg="#50C2F3",font="Arial 30")
    label3.place(relx=.5, rely=.6 ,anchor="c")
    vegan=StringVar()
    vegan_button=Button(text="Веган",width="45",bg="#f5f507", command=vegans,font="Arial 15")
    vegan_button.place(relx=.5, rely=.7 ,anchor="c")
    root.mainloop()
def mid3():
    global root
    root=Tk()
    root.geometry("1600x900")
    root.configure(bg="#c98842")
    c=Canvas(root,bg="gray",height=10,width=20)
    filename=PhotoImage(file="kalk.png")
    background_label=Label(root,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
    back = StringVar()
    back_button = Button(text="Назад", width="15", bg="#EEE0CC", command=delp)
    back_button.place(relx=.1, rely=.1, anchor="c")
    poetry ="      У вас все впорядке!\n Вы можете ознакомиться\n с Веганской диетой"
    label2 = Label(text=poetry, justify=LEFT,bg="#50C2F3",font="Arial 30")
    label2.place(x=340,y=50)
    vegan=StringVar()
    vegan_button=Button(text="Веган",width="45",bg="#f5f507", command=vegans,font="Arial 15")
    vegan_button.place(relx=.5, rely=.3 ,anchor="c")
    root.mainloops()

def kkal():
    root.destroy()
    print("*****************MENU*************************\n1)Вы занимаитесь спортом")
    ask1=int(input(" Да-1, Нет-2\n"))
    ask2=int(input("2)Сколько раз в день вы едите?\n Один раз-1, Два раза-2, Три раза-3, Четыре или больше=4\n"))
    ask3=int(input("3)Пьете ли вы норму воды (2литра)?\n Да=1, Нет=2 \n"))
    ask4=int(input("4)Часто ли вы едите в FastFood? \n Нет-1, Да-2 \n"))
    ask5=int(input("5)Ваш вес? \n >50кг-1 ,50кг< >90кг-2, 90кг<-3\n"))
    print("**********************************************")
    amount=ask1+ask2+ask3+ask4+ask5
    if amount<8 or amount==8:
        mid2()
    elif amount==9 and amount==10 and amount==11:
        mid3()
    else:
        mid()

    ''''''

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
    poetry ="Ведутся работы"
    label2 = Label(text=poetry, justify=LEFT,bg="#FFFFFF",font="Arial 30")
    label2.place(x=940,y=50)
    
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
    label2.place(x=640,y=50)

    recept=StringVar()
    recept_button=Button(text="   Здоровая еда    ",bg="#16BE1B", command=resept,font="Arial 20")
    recept_button.place(relx=.5, rely=.2 ,anchor="c")

    kal=StringVar()
    kal_button=Button(text="Калькулятор калорий",bg="#D696D8",command=kkal,font="Arial 20")
    kal_button.place(relx=.5, rely=.3 ,anchor="c")

    recept2=StringVar()
    recept2_button=Button(text="      Гайд на питание       ",bg="#FF9700", command=rec,font="Arial 20")
    recept2_button.place(relx=.5, rely=.4 ,anchor="c")

    elsy=StringVar()
    elsy_button=Button(text="            Другое            ",bg="#D7CCEE",command=eelse,font="Arial 20")
    elsy_button.place(relx=.5, rely=.5 ,anchor="c")
    root.mainloop()

menu()
