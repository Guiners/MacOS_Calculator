from tkinter import *

# declaring variables
screen = Tk()
x = 230
y = 300
display_y = 64
screen.geometry("230x298")
screen.resizable(0, 0)
screen.title("Kalkulator")
large_font = ("Verdana", 15)
screen_font = ("Verdana", 40)
screen.var = []
screen.var1 = []
screen.var2 = []
screen.function = IntVar()
screen.function = 0
screen.y = BooleanVar()
button_x = x / 4
button_y = (y - display_y) / 5
f = 9


def screen_display(val):
    if type(val) == float:
        display_length = len(str(round(val, 8))) - len(str(round(val)))
        display = round((val), display_length)
        show_display = Label(
            screen, text=display, font=screen_font, bg="grey", anchor=E, fg="white"
        )
        show_display.place(height=display_y, width=x, x=0, y=0)
    elif type(val) == int:
        show_display = Label(
            screen, text=val, font=screen_font, bg="grey", anchor=E, fg="white"
        )
        show_display.place(height=display_y, width=x, x=0, y=0)
    elif type(val) == list:
        if len(val) > 0:
            display = ""
            display = "".join(str(i) for i in screen.var)
            show_display = Label(
                screen, text=display, font=screen_font, bg="grey", anchor=E, fg="white"
            )
            show_display.place(height=display_y, width=x, x=0, y=0)
        else:
            show_display = Label(
                screen, text=val, font=screen_font, bg="grey", anchor=E, fg="white"
            )
            show_display.place(height=display_y, width=x, x=0, y=0)


def add(number):
    if type(screen.var) == list:
        if number == "." and len(screen.var) == 0:
            screen.var.append(str(0))
            screen.var.append(str(number))
            screen_display(screen.var)
        else:
            screen.var.append(str(number))
            screen_display(screen.var)
    else:
        screen.var = str(screen.var)
        screen.var = list(screen.var)
        if number == "." and len(screen.var) == 0:
            screen.var.append(str(0))
            screen.var.append(str(number))
            screen_display(screen.var)
        else:
            screen.var.append(str(number))
            screen_display(screen.var)
        screen.var.append(number)
        screen_display(screen.var)


def dele():
    if type(screen.var) == list:
        screen.var.pop()
        screen_display(screen.var)
    else:
        screen.var = str(screen.var)
        screen.var = list(screen.var)
        screen.var.pop()
        screen_display(screen.var)


def reseting_var():
    screen.var1 = []
    screen.var2 = []


def equal():
    if type(screen.var) != list:
        screen.var = str(screen.var)
        screen.var = list(screen.var)

    for char in screen.var:
        if char == ".":
            screen.y = True
            break
        else:
            screen.y = False

        string_number = [str(char) for char in screen.var]
        screen.var2 = "".join(string_number)
        if screen.y:
            screen.var2 = float(screen.var2)
        elif not screen.y:
            screen.var2 = int(screen.var2)
        screen.var = []

    if screen.function == 1:
        if type(screen.var) == list:
            screen.var = screen.var1 + screen.var2
            screen_display(screen.var)
            reseting_var()
        else:
            screen.var = str(screen.var)
            screen.var = list(screen.var)
            screen.var = screen.var1 + screen.var2
            screen_display(screen.var)
            reseting_var()

    elif screen.function == 2:
        if type(screen.var) == list:
            screen.var = screen.var1 - screen.var2
            screen_display(screen.var)
            reseting_var()
        else:
            screen.var = str(screen.var)
            screen.var = list(screen.var)
            screen.var = screen.var1 - screen.var2
            screen_display(screen.var)
            reseting_var()

    elif screen.function == 3:
        if type(screen.var) == list:
            screen.var = screen.var1 * screen.var2
            screen_display(screen.var)
            reseting_var()
        else:
            screen.var = str(screen.var)
            screen.var = list(screen.var)
            screen.var = screen.var1 * screen.var2
            screen_display(screen.var)
            reseting_var()

    elif screen.function == 4:
        if screen.var2 != 0:
            if type(screen.var) == list:
                screen.var = screen.var1 / screen.var2
                print(screen.var)
                if round(screen.var) == screen.var:
                    screen.var = int(screen.var)
                    screen_display((screen.var))
                    reseting_var()
                else:
                    screen_display((screen.var))
                    reseting_var()
            else:
                screen.var = str(screen.var)
                screen.var = list(screen.var)
                screen.var = screen.var1 / screen.var2
                if round(screen.var) == screen.var:
                    screen.var = int(screen.var)
                    screen_display((screen.var))
                    reseting_var()
                else:
                    screen_display((screen.var))
                    reseting_var()
    screen.function = 0


def convert(number):
    if type(screen.var) != list:
        screen.var = str(screen.var)
        screen.var = list(screen.var)

    screen.function = number
    for char in screen.var:
        if char == ".":
            screen.y = True
            break
        else:
            screen.y = False

        string_number = [str(char) for char in screen.var]
        screen.var2 = "".join(string_number)
        if screen.y:
            screen.var2 = float(screen.var2)
        elif not screen.y:
            screen.var2 = int(screen.var2)
        screen.var = []
    screen_display(screen.var)


def change():
    if screen.var[0] == "-":
        screen.var.pop(0)
        screen_display(screen.var)

    elif screen.var[0] != "-":
        screen.var.insert(0, "-")
        screen_display(screen.var)


