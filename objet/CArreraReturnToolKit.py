from multiprocessing.context import BufferTooShort
from platform import win32_ver
from tkinter import*

from lxml.html.builder import FRAME
from pyparsing import withClass

from librairy.travailJSON import *
from librairy.dectectionOS import *

class CArreraReturnToolKit :
    def __init__(self,debugConf:str):
        configFile = jsonWork(debugConf)
        self.__name = configFile.lectureJSON("NameSoft")
        self.__color = configFile.lectureJSON("color")
        self.__textcolor = configFile.lectureJSON("textColor")
        self.__styleTextTitle = ("Arial",25)
        self.__styleText = ("Arial", 15)

    def active(self):
        # Creation de la fenetre
        win = Toplevel()
        win.title(self.__name)
        if (OS().osLinux() == True):

            win.maxsize(500, 635)
            win.minsize(500, 635)
        else:
            win.maxsize(500, 610)
            win.minsize(500, 610)
        win.configure(bg=self.__color)
        # Frame
        frameBTN = Frame(win,width=400,height=400,bg="red")
        # Widget
        # Win
        labelTitle = Label(win,text=self.__name,
                           bg=self.__color,
                           font=self.__styleTextTitle,fg=self.__textcolor)
        btnQuit = Button(win,text="Quitter",bg=self.__color,
                         fg=self.__textcolor,font=self.__styleText)
        # Affichage
        frameBTN.place(relx=0.5, rely=0.5, anchor="center")
        labelTitle.pack()
        btnQuit.pack(side="bottom")