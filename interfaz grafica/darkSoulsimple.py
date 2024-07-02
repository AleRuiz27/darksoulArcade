from tkinter import ttk, messagebox, Label
import tkinter as tk
import random


vida_jefe_el_bailarin = 1000
daño_jefe_el_bailarin = 50
el_bailarin = """En los reinos infernales de la oscuridad eterna, donde las sombras danzan al ritmo de la desesperación \n se yergue majestuoso "El Bailarín". Este enigmático coloso, envuelto en llamas purpúreas que serpentean alrededor de su figura imponente,\n es tanto una obra de arte como un verdugo implacable para aquellos que osan desafiarlo.

Su presencia es un espectáculo macabro y hermoso a la vez: cada movimiento fluido de sus largos brazos termina en garras afiladas como cuchillas, capaces de desgarrar tu alma. \n Los ojos del Bailarín, ocultos tras una máscara antigua y enigmática emiten una luz que paraliza de miedo incluso al más valiente de los guerreros.

Los rumores susurran que "El Bailarín" fue una vez un noble guerrero que perdió su humanidad en un pacto oscuro por poder. \n Ahora, su danza mortal se convierte en una prueba de fuego para aquellos que buscan atravesar las tinieblas y reclamar la gloria en los dominios olvidados del mundo de las almas perdidas"""
cartel_bienvenida = """
Bienvenido a Dark Souls: Preparación para la Batalla

En las profundidades de la oscuridad, un desafío aguarda. Eres el elegido para enfrentar al temido Jefe. Escoge sabiamente tus habilidades y armas, pues cada paso te acerca al enfrentamiento final.

Forja tu camino, supera tus límites y desvela los secretos ocultos en las sombras. La batalla será feroz, pero tu determinación es tu mayor arma.

¡Prepárate, guerrero! El destino aguarda tu valentía en esta lucha épica.

Que tus decisiones guíen tu destino en Dark Souls.

"""
espadachin_descripcion = "Un maestro de la espada, rápido y letal en el combate cuerpo a cuerpo."
mago_descripcion = "Un experto en artes arcanas, capaz de lanzar poderosos hechizos."
guerrero_descripcion = "Un luchador formidable, especializado en el combate con armas pesadas."
paladin_descripcion = "Un guerrero sagrado, defensor de la justicia con habilidades magicas."
palabras_Del_Bailarin = "En la oscuridad del escenario, el héroe se enfrenta al Bailarín. Sus miradas se cruzan, llenas de determinación y desafío.\n La batalla decisiva está a punto de comenzar.\n ¿Quién saldrá victorioso?"
def abrir_nueva_ventana(personaje):
    
    nueva_ventana = tk.Tk()
    nueva_ventana.title("Dark Soul-Inicio Cero")
    nueva_ventana.config(width=800, height=600)
    
    #desempaquetar  la lista de personsaje. 
    global vida_pj,defensa
    nombre, vida_pj, daño, defensa, daño_magico = personaje
     
    
    
    
    
   
    Label(nueva_ventana, text=f"Seleccionaste {nombre}\nVida: {vida_pj}\nDaño: {daño}\nDefensa: {defensa}\nMagia: {daño_magico}", fg="red", background="black").place(x=350, y=0)
    
    
    Label(nueva_ventana, text=f"{el_bailarin}", fg="Red").place(x=0, y=150)

    boton_cerrar = tk.Button(nueva_ventana, text="EMPEZAR LA BATALLA", command=lambda: pelea())
    boton_cerrar.place(x=400, y= 300)  



    



    
        
        
    

             

       


    def actualizar_jefe_pj():
        
        mensaje_jefe.config(text=f"vida del Bailarin: {vida_jefe_el_bailarin}", font=80, fg="Red")
        mensaje_Pj.config(text=f"vida del {nombre}: {vida_pj}",font=60, fg="Green")
        
            


    def atacar():
        
        global vida_jefe_el_bailarin,estado_pelea,boton_atacar,daño_jefe_el_bailarin

        if vida_jefe_el_bailarin <= 1 or vida_pj <= 1:
            vida_jefe_el_bailarin = 0
         
         
            resultado.config(text="¡El bailarin ha muerto!")
            final()
         
         
         
        
         
        else:
            vida_jefe_el_bailarin-=(daño + daño_magico)
            estado_pelea.config(text="Golpeaste al Bailarin")
            print (vida_jefe_el_bailarin)
            turno_jefe()
        actualizar_jefe_pj()
        

    def defender():
        global vida_pj, daño_jefe_el_bailarin
        
        print(vida_pj)
        if vida_pj <= 1 or vida_jefe_el_bailarin <= 1:
            vida_pj = 0
            daño_jefe_el_bailarin = 0
            final()
            
            
            
            
            resultado.config(text=f"el {nombre} murio")
            
            
        else:
            
            actualizar_jefe_pj()
            turno_jefe()
    def turno_jefe():
        suerte = random.randint(1,3)
        if suerte == 1:
            global vida_pj, daño_jefe_el_bailarin,resultado,estado_pelea, daño,daño_magico
            vida_pj-=daño_jefe_el_bailarin
            if vida_pj <= 1:
                 vida_pj = 0
                 resultado.config(text=f"el {nombre} murio")
                 final()
                
                 
                 
                
                
            else:
                estado_pelea.config(text=f"el bailarin te ah golpeado")
                print("entro golpe")
        elif suerte == 2:
                estado_pelea.config(text=f"el bailarin fallo el golpe")
                print("fallo el golpe")
        elif suerte == 3:
                estado_pelea.config(text=f"bloqueaste el golpe")
                print("bloqueaste el golpe")
        actualizar_jefe_pj()
    def final():
        boton_atacar.config(state="disabled")
        boton_defender.config(state="disabled")
    

    
        
        
        
        
    
    
          
        


        

        


        
        

    
        
        
        
       
            

        
        







    def pelea():
        global nueva_ventana_pelea
        nueva_ventana_pelea = tk.Toplevel()
        nueva_ventana_pelea.title(f"Pelea  El Bailarín")
        nueva_ventana_pelea.geometry("800x600")
        global vida_jefe
        vida_jefe = 100

        global resultado 
        resultado= tk.Label(nueva_ventana_pelea, text="")
        resultado.place(x=500,y=600)
        resultado.config(font=(30))
        global estado_pelea
        estado_pelea = tk.Label(nueva_ventana_pelea,text="")
        estado_pelea.place(x=450, y=400)
        estado_pelea.config(font=30)
        global mensaje_jefe
        mensaje_jefe = tk.Label(nueva_ventana_pelea,text=f"vida Del Bailarin: {vida_jefe_el_bailarin}")
        mensaje_jefe.pack()
        global mensaje_Pj
        mensaje_Pj = tk.Label(nueva_ventana_pelea, text=f"vida del {nombre}: {vida_pj}")
        mensaje_Pj.pack()

        
        

        tk.Label(nueva_ventana_pelea, text=f"{palabras_Del_Bailarin}").pack()

        global boton_atacar
        boton_atacar= tk.Button(nueva_ventana_pelea, text="ATACAR",command=lambda:atacar()).place(x=300,y=200)
        global boton_defender
        boton_defender= tk.Button(nueva_ventana_pelea,text="DEFENDERSE",command=lambda:defender()).place(x=800,y=200)
        

    
    
    
   
    
        
    
    
    
    
    nueva_ventana.mainloop()





    
    


    nueva_ventana.mainloop()
    

    


