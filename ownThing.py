import tkinter
def continueOrNot():
    global again
    if var1.get() == 0 and var2.get() == 1:
        again = "no"
    elif var1.get() == 1 and var2.get() == 0:
        again = "yes"
    var1.set(0)
    var2.set(0)
    epicScreen.destroy()

while True:
    try:
        number = int(input("Vul een nummer in: "))
    except ValueError:
        print("AAAAAAAAAAAAAA DAT WAS GEEN NUMMER!!!")
    else:
        print("goed gedaan meneer.")
    epicScreen = tkinter.Tk()
    epicScreen.attributes("-topmost", True)
    var1 = tkinter.IntVar()
    var2 = tkinter.IntVar()
    text = tkinter.Label(text="Wil je verder gaan?",font=("Comic_Sans", 20)).pack()
    c1 = tkinter.Checkbutton(epicScreen, text='ja',variable=var1, onvalue=1, offvalue=0, command=continueOrNot)
    c1.pack()
    c2 = tkinter.Checkbutton(epicScreen, text='nee',variable=var2, onvalue=1, offvalue=0, command=continueOrNot)
    c2.pack()
    epicScreen.mainloop()
    if again == "no":
        print("sad moment")
        break