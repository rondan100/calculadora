from tkinter import *
import math 

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="black")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add("*Font", "arial 20 bold")
        self.pack(expand=YES, fill=Y)
        self.master.title("Calculator")
        

        display = StringVar()
        hist = StringVar()
        # relief can be FLAT or RIDGE or RAISED or SUNKEN GROOVE
        E1 = Entry(self, relief=RIDGE, textvariable=display, width=20,justify='right', bd=10, bg='darkgray')
        E1.pack(side=TOP, expand=YES, fill=BOTH)

        Label(self, relief=FLAT, textvariable=hist,height = 5, width=20, font="arial 15 bold", anchor="ne", justify='right', bd=10, bg='darkgray').pack(side=TOP, expand=YES, fill=BOTH)

        erase = iCalc(self, TOP)
        for clearBut in ("C","<"):          
            for ichar in clearBut:
                if clearBut == "C":
                    button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(""))
                else:
                    button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: E1.delete(len(display.get())-1), )
        for numBut in ("789/", "456*", "123-", ".0+"):
            functionNum = iCalc(self, TOP)
            for char in numBut:
                button(functionNum, LEFT, char, lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))
        equalButton = iCalc(self, TOP)
        for iEqual in ("=","raiz"):
            if iEqual == "=":
                btniEqual = button(equalButton, RIGHT, iEqual)
                btniEqual.bind("<ButtonRelease-1>", lambda e, s=self, storeObj=display, h=hist: s.calc(storeObj, h), '+')
            else:
                btniEqual = button(equalButton, LEFT, iEqual, lambda storeObj=display, s='%s' % iEqual: storeObj.set("math.sqrt(" + storeObj.get() + ")"))

    def calc(self, display, hist):
        try:
            if hist.get():
                hist.set(display.get() + "\n" + hist.get())
            else:
                hist.set(hist.get() + display.get())
            
            display.set(eval(display.get()))
            hist.set(hist.get() + " = " + display.get())
        except:
            display.set("ERROR")

if __name__ == '__main__':
    app().mainloop()
