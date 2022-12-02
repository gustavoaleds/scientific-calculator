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

janela = Tk()
janela.title('Scientific Calculator')
janela.geometry('235x310')
janela.config(bg=cor1)


#### FRAMES  ####

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)
#### FUNÇÕES ####

def entering_values(event):
    global all_vallues
    all_values = all_values +str(event)
    value_text.set(all_values)

    def calculate():
        global all_values

        global texto

        texto = all_values

        modulos =['math.tan','math.sin','math.cos','math.sqrt','math.log','math.log10','math.e','math.pow','math.pi','math.radian']

        for i in modulos:
            if i=='math.tan':
                texto = texto.replace("tan", i)
            
            if i=='math.sin':
                texto = texto.replace("sin", i)

            if i=='math.cos':
                texto = texto.replace("cos", i)
            
            if i=='math.sqrt':
                texto = texto.replace("sqrt", i)

            #-------------------------------------
        
            if i=='math.log':
                texto = texto.replace("log", i)

            if i=='math.log10':
                texto = texto.replace("log10", i)

            if i=='math.e':
                texto = texto.replace("e", i)

janela.mainloop()