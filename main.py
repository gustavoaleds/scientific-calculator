from tkinter import *;
from tkinter import ttk;

import math;

#### CORES ####

cor1 = "#3b3b3b"    #black
cor2 = "#feffff"    #white
cor3 = "#424345"    #black2
cor4 = "#ECEFF1"    #grey
cor5 = "#FFAB40"    #orange

#### JANELA PRINCIPAL ####

screen = Tk()
screen.title('Scientific Calculator')
screen.geometry('235x288')
screen.config(bg=cor1)


#### FRAMES  ####

frame_screen = Frame(screen, width=300, height=56, bg=cor3)
frame_screen.grid(row=0, column=0)

frame_scientific = Frame(screen, width=300, height=86)
frame_scientific.grid(row=1, column=0)

frame_body = Frame(screen, width=300, height=340)
frame_body.grid(row=2, column=0)

#### FUNÇÕES ####

global all_values

all_values = ''
text = StringVar()

def enter_values(event):
    global all_values

    all_values = all_values + str(event)
    text.set(all_values)

####CONFIGURAÇÕES DE FRAME DA TELA RESULTADO ####

label_screen = Label(frame_screen, width=16, height=2,textvariable=('text'), bd=0, padx=7, anchor='e', justify=RIGHT,font=('Ivy 18'), bg=cor3, fg=cor2)
label_screen.place(x=0, y=0)

####CONFIGURANDO FRAME CIENTIFICO ####

b_0 = Button(frame_scientific, command=lambda:enter_values('tan'), text='tan', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=1)
b_1 = Button(frame_scientific,command=lambda:enter_values('sin'), text='sin', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=1)
b_2 = Button(frame_scientific,command=lambda:enter_values('cos'), text='cos', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=1)
b_3 = Button(frame_scientific,command=lambda:enter_values('sqrt'), text='sqrt', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=177, y=1)

b_0 = Button(frame_scientific,command=lambda:enter_values('log'), text='log', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=29)
b_1 = Button(frame_scientific,command=lambda:enter_values('log10'), text='log10', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=29)
b_2 = Button(frame_scientific,command=lambda:enter_values('e'), text='e', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=29)
b_3 = Button(frame_scientific,command=lambda:enter_values('pow'), text='pow', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=177, y=29)

b_0 = Button(frame_scientific,command=lambda:enter_values('pi'), text='pi', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=58)
b_1 = Button(frame_scientific,command=lambda:enter_values(','), text=',', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=58)
b_2 = Button(frame_scientific,command=lambda:enter_values('('), text='(', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=58)
b_3 = Button(frame_scientific,command=lambda:enter_values(')'), text=')', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=177, y=58)

####CONFIGURANDO FRAME DE CORPO ####
b_0 = Button(frame_body, text='C',command=lambda:enter_values('C'), width=14, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.place(x=0, y=1)
b_1 = Button(frame_body, text='%',command=lambda:enter_values('%'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_1.place(x=118, y=1)
b_2 = Button(frame_body, text='/',command=lambda:enter_values('/'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_2.place(x=177, y=1)

b_0 = Button(frame_body, text='7',command=lambda:enter_values('7'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=30)
b_1 = Button(frame_body, text='8',command=lambda:enter_values('8'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=30)
b_2 = Button(frame_body, text='9',command=lambda:enter_values('9'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=30)
b_3 = Button(frame_body, text='*',command=lambda:enter_values('*'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_3.place(x=177, y=30)

b_0 = Button(frame_body, text='4',command=lambda:enter_values('4'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=59)
b_1 = Button(frame_body, text='5',command=lambda:enter_values('5'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=59)
b_2 = Button(frame_body, text='6',command=lambda:enter_values('6'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=59)
b_3 = Button(frame_body, text='-',command=lambda:enter_values('-'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_3.place(x=177, y=59)

b_0 = Button(frame_body, text='1',command=lambda:enter_values('1'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=88)
b_1 = Button(frame_body, text='2',command=lambda:enter_values('2'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=88)
b_2 = Button(frame_body, text='3',command=lambda:enter_values('3'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=88)
b_3 = Button(frame_body, text='+',command=lambda:enter_values('+'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_3.place(x=177, y=88)

b_0 = Button(frame_body, text='0',command=lambda:enter_values('0'), width=14, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=116)
b_1 = Button(frame_body, text='.',command=lambda:enter_values('.'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_1.place(x=118, y=116)
b_2 = Button(frame_body, text='=',command=lambda:enter_values('='), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_2.place(x=177, y=116)

screen.mainloop()