def mostrar_seleccion():     
    selecion_personaje = ventana_seleccion.get()



    if selecion_personaje == "Guerrero":
        
        vida = 500
        daño = 30
        defensa = 200
        daño_magico = 40
        
        personaje = ["Guerrero", 500, 30, 200, 0]
        print("Seleccionaste Guerrero")
        Label(None,text=f"  selecionaste Guerrero \n vida: {vida} \n daño:{daño} \n defensa: {defensa} \n Magia: {daño_magico}  ", fg="red", background="black").place(x=660,y=250)#colocar fondo blanco, borde y actua como un falso cuadro de texto
        Label(None,text=f"{guerrero_descripcion}", fg="red", background="black").place(x=550,y=340)
        
    
    elif selecion_personaje == "Mago":
        print("Seleccionaste Mago")
        vida = 350
        daño = 12
        defensa = 150
        daño_magico= 40
        personaje = ["Mago", 350, 12, 40,40 ]
        
        Label(None,text=f"  selecionaste  Mago   \n vida: {vida} \n daño:{daño} \n daño magico: {daño_magico} \n defensa: {defensa}  ", fg="red", background="black").place(x=660,y=250)
        Label(None,text=f"{mago_descripcion}", fg="red", background="black").place(x=550,y=340)
    elif selecion_personaje == "Paladin":
        print("Seleccionaste Paladin")
        vida = 700
        daño = 60
        daño_magico= 35
        defensa = 400
        personaje = ["Paladin", 700, 60, 35,400 ]
        
        
        Label(None,text=f"  selecionaste Paladin \n vida: {vida} \n daño:{daño} \n daño magico: {daño_magico} \n defensa: {defensa}  ", fg="red", background="black").place(x=660,y=250)
        Label(None,text=f"{paladin_descripcion}", fg="red", background="black").place(x=550,y=340)
    elif selecion_personaje == "Espadachin":
        print("Seleccionaste Espadachin")
        vida = 450
        daño = 90
        daño_magico = 0
        defensa = 200
        personaje = ["Espadachin", 450, 90, 0, 200 ]
        Label(None,text=f"  selecionaste Espadachin \n vida: {vida} \n daño:{daño} \n daño magico: {daño_magico} \n defensa: {defensa}  ", fg="red", background="black").place(x=660,y=250)
        Label(None,text=f"{espadachin_descripcion}", fg="red", background="black").place(x=550,y=340)
    boton_cerrar = tk.Button(ventanaPrincipal, text="Seleccionar Personaje", command=lambda: [ventanaPrincipal.destroy(), abrir_nueva_ventana(personaje)])
    boton_cerrar.place(x=660, y= 450)



    

#creacion de ventanas, botones
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Dark Soul-Simple")
ventanaPrincipal.config(width=800, height=600)
boton1 = tk.Button(ventanaPrincipal,text="Elegir",command=mostrar_seleccion)
Label(ventanaPrincipal, text=f"{cartel_bienvenida}").place(x=200,y=0)




ventana_seleccion= ttk.Combobox(ventanaPrincipal, state="Readonly",values=["Guerrero","Mago","Paladin","Espadachin"])
ventana_seleccion.place(x=650, y= 170)





#incertar ventanas/ botones
boton1.place(x=800,y= 190)

ventanaPrincipal.mainloop() 
