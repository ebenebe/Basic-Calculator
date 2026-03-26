
import tkinter as tk


root = tk.Tk()
root.title('Calculator')
e = tk.Entry(root,width=35,borderwidth=3)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,tk.END)
    e.insert(0,str(current)+ str(number))


def button_clear():
    e.delete(0,tk.END)

def button_add():
    first_number = e.get()
    global f_num 
    global operation
    operation = 'addition'
    f_num = float(first_number)
    e.delete(0,tk.END)


def button_equal():
    second_number = e.get()
    e.delete(0,tk.END)

    if operation == 'addition':
        e.insert(0,f_num + float(second_number))
    elif operation == 'subtraction':
        e.insert(0,f_num - float(second_number))
    elif operation == 'multiplication':
        e.insert(0,f_num * float(second_number))
    elif operation == 'division':
        try:
            e.insert(0,f_num / float(second_number))
        except ZeroDivisionError:
            e.insert(0, "Error")



def button_subtract():
    first_number = e.get()
    global f_num 
    global operation
    operation = 'subtraction'
    f_num = float(first_number)
    e.delete(0,tk.END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global operation
    operation = 'multiplication'
    f_num = float(first_number)
    e.delete(0,tk.END)

def button_divide():
    first_number = e.get()
    global f_num 
    global operation
    operation = 'division'
    f_num = float(first_number)
    e.delete(0,tk.END)




b1 = tk.Button(root,text='1', padx=40,pady=20, command= lambda:button_click(1))
b2 = tk.Button(root,text='2', padx=40,pady=20, command= lambda:button_click(2))
b3 = tk.Button(root,text='3', padx=40,pady=20, command= lambda:button_click(3))
b4 = tk.Button(root,text='4', padx=40,pady=20, command= lambda:button_click(4))
b5 = tk.Button(root,text='5', padx=40,pady=20, command= lambda:button_click(5))
b6 = tk.Button(root,text='6', padx=40,pady=20, command= lambda:button_click(6))
b7 = tk.Button(root,text='7', padx=40,pady=20, command= lambda:button_click(7))
b8 = tk.Button(root,text='8', padx=40,pady=20, command= lambda:button_click(8))
b9 = tk.Button(root,text='9', padx=40,pady=20, command= lambda:button_click(9))
b0 = tk.Button(root,text='0', padx=40,pady=20, command= lambda:button_click(0))
b_dot = tk.Button(root,text='.', padx=40,pady=20, command= lambda:button_click('.'))


b_add = tk.Button(root,text='+', padx=40,pady=20, command= button_add)
b_equal = tk.Button(root,text='=', padx=80,pady=20, command= button_equal)
b_clear = tk.Button(root,text='Clear', padx=40,pady=20, command= button_clear)

b_subtract = tk.Button(root,text='-', padx=40,pady=20, command= button_subtract)
b_multiply = tk.Button(root,text='*', padx=40,pady=20, command= button_multiply)
b_divide = tk.Button(root,text='/', padx=40,pady=20, command= button_divide)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
b_dot.grid(row=4,column=1)

b_add.grid(row=5,column=0)
b_clear.grid(row=4,column=2)
b_equal.grid(row=5,column=1,columnspan=6)

b_subtract.grid(row=6,column=0)
b_multiply.grid(row=6,column=1)
b_divide.grid(row=6,column=2)

root.mainloop()






    


