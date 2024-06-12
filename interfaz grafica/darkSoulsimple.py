from tkinter import ttk, messagebox, Label
import tkinter as tk


def mostrar_seleccion():     
    selecion_personaje = ventana_seleccion.get()



    if selecion_personaje == "Guerrero":
        vida = 500
        daño = 30
        defensa = 200
        daño_magico = 0
        print("Seleccionaste Guerrero")
        Label(None,text=f"  selecionaste Guerrero \n vida: {vida} \n daño:{daño} \n defensa: {defensa} \n Magia: {daño_magico}  ", fg="red", background="black").place(x=300,y=150)#colocar fondo blanco, borde y actua como un falso cuadro de texto

        
    
    elif selecion_personaje == "Mago":
        print("Seleccionaste Mago")
        vida = 350
        daño = 12
        daño_magico= 40
        defensa = 150
        
        Label(None,text=f"  selecionaste  Mago   \n vida: {vida} \n daño:{daño} \n daño magico: {daño_magico} \n defensa: {defensa}  ", fg="red", background="black").place(x=300,y=150)
    elif selecion_personaje == "Paladin":
        print("Seleccionaste Paladin")
        vida = 700
        daño = 60
        daño_magico= 35
        defensa = 400
        
        Label(None,text=f"  selecionaste Paladin \n vida: {vida} \n daño:{daño} \n daño magico: {daño_magico} \n defensa: {defensa}  ", fg="red", background="black").place(x=300,y=150)
    elif selecion_personaje == "Espadachin":
        print("Seleccionaste Espadachin")
        vida = 450
        daño = 90
        daño_magico = 0
        defensa = 200
        Label(None,text=f"  selecionaste Espadachin \n vida: {vida} \n daño:{daño} \n daño magico: {daño_magico} \n defensa: {defensa}  ", fg="red", background="black").place(x=300,y=150)


#creacion de ventanas, botones
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Dark Soul-Simple")
ventanaPrincipal.config(width=800, height=600)
boton1 = tk.Button(ventanaPrincipal,text="Elegir",command=mostrar_seleccion)
Label(ventanaPrincipal, text="bievenido").place(x=200,y=300)




ventana_seleccion= ttk.Combobox(ventanaPrincipal, state="Readonly",values=["Guerrero","Mago","Paladin","Espadachin"])






#incertar ventanas/ botones
boton1.place(x=10,y=40)
ventana_seleccion.place(x=0,y=10)

ventanaPrincipal.mainloop() 