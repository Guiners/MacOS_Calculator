from tkinter import *


# declaring variables
screen = Tk()
x = 230
y = 300
e_y = 64
screen.geometry("230x298")
screen.resizable(0, 0)
screen.title("Kalkulator")
large_font = ('Verdana', 15)
screen_font = ('Verdana', 40)
screen.var = []
screen.var1 = []
screen.var2 = []
screen.function = IntVar()
screen.function = 0
screen.y = BooleanVar()
button_x = (x/4)
button_y = ((y - e_y)/5)
f = 9


# blue screen
def ekran(val):
    if type(val) == float:
        n = len(str(round(val, 8))) - len(str(round(val)))
        kopa = round((val), n)
        e = Label(screen, text=kopa, font=screen_font, bg="grey", anchor=E, fg="white")
        e.place(height=e_y, width=x, x=0, y=0)
    elif type(val) == int:
        e = Label(screen, text=val, font=screen_font, bg="grey", anchor=E, fg="white")
        e.place(height=e_y, width=x, x=0, y=0)
    elif type(val) == list:
        if len(val) > 0:
            kopa = ''
            kopa = ''.join(str(i) for i in screen.var)
            e = Label(screen, text=kopa, font=screen_font, bg="grey", anchor=E, fg="white")
            e.place(height=e_y, width=x, x=0, y=0)
        else:
            e = Label(screen, text=val, font=screen_font, bg="grey", anchor=E, fg="white")
            e.place(height=e_y, width=x, x=0, y=0)


# adding numbers on blue screen
def add(x):
    if type(screen.var) == list:
        if x == "." and len(screen.var) == 0:
            screen.var.append(str(0))
            screen.var.append(str(x))
            ekran(screen.var)
        else:
            screen.var.append(str(x))
            ekran(screen.var)
    else:
        screen.var = str(screen.var)
        screen.var = list(screen.var)
        if x == "." and len(screen.var) == 0:
            screen.var.append(str(0))
            screen.var.append(str(x))
            ekran(screen.var)
        else:
            screen.var.append(str(x))
            ekran(screen.var)
        screen.var.append(x)
        ekran(screen.var)


# removing numbers on blue screen
def dele():
    if type(screen.var) == list:
        screen.var.pop()
        ekran(screen.var)
    else:
        screen.var = str(screen.var)
        screen.var = list(screen.var)
        screen.var.pop()
        ekran(screen.var)


# it should work like changing list to int but its incomplite
def reseting_var():
    screen.var1 = []
    screen.var2 = []


def equal():
    if type(screen.var) != list:
        screen.var = str(screen.var)
        screen.var = list(screen.var)

    for i in screen.var:
        if i == ".":
            screen.y = True
            break
        else:
            screen.y = False

    if screen.y == True:
        s = [str(i) for i in screen.var]
        screen.var2 = "".join(s)
        screen.var2 = float(screen.var2)
        screen.var = []
    elif screen.y == False:
        s = [str(i) for i in screen.var]
        screen.var2 = "".join(s)
        screen.var2 = int(screen.var2)
        screen.var = []


    if screen.function == 1:
        if type(screen.var) == list:
            screen.var = screen.var1 + screen.var2
            ekran(screen.var)
            reseting_var()
        else:
            screen.var = str(screen.var)
            screen.var = list(screen.var)
            screen.var = screen.var1 + screen.var2
            ekran(screen.var)
            reseting_var()

    elif screen.function == 2:
        if type(screen.var) == list:
            screen.var = screen.var1 - screen.var2
            ekran(screen.var)
            reseting_var()
        else:
            screen.var = str(screen.var)
            screen.var = list(screen.var)
            screen.var = screen.var1 - screen.var2
            ekran(screen.var)
            reseting_var()

    elif screen.function == 3:
        if type(screen.var) == list:
            screen.var = screen.var1 * screen.var2
            ekran(screen.var)
            reseting_var()
        else:
            screen.var = str(screen.var)
            screen.var = list(screen.var)
            screen.var = screen.var1 * screen.var2
            ekran(screen.var)
            reseting_var()

    elif screen.function == 4:
        if screen.var2 != 0:
            if type(screen.var) == list:
                screen.var = screen.var1 / screen.var2
                print(screen.var)
                if round(screen.var) == screen.var:
                   screen.var = int(screen.var)
                   ekran((screen.var))
                   reseting_var()
                else:
                    ekran((screen.var))
                    reseting_var()
            else:
                screen.var = str(screen.var)
                screen.var = list(screen.var)
                screen.var = screen.var1 / screen.var2
                if round(screen.var) == screen.var:
                    screen.var = int(screen.var)
                    ekran((screen.var))
                    reseting_var()
                else:
                    ekran((screen.var))
                    reseting_var()
    screen.function = 0
