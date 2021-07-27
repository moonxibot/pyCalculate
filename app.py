from tkinter import *

window = Tk()
window.title("미니 계산기")

def buttonClick(key):
    if key == "=":
        result = str(eval(inputEntry.get()))
        inputEntry.delete(0, END)
        inputEntry.insert(END, str(result))
    elif key == "C":
        inputEntry.delete(0, END)
    else:
        inputEntry.insert(END, str(key))

inputEntry = Entry(window, width=27, bg="skyblue", fg="black")
inputEntry.grid(row=0, column=0, columnspan=5)

buttonList = [
'7',  '8',  '9',  '/',  'C',
'4',  '5',  '6',  '*',  ' ',
'1',  '2',  '3',  '-',  ' ',
'0',  '.',  '=',  '+',  ' ' ]

row = 1
column = 0

for i in buttonList:
    Button(window, text=i, width=5,height=2,command=lambda arg=i:buttonClick(arg)).grid(column=column, row=row)

    column += 1
    if column > 4:
        column = 0
        row += 1

window.mainloop()
