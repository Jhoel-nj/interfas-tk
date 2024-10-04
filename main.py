from tkinter import *
#que es un Frame?


root = Tk()         #crear ventana

root.title('Dota 2')  #anadir titulo a mi ventana

root.resizable(1,1) #perimite ampliar la ventana segun sus parametros(1,1)(1,0)(0,0)(0,1)

root.iconbitmap(r"img/logo32.ico")

root.geometry('650x350')    #tamano inicial de la ventana

root.config(bg='green')     #color del fondo de la ventana

root.mainloop()