# screen where the numbers are
screen_display(screen.var)


button_del = Button(
    screen,
    text="AC",
    font=large_font,
    command=lambda: dele(),
    highlightbackground="black",
    fg="white",
)
button_del.place(height=button_y, width=button_x, x=0, y=display_y)

button_negative_or_positive = Button(
    screen,
    text="+/-",
    font=large_font,
    command=lambda: change(),
    highlightbackground="black",
    fg="white",
)
button_negative_or_positive.place(
    height=button_y, width=button_x, x=button_x, y=display_y
)

button_percentages = Button(
    screen,
    text="%",
    command=lambda: add(0),
    font=large_font,
    highlightbackground="black",
    fg="white",
)
button_percentages.place(
    height=button_y, width=button_x, x=button_x + button_x, y=display_y
)

button_add = Button(
    screen,
    text="÷",
    font=large_font,
    command=lambda: convert(4),
    highlightbackground="orange",
    fg="white",
)
button_add.place(
    height=button_y, width=button_x, x=button_x + button_x + button_x, y=display_y
)


button7 = Button(
    screen,
    text="7",
    font=large_font,
    command=lambda: add(7),
    highlightbackground="black",
    fg="white",
)
button7.place(height=button_y, width=button_x, x=0, y=display_y + button_y)

button8 = Button(
    screen,
    text="8",
    font=large_font,
    command=lambda: add(8),
    highlightbackground="black",
    fg="white",
)
button8.place(height=button_y, width=button_x, x=button_x, y=display_y + button_y)

button9 = Button(
    screen,
    text="9",
    font=large_font,
    command=lambda: add(9),
    highlightbackground="black",
    fg="white",
)
button9.place(
    height=button_y, width=button_x, x=button_x + button_x, y=display_y + button_y
)

button_min = Button(
    screen,
    text="×",
    font=large_font,
    command=lambda: convert(3),
    highlightbackground="orange",
    fg="white",
)
button_min.place(
    height=button_y,
    width=button_x,
    x=button_x + button_x + button_x,
    y=display_y + button_y,
)


button4 = Button(
    screen,
    text="4",
    font=large_font,
    command=lambda: add(4),
    highlightbackground="black",
    fg="white",
)
button4.place(height=button_y, width=button_x, x=0, y=display_y + button_y + button_y)

button5 = Button(
    screen,
    text="5",
    font=large_font,
    command=lambda: add(5),
    highlightbackground="black",
    fg="white",
)
button5.place(
    height=button_y, width=button_x, x=button_x, y=display_y + button_y + button_y
)

button6 = Button(
    screen,
    text="6",
    font=large_font,
    command=lambda: add(6),
    highlightbackground="black",
    fg="white",
)
button6.place(
    height=button_y,
    width=button_x,
    x=button_x + button_x,
    y=display_y + button_y + button_y,
)

button_multiply = Button(
    screen,
    text="−",
    font=large_font,
    command=lambda: convert(2),
    highlightbackground="orange",
    fg="white",
)
button_multiply.place(
    height=button_y,
    width=button_x,
    x=button_x + button_x + button_x,
    y=display_y + button_y + button_y,
)


button1 = Button(
    screen,
    text="1",
    font=large_font,
    command=lambda: add(1),
    highlightbackground="black",
    fg="white",
)
button1.place(
    height=button_y,
    width=button_x,
    x=0,
    y=display_y + button_y + button_y + button_y - 1,
)

button2 = Button(
    screen,
    text="2",
    font=large_font,
    command=lambda: add(2),
    highlightbackground="black",
    fg="white",
)
button2.place(
    height=button_y,
    width=button_x,
    x=button_x,
    y=display_y + button_y + button_y + button_y - 1,
)

button3 = Button(
    screen,
    text="3",
    font=large_font,
    command=lambda: add(3),
    highlightbackground="black",
    fg="white",
)
button3.place(
    height=button_y,
    width=button_x,
    x=button_x + button_x,
    y=display_y + button_y + button_y + button_y - 1,
)

button_divide = Button(
    screen,
    text="+",
    font=large_font,
    command=lambda: convert(1),
    highlightbackground="orange",
    fg="white",
)
button_divide.place(
    height=button_y,
    width=button_x,
    x=button_x + button_x + button_x,
    y=display_y + button_y + button_y + button_y - 1,
)

# fifth row of buttons
button0 = Button(
    screen,
    text="0",
    font=large_font,
    command=lambda: add(0),
    highlightbackground="black",
    fg="white",
)
button0.place(
    height=button_y,
    width=button_x + button_x,
    x=0,
    y=display_y + button_y + button_y + button_y + button_y - 1,
)

button_comma = Button(
    screen,
    text=",",
    font=large_font,
    command=lambda: add("."),
    highlightbackground="black",
    fg="white",
)
button_comma.place(
    height=button_y,
    width=button_x,
    x=button_x + button_x,
    y=display_y + button_y + button_y + button_y + button_y - 1,
)

button_equal = Button(
    screen,
    text="=",
    font=large_font,
    command=lambda: equal(),
    highlightbackground="orange",
    fg="white",
)
button_equal.place(
    height=button_y,
    width=button_x,
    x=button_x + button_x + button_x,
    y=display_y + button_y + button_y + button_y + button_y - 1,
)


screen.mainloop()
