from tkinter import *
import numpy as np
from tkinter.messagebox import showinfo
root = Tk()
root['bg']='#000000'
root.title('X0')
root.geometry('300x300' f"+{(root.winfo_screenwidth() - 300) // 2}+{(root.winfo_screenheight() - 300) // 2}")
root.resizable(width=False, height=False)
matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
d=0
e=0
def endgame(end):
    for i in range(3):
        for j in range(3):
            exec(f'btn{i}{j}["text"] = " "')
            matrix[i,j] = 0
    if end == 1:
        showinfo(title="Игра завершена", message="Победили крестики!")
    elif end == 3:
        showinfo(title="Игра завершена", message="Ничья!")
    else:
        showinfo(title="Игра завершена", message="Победили нолики!")
def check():
    global e
    for i in range(3):
        if matrix[i,0] == matrix[i,1] == matrix[i,2] and matrix[i,0] != 0:
            endgame(matrix[i,0])
        if matrix[0,i] == matrix[1,i] == matrix[2,i] and matrix[0,i] != 0:
            endgame(matrix[0,i])
        if matrix[0,0] == matrix[1,1] == matrix[2,2] and matrix[0,0] != 0:
            endgame(matrix[0,0]) 
        if matrix[0,2] == matrix[1,1] == matrix[2,0] and matrix[1,1] != 0:
            endgame(matrix[1,1] == 1)
    for i in range(3):
        for j in range(3):
            if matrix[i,j] != 0:
                e=1+e  
                if e == 9:
                    endgame(3) 
            else: e=0
def bb(event, button, btn, ii, jj):
    global d
    if button == " ":
        if d==0:
            btn["text"] = "X"
            d+=1
            matrix[jj, ii] = 1
            check()
        elif d==1:
            btn["text"] = "0"
            d-=1
            matrix[jj, ii] = 2
            check()
frame=Frame(root, bg='black')
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
for i in range(3):
    for j in range(3):
        exec(f'btn{i}{j}= Button(frame, text=" ", font=(50))') 
        exec(f'btn{i}{j}.bind("<Button-1>", lambda event: bb(event, btn{i}{j}["text"], btn{i}{j}, {i}, {j}))')
        exec(f'btn{i}{j}.configure(height=2, width=4)')
        exec(f'btn{i}{j}.grid(column=i, row=j, ipadx=7, ipady=4, padx=6, pady=4)')  
root.mainloop()