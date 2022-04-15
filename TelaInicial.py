from tkinter import *

def criaJanela():

    janela = Tk()

    janela.title("Trabalho C213")
    janela.geometry("350x250")
    #Título
    text_header = Label(janela, text="Projeto – Planta de nível – Controlador PI")
    text_header.place(x = 0, y = 5, width = 350, height = 30)

    #Texto para Máximo pico
    text_maxPico = Label(janela, text="Máximo pico:")
    text_maxPico.place(x = 10, y = 60)
    cxTxt_maxPico = Entry(janela)
    cxTxt_maxPico.place(x = 150, y = 60, width = 120)    

    #Texto para tempo de acomodação
    text_tempAcom = Label(janela, text="Tempo de acomodação:")
    text_tempAcom.place(x = 10, y = 90)
    cxTxt_tempAcom = Entry(janela)
    cxTxt_tempAcom.place(x = 150, y = 90, width = 120)

    #Texto para Tolerância
    text_tolerancia = Label(janela, text="Tolerância (+/- %):")
    text_tolerancia.place(x = 10, y = 120)
    cxTxt_tolerancia = Entry(janela)
    cxTxt_tolerancia.place(x = 150, y = 120, width = 120)

    #Criando botões
    
    
    janela.mainloop()

criaJanela()