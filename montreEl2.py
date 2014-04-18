# -*- coding:Latin-1 -*-

from Tkinter import *
from time import localtime

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

f = ElWatch()
