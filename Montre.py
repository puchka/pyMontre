# -*- coding:Latin-1 -*-

from Tkinter import *
from time import localtime
from math import sin, cos, pi

class ElWatch(Frame):
    "classe d'une montre électronique"
    def __init__(self):
        Frame.__init__(self,bg='grey')
        self.hvar = StringVar()
        self.hh = Entry(self,textvariable=self.hvar,width=5,
                        justify=CENTER,bg="light blue")
        self.hh.grid(row=1,column=1,padx=2,pady=2)

        self.mvar = StringVar()
        self.mm = Entry(self,textvariable=self.mvar,width=5,
                        justify=CENTER,bg="light blue")
        self.mm.grid(row=1,column=2,padx=2,pady=2)

        self.svar = StringVar()
        self.ss = Entry(self,textvariable=self.svar,width=5,
                        justify=CENTER,bg="light blue")
        self.ss.grid(row=1,column=3,padx=2,pady=2)
        
        time = localtime()
        self.h = time[3]
        self.m = time[4]
        self.s = time[5]
        self.hvar.set(str(self.h))
        self.mvar.set(str(self.m))
        self.svar.set(str(self.s))
        self.master.after(1000,self.heure)

        self.grid()

    def heure(self):
        "méthode qui met en marche la montre"
        time = localtime()
        self.h = time[3]
        self.m = time[4]
        self.s = time[5]
        self.svar.set(str(self.s))
        self.mvar.set(str(self.m))
        self.hvar.set(str(self.h))
        self.master.after(1000,self.heure)


class MecWatch(Frame):
    "classe d'un motre mécanique"
    def __init__(self):
        Frame.__init__(self)
        self.montre = Canvas(self,width=200,heigh=200,bg='grey')
        self.montre.grid(row=1,column=1)
        
        self.montre.create_oval(15,15,185,185,fill='light blue',width=2)
        a = 0
        while a < 4:
            x1 = cos(a*pi/2-pi/2)*80+100
            y1 = sin(a*pi/2-pi/2)*80+100
            x2 = cos(a*pi/2-pi/2)*85+100
            y2 = sin(a*pi/2-pi/2)*85+100
            self.montre.create_line(x1,y1,x2,y2,width=2)
            a += 1
        b = 0
        while b < 2*pi:
            x_1 = cos(b)*80+100
            y_1 = sin(b)*80+100
            x_2 = cos(b)*85+100
            y_2 = sin(b)*85+100
            self.montre.create_line(x_1,y_1,x_2,y_2,width=1)
            b += pi/6
        time = localtime()
        h = time[3]
        m = time[4]
        s = time[5]
        # Aiguille des heures
        if h <= 12:
            self.h = self.montre.create_line(100,100,
                                    cos(h*pi/6-pi/2+m*(pi/360))*50+100,
                                    sin(h*pi/6-pi/2+m*(pi/360))*50+100,
                                             width=1.5)
        if h > 12:
            self.h = self.montre.create_line(100,100,
                                   cos((h-12)*pi/6-pi/2+m*(pi/360))*50+100,
                                   sin((h-12)*pi/6-pi/2+m*(pi/360))*50+100,
                                             width=1.5)
        # Aiguille des minutes
        self.m = self.montre.create_line(100,100,
                                cos(m*pi/30-pi/2)*60+100,
                                sin(m*pi/30-pi/2)*60+100,
                                         width=1.2)
        # Aiguille des secondes
        self.s = self.montre.create_line(100,100,
                                cos(s*pi/30-pi/2)*75+100,
                                sin(s*pi/30-pi/2)*75+100)
        self.master.after(1000,self.heure)
        self.grid()

    def heure(self):
        time = localtime()
        h = time[3]
        m = time[4]
        s = time[5]
        # Aiguille des heures
        if h <= 12:
            self.montre.coords(self.h,100,100,
                                    cos(h*pi/6-pi/2+m*(pi/360))*50+100,
                                    sin(h*pi/6-pi/2+m*(pi/360))*50+100)
        if h > 12:
            self.montre.coords(self.h,100,100,
                                   cos((h-12)*pi/6-pi/2+m*(pi/360))*50+100,
                                   sin((h-12)*pi/6-pi/2+m*(pi/360))*50+100)
        # Aiguille des minutes
        self.montre.coords(self.m,100,100,
                                cos(m*pi/30-pi/2)*60+100,
                                sin(m*pi/30-pi/2)*60+100)
        # Aiguille des secondes
        self.montre.coords(self.s,100,100,
                                cos(s*pi/30-pi/2)*75+100,
                                sin(s*pi/30-pi/2)*75+100)
        self.master.after(1000,self.heure)


class MenuBar(Frame):
    "classe d'une menu"
    def __init__(self,boss):
        Frame.__init__(self)
        self.quitter = Menubutton(self,text="Quitter",bd=2,relief=RAISED)
        menu1 = Menu(self.quitter)
        menu1.add_command(label="Quitter",command=boss.quitter)
        self.quitter.configure(menu=menu1)
        self.quitter.grid(pady=2)


class Montre(Frame):
    "classe d'une montre"
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Montre")
        self.menu = MenuBar(self)
        self.menu.grid(row=0)
        self.mec = MecWatch()
        self.mec.grid(row=1,padx=2,pady=2)
        self.elec = ElWatch()
        self.elec.grid(row=2,pady=4)

    def quitter(self):
        self.msg = Toplevel(self)
        self.msg.title("Quitter")
        Label(self.msg,text="Voulez-vous vraiment \
quitter la montre?").grid(row=1,column=1,columnspan=2,padx=2,pady=2)
        bouq = Button(self.msg,text="Oui",command=self.master.quit,
                      width=10)
        bouq.grid(row=2,column=1,pady=2)
        boua = Button(self.msg,text="Annuler",command=self.annuler,
                      width=10)
        boua.grid(row=2,column=2,pady=2)

    def annuler(self):
        self.msg.destroy()

Montre().mainloop()