def convert(x):
    if type(screen.var) != list:
        screen.var = str(screen.var)
        screen.var = list(screen.var)

    for i in screen.var:
        if i == ".":
            screen.y = True
            break
        else:
            screen.y = False

    if screen.y == True:
        screen.function = x
        s = [str(i) for i in screen.var]
        screen.var1 = str("".join(s))
        screen.var1 = float(screen.var1)
        screen.var = []
    elif screen.y == False:
        screen.function = x
        s = [str(i) for i in screen.var]
        screen.var1 = int("".join(s))
        screen.var = []
    ekran(screen.var)

def change():
    if screen.var[0] == "-":
        screen.var.pop(0)
        ekran(screen.var)

    elif screen.var[0] != "-":
        screen.var.insert(0, "-")
        ekran(screen.var)


# screen where the numbers are
ekran(screen.var)

# first row of numbers 1,2,3
bdel = Button(screen, text="AC", font=large_font, command=lambda: dele(), highlightbackground = "black", fg = "white")
bdel.place(height=button_y, width=button_x, x=0, y=e_y)

bmp = Button(screen, text="+/-", font=large_font, command=lambda: change(), highlightbackground = "black", fg = "white")
bmp.place(height=button_y, width=button_x, x=  button_x, y=e_y)

bp = Button(screen, text="%", command=lambda: add(0), font=large_font, highlightbackground = "black", fg = "white")
bp.place(height=button_y, width=button_x, x=button_x + button_x, y=e_y)

badd = Button(screen, text="÷", font=large_font, command=lambda: convert(4), highlightbackground = "orange", fg = "white")
badd.place(height=button_y, width=button_x, x=button_x + button_x + button_x, y=e_y)

# second row of numbers 4,5,6
b7 = Button(screen, text="7", font=large_font, command=lambda: add(7), highlightbackground = "black", fg = "white")
b7.place(height=button_y, width=button_x, x=0, y=e_y + button_y)

b8 = Button(screen, text="8", font=large_font, command=lambda: add(8), highlightbackground = "black", fg = "white")
b8.place(height=button_y, width=button_x, x=button_x, y=e_y + button_y)

b9 = Button(screen, text="9", font=large_font, command=lambda: add(9), highlightbackground = "black", fg = "white")
b9.place(height=button_y, width=button_x, x=button_x + button_x, y=e_y + button_y)

bmin = Button(screen, text="×", font=large_font, command=lambda: convert(3), highlightbackground = "orange", fg = "white")
bmin.place(height=button_y, width=button_x, x=button_x + button_x + button_x, y=e_y + button_y)

# third row of numbers 7,8,9
b4 = Button(screen, text="4", font=large_font, command=lambda: add(4),highlightbackground = "black", fg = "white")
b4.place(height=button_y, width=button_x, x=0, y=e_y + button_y + button_y)

b5 = Button(screen, text="5", font=large_font, command=lambda: add(5), highlightbackground = "black", fg = "white")
b5.place(height=button_y, width=button_x, x=button_x, y=e_y + button_y + button_y)

b6 = Button(screen, text="6", font=large_font, command=lambda: add(6), highlightbackground = "black", fg = "white")
b6.place(height=button_y, width=button_x, x=button_x + button_x, y=e_y + button_y + button_y)

bmul = Button(screen, text="−", font=large_font, command=lambda: convert(2), highlightbackground = "orange", fg = "white")
bmul.place(height=button_y, width=button_x, x=button_x + button_x + button_x, y=e_y + button_y + button_y)

# forth row of numbers ".", 0, "del"
b1 = Button(screen, text="1", font=large_font, command=lambda: add(1), highlightbackground = "black", fg = "white")
b1.place(height=button_y, width=button_x, x=0, y=e_y + button_y + button_y + button_y - 1)

b2 = Button(screen, text="2", font=large_font, command=lambda: add(2), highlightbackground = "black", fg = "white")
b2.place(height=button_y, width=button_x, x=button_x, y=e_y + button_y + button_y + button_y -1)

b3 = Button(screen, text="3", font=large_font, command=lambda: add(3), highlightbackground = "black", fg = "white")
b3.place(height=button_y, width=button_x, x=button_x + button_x, y=e_y + button_y + button_y + button_y - 1)

bdiv = Button(screen, text="+", font=large_font, command=lambda: convert(1), highlightbackground = "orange", fg = "white")
bdiv.place(height=button_y, width=button_x, x=button_x + button_x + button_x, y=e_y + button_y + button_y + button_y - 1)

#fifth row of buttons
b0 = Button(screen, text="0", font=large_font, command=lambda: add(0), highlightbackground = "black", fg = "white")
b0.place(height=button_y, width=button_x + button_x, x=0, y=e_y + button_y + button_y + button_y + button_y - 1)

bc = Button(screen, text=",", font=large_font, command=lambda: add("."), highlightbackground = "black", fg = "white")
bc.place(height=button_y, width=button_x , x=button_x + button_x, y=e_y + button_y + button_y + button_y + button_y - 1)

be = Button(screen, text="=", font=large_font, command=lambda: equal(), highlightbackground = "orange", fg = "white")
be.place(height=button_y, width=button_x, x=button_x + button_x + button_x, y=e_y + button_y + button_y + button_y + button_y - 1)


screen.mainloop()
