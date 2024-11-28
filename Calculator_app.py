from tkinter import *
gui=Tk()
gui.title("Calculator")
#gui.geometry("300x200")
gui.configure(bg="steel blue")
#add ,subtract,multiply,divide,percent functions
def _click(number):
    current=en.get() #saves whatever number in the input box to the variable current
    en.delete(0,END) #delete whatever inside the input box
    en.insert(0,str(current)+str(number))

def _add():
    global f_number
    first_number=en.get()
    f_number=int(first_number)
    global math
    math="addition"
    en.delete(0,END)

def _minus():
    global f_number
    first_number = en.get()
    f_number = int(first_number)
    global math
    math="subtraction"
    en.delete(0, END)
def _multiplication():
    global f_number
    first_number = en.get()
    f_number = int(first_number)
    global math
    math = "multiplication"
    en.delete(0, END)

def _division():
    global f_number
    first_number = en.get()
    f_number = int(first_number)
    global math
    math="division"
    en.delete(0, END)
def _percentage():
    global f_number
    first_number = en.get()
    f_number = int(first_number)
    global math
    math = "percentage"
    en.delete(0, END)

def _clear():
    en.delete(0,END)

def _ans():
    ans=en.get()
    ans=int(ans)
    en.delete(0,END)
    en.insert(0,ans)

def _equal():
    global math
    s_number=en.get()
    en.delete(0,END)
    if math=="addition":
         en.insert(0,f_number+int(s_number))
    if math=="subtraction":
        en.insert(0, f_number-int(s_number))
    if math == "multiplication":
        en.insert(0, f_number *int(s_number))
    if math == "division":
        en.insert(0, f_number / int(s_number))
    if math == "percentage":
        en.insert(0, f_number % int(s_number))

#define input screen
en=Entry(gui,width=40,borderwidth=8)
en.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


#define Buttons
#(name of your gui,the button text,length,width,command requested)
#Note : each button is separated automatically 10 xpixels from each other
button_0=Button(gui,text="0",padx=40,pady=25,command=lambda:_click(0),bg="turquoise2")
button_1=Button(gui,text="1",padx=40,pady=25,command=lambda:_click(1),bg="turquoise2")
button_2=Button(gui,text="2",padx=40,pady=25,command=lambda:_click(2),bg="turquoise2")
button_3=Button(gui,text="3",padx=40,pady=25,command=lambda:_click(3),bg="turquoise2")
button_4=Button(gui,text="4",padx=40,pady=25,command=lambda:_click(4),bg="turquoise2")
button_5=Button(gui,text="5",padx=40,pady=25,command=lambda:_click(5),bg="turquoise2")
button_6=Button(gui,text="6",padx=40,pady=25,command=lambda:_click(6),bg="turquoise2")
button_7=Button(gui,text="7",padx=40,pady=25,command=lambda:_click(7),bg="turquoise2")
button_8=Button(gui,text="8",padx=40,pady=25,command=lambda:_click(8),bg="turquoise2")
button_9=Button(gui,text="9",padx=40,pady=25,command=lambda:_click(9),bg="turquoise2")

button_plus=Button(gui,text="+",padx=40,pady=25,command=_add,bg="turquoise2")
button_minus=Button(gui,text="-",padx=40,pady=25,command=_minus,bg="turquoise2")
button_multiply=Button(gui,text="x",padx=40,pady=25,command=_multiplication,bg="turquoise2")
button_divide=Button(gui,text="/",padx=40,pady=25,command=_division,bg="turquoise2")
button_percentage=Button(gui,text="%",padx=40,pady=25,command=_percentage,bg="turquoise2")
button_equal=Button(gui,text="=",padx=40,pady=25,command=_equal,bg="turquoise2")

button_clear=Button(gui,text="Clear",padx=30,pady=25,command=_clear,bg="white")
button_ans=Button(gui,text="ANS",padx=30,pady=25,command=_ans,bg="white")

#Positioning buttons and put them on the screen
button_9.grid(column=0,row=1)
button_8.grid(column=1,row=1)
button_7.grid(column=2,row=1)

button_6.grid(column=0,row=2)
button_5.grid(column=1,row=2)
button_4.grid(column=2,row=2)

button_3.grid(column=0,row=3)
button_2.grid(column=1,row=3)
button_1.grid(column=2,row=3)

button_0.grid(column=0,row=4)

button_clear.grid(column=1,row=4)  #cloumn span=2 to take the size of two columns
button_ans.grid(column=2,row=4)

button_equal.grid(column=2,row=5)
button_plus.grid(column=0,row=5)
button_minus.grid(column=1,row=5)
button_multiply.grid(column=0,row=6)
button_divide.grid(column=1,row=6)
button_percentage.grid(column=2,row=6)


gui.mainloop()
