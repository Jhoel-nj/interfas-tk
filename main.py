from tkinter import *
#que es un Frame?


root = Tk()         #crear ventana

root.title('Dota 2')  #anadir titulo a mi ventana

root.resizable(1,1) #perimite ampliar la ventana segun sus parametros(1,1)(1,0)(0,0)(0,1)

root.iconbitmap(r"img/logo32.ico")

root.geometry('650x350')    #tamano inicial de la ventana

root.config(bg='gray')     #color del fondo de la ventana


def mensaje():
    print('mensaje del boton')

#CREANDO UN LABEL
lbl = Label(root, text='enviar mensaje')
#CREANDO UN BOTON
btn = Button(root, text='mensaje', command=mensaje, bg='black', fg='white')







lbl.pack()  #siempre se debe ejecutar esto para q los widgets se muestren en la ventana
btn.pack()
root.mainloop()