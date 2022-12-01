from tkinter import *;
from tkinter import ttk;

import math;

#### CORES ####

cor1 = "#feffff" #white
cor2 = "#6f9fbd" #blue
cor3 = "#38576b" #valor

fundo = "#e8e6e6"
cor10 = "#363434"
cor11 = "#424345"

cor4 = '#FFAB40'
cor5 = '#FF333a'
cor6 = '#6bd66f'
cor7 = '#ab8918'

janela = Tk()
janela.title('')
janela.geometry('235x289')
janela.configure(bg=cor1)

style = ttk.Style(janela)
style.theme_use("clam")

#### FRAMES  ####

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columspan=1, ipadx=280)

frame_score = Frame(janela, width=300, height=56, bg=cor3, pady=0, padx=0, relief="flat",)
frame_score.grid(row=1, column=0, sticky=NW)

frame_cientifica = Frame(janela, width=300, height=86, bg=cor3, pady=0, padx=0, relief="flat",)
frame_cientifica.grid(row=2, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340, bg=fundo, pady=0, padx=0, relief="flat",)
frame_quadros.grid(row=3, column=0, sticky=NW)

#### FUNÇÕES ####

