'''
===============================================================================
Creator = Helia Sadat Hashemi Aghdam
Nov 2022
===============================================================================
Project Subject = X and O character detection with Hebb Algorithm
===============================================================================
'''

from tkinter import *
from tkinter import messagebox
import tkinter as tk
from functools import partial


#create gui window
gui = Tk()
gui.geometry("450x450")
var = StringVar()
gui.title('Character Detection')

# hebb algorithm
def hebbian(entry):
    train_data = []
    weight = [0] * 25
    bias = 0
    entry = entry[:-1]
    read_dataset = (open("./Dataset.txt")).readlines()
    for a in read_dataset:
        temp = [int(z) for z in a.split(',')[:-1]]
        if a.split(',')[-1] == "1\n":
            temp.append(1)
        else:
            temp.append(-1)
        train_data.append(temp)
    
    for test in train_data:
        if len(test)== 26:

            for d in range(25):
                weight[d] += (test[d] * test[-1])
            bias += (1 * test[25])
    
    total = bias
    for i in range(25):
        total += weight[i] * entry[i]
        
    if total >= 0:
        messagebox.showwarning("Success", "Character is X")
    elif total < 0:
        messagebox.showwarning("Success", "Character is O")
    else:
        messagebox.showwarning("Error", "Try again")
    

#get data and add to the dataset.txt file .

def get_data(data,  n):
    if(n == 1):
        hebbian(data)
    elif var.get() == "X":
        data[25] = 1
        open("./Dataset.txt", "a+").write(",".join(str(q)
                                                   for q in data) + "\n")
        messagebox.showwarning("Success", "Saved data successfully")

    elif var.get() == "O":
        data[25] = -1
        
        open("./Dataset.txt", "a+").write(",".join(str(r)
                                                   for r in data) + "\n")
        messagebox.showwarning("Success", "Saved data successfully")

    else:
        messagebox.showwarning("Error", "Invalid Data")

#selecting button with click action and change button color and value in data.

def select_button(widget,n, arr):
    m = widget['text']
    if(arr[m] == 1):
        widget['bg'] = 'white'
        arr[m] = -1
    else:
        widget['bg'] = 'black'
        arr[m] = 1


# clear 
def clear(arr , btns):
    for x in range(len(arr)):
        if arr[x] == 1:
            arr[x] = -1
    for i in btns:
        i['bg'] = "white"
    
    
#create buttons

global arr
arr = [-1] * 26
btns = []

for i in range(25):
    btn = tk.Button(gui, text=i, bg="white",fg="black",borderwidth=10, height=10, width=15,)
    btn.config(command=lambda arg=btn : select_button(arg, i, arr))
    btn.grid(row=i // 5, column=i % 5, sticky='w')
    btns.append(btn)
n_rows = 5
n_columns = 5
for i in range(n_rows):
    for j in range(n_columns):
        gui.grid_rowconfigure(i, weight=1)
        gui.grid_columnconfigure(j, weight=1)


# functional buttons
R_X = Radiobutton(gui, text="X",value='X',font= 'Iphone 10 bold',variable=var)
R_X.grid(row=7, column=0)

R_O = Radiobutton(gui, text="O",value='O',font= 'Iphone 10 bold', variable=var)
R_O.grid(row=7, column=1)

button1 = Button(gui, text="Add to data",font= 'Iphone 10 bold',borderwidth=5,command=partial(get_data, arr, 0), 
                 width=9, background="orange")
button1.grid(row=7, column=2)

button2 = Button(gui, text="Predict",font= 'Iphone 10 bold',borderwidth=5,command=partial(get_data, arr, 1), 
                 width=9, background="white")
button2.grid(row=7, column=4)

button3 = Button(gui, text="clear",font= 'Iphone 10 bold',borderwidth=5,command=partial(clear, arr, btns), 
                 width=9, background="gray")
button3.grid(row=7, column=3)


mainloop()
