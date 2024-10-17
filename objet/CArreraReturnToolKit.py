from platform import win32_ver
from tkinter import*
from librairy.travailJSON import *
from librairy.dectectionOS import *

class CArreraReturnToolKit :
    def __init__(self,debugConf:str):
        configFile = jsonWork(debugConf)
        self.__name = configFile.lectureJSON("NameSoft")
        self.__color = configFile.lectureJSON("color")
        self.__styleTextTitle = ("Arial",25)
        self.__styleText = ("Arial", 15)

    def active(self):
        win = Toplevel()
        win.title(self.__name)
        if (OS().osLinux() == True):

            win.maxsize(500, 635)
            win.minsize(500, 635)
        else:
            win.maxsize(500, 610)
            win.minsize(500, 610)
        win.configure(bg=self.__color)
        labelTitle = Label(win,text=self.__name,
                           bg=self.__color,font=self.__styleTextTitle)

        labelTitle.pack()