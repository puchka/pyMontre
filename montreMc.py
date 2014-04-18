# -*- coding:Latin-1 -*-

from Tkinter import *
from time import localtime
from math import sin, cos, pi

class MecWatch(Frame):
    "classe d'un motre mécanique"
    def __init__(self):
        Frame.__init__(self)
        self.montre = Canvas(self,width=200,heigh=200,bg='white')
        self.montre.grid(row=1,column=1)
        
        self.montre.create_oval(15,15,185,185)
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
                                    sin(h*pi/6-pi/2+m*(pi/360))*50+100)
        if h > 12:
            self.h = self.montre.create_line(100,100,
                                   cos((h-12)*pi/6-pi/2+m*(pi/360))*50+100,
                                   sin((h-12)*pi/6-pi/2+m*(pi/360))*50+100)
        # Aiguille des minutes
        self.m = self.montre.create_line(100,100,
                                cos(m*pi/30-pi/2)*60+100,
                                sin(m*pi/30-pi/2)*60+100)
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

f = MecWatch()
