#Importando los programas que voy a usar
from tkinter import *
from tkinter.font import *
import os

################################################

#Creando la ventana
ventana = Tk()

################################################

#Funcion de borrar
def todo_a_cero():
    entra_dosmil.delete(0,END)
    entra_mil.delete(0,END)                         #Borra el entry
    entra_quinientos.delete(0,END) 
    entra_doscientos.delete(0,END) 
    entra_cien.delete(0,END) 
    entra_cincuenta.delete(0,END) 
    entra_veinte.delete(0,END) 
    entra_diez.delete(0,END)
    mostrar_dosmil.config(text="$0")
    mostrar_mil.config(text="$0")                   #Pone $0 en texto de la derecha
    mostrar_quinientos.config(text="$0")
    mostrar_doscientos.config(text="$0")
    mostrar_cien.config(text="$0")
    mostrar_cincuenta.config(text="$0")
    mostrar_veinte.config(text="$0")
    mostrar_diez.config(text="$0")
    mostrar_total.config(text="$0") 

################################################

#Configuracion de la ventana    
ventana.geometry("450x500")                   #Tamaño         
ventana.resizable(0,0)                        #No se pueda agrandar       
ventana.title("Contador de billetes")         #Titulo ventana

photopath = os.path.join(os.path.dirname(__file__), "billetes.png")            #Llamando icono
icono = PhotoImage(file=photopath)                                             #poniendo el icono en una variable
ventana.iconphoto(True, icono)                                                 #Poniendo el icono

photopath = os.path.join(os.path.dirname(__file__), "fondo_azul.png")     #Llamando fondo
imagen_fondo = PhotoImage(file=photopath)                                 #Poniendo la imagen en una variable
fondo = Label(ventana, image = imagen_fondo)                              #Poniendo el fondo
fondo.place(x=0,y=0,relheight=1,relwidth=1)                               #Ubicando el fondo

################################################

#Creando las fuentes
fuente_mostrar = Font(size=15)                 #Size tamaño de letra
fuente_total = Font(size=19)            
fuente_cantidad = Font(size=10)

################################################

#Poniendo el lugar donde se ingresa la cantidad

entra_dosmil = Entry(ventana, font=fuente_cantidad)        #Creandolo
entra_dosmil.place(x=175,y=99,width=45,height=30)

entra_mil = Entry(ventana,font=fuente_cantidad)        #Creandolo
entra_mil.place(x=175,y=142,width=45,height=30)         #Ubicacion y Tamaño

entra_quinientos = Entry(ventana,font=fuente_cantidad)
entra_quinientos.place(x=175,y=182,width=45,height=30)

entra_doscientos = Entry(ventana,font=fuente_cantidad)
entra_doscientos.place(x=175,y=222,width=45,height=30)

entra_cien = Entry(ventana,font=fuente_cantidad)
entra_cien.place(x=175,y=262,width=45,height=30)

entra_cincuenta = Entry(ventana,font=fuente_cantidad)
entra_cincuenta.place(x=175,y=302,width=45,height=30)

entra_veinte = Entry(ventana,font=fuente_cantidad)
entra_veinte.place(x=175,y=342,width=45,height=30)

entra_diez = Entry(ventana,font=fuente_cantidad)
entra_diez.place(x=175,y=382,width=45,height=30)

################################################

#Creando donde se muestra el total de cada billete

mostrar_dosmil = Label(ventana, bg="#30327f", fg="white", font=fuente_mostrar, text="$0")
mostrar_dosmil.place(x=300,y=97)

mostrar_mil = Label(ventana, bg="#30327f", fg="white", font=fuente_mostrar, text="$0")       #Creandolo y poniendole color de letra, fondo y fuente
mostrar_mil.place(x=300,y=140)                                                                #Ubicandolo

mostrar_quinientos = Label(ventana, bg="#30327f", fg="white", font=fuente_mostrar, text="$0")
mostrar_quinientos.place(x=300,y=185)

mostrar_doscientos = Label(ventana, bg="#30327f", fg="white", font=fuente_mostrar, text="$0")
mostrar_doscientos.place(x=300,y=225)

mostrar_cien = Label(ventana, bg="#30327f", fg="white", font=fuente_mostrar, text="$0")
mostrar_cien.place(x=300,y=262)

mostrar_cincuenta = Label(ventana, bg="#30327f", fg="white", font=fuente_mostrar, text="$0")
mostrar_cincuenta.place(x=300,y=302)

mostrar_veinte = Label(ventana, bg="#30327f", fg="white", font=fuente_mostrar, text="$0")
mostrar_veinte.place(x=300,y=342)

mostrar_diez= Label(ventana, bg="#30327f", fg="white", font=fuente_mostrar, text="$0")
mostrar_diez.place(x=300,y=382)

mostrar_total = Label(ventana, bg="#30327f", fg="white", font=fuente_total, text="$0")
mostrar_total.place(x=315,y=437)

################################################

#Funcion que se ejecuta al detectar una tecla en los entry

def total_dosmil(*Args):
    try:
        if entra_dosmil.get() == "":
            entra_dosmil.insert(0,"0")
            
        mostrar_total.config(text="$0")
        entero_dosmil = int(entra_dosmil.get()) * 2000
        mostrar_dosmil.config(text=f"${entero_dosmil}")
        
        if entra_mil.get() == "" :
            entra_mil.insert(0,"0")
            
        if entra_quinientos.get() == "" :
            entra_quinientos.insert(0,"0")    
            
        if entra_doscientos.get() == "":
            entra_doscientos.insert(0,"0")
            
        if entra_cien.get() == "":
            entra_cien.insert(0,"0")
            
        if entra_cincuenta.get() == "":
            entra_cincuenta.insert(0,"0")
            
        if entra_veinte.get() == "":
            entra_veinte.insert(0,"0")
            
        if entra_diez.get() == "":
            entra_diez.insert(0,"0")
        
        entero_mil = int(entra_mil.get()) * 1000
        mostrar_mil.config(text=f"${entero_mil}")
        
        entero_quinientos = int(entra_quinientos.get()) * 500
        mostrar_quinientos.config(text=f"${entero_quinientos}")
        
        entero_doscientos = int(entra_doscientos.get()) * 200
        mostrar_doscientos.config(text=f"${entero_doscientos}")
        
        entero_cien = int(entra_cien.get()) * 100
        mostrar_cien.config(text=f"${entero_cien}")
        
        entero_cincuenta = int(entra_cincuenta.get()) * 50
        mostrar_cincuenta.config(text=f"${entero_cincuenta}")
        
        entero_veinte = int(entra_veinte.get()) * 20
        mostrar_veinte.config(text=f"${entero_veinte}")
        
        entero_diez = int(entra_diez.get()) * 10
        mostrar_diez.config(text=f"${entero_diez}")
        
        total_resultado = entero_dosmil + entero_mil + entero_quinientos + entero_doscientos + entero_cien + entero_cincuenta + entero_veinte +  entero_diez
        mostrar_total.config(text=f"${total_resultado}")
        
        if entra_dosmil.get() == "0":
            entra_dosmil.delete(0,END)
        
        if entra_quinientos.get() == "0":
            entra_quinientos.delete(0,END)
        
        if entra_mil.get() == "0" :
            entra_mil.delete(0,END)
            
        if entra_doscientos.get() == "0":
            entra_doscientos.delete(0,END)
            
        if entra_cien.get() == "0":
            entra_cien.delete(0,END)
            
        if entra_cincuenta.get() == "0":
            entra_cincuenta.delete(0,END)
            
        if entra_veinte.get() == "0":
            entra_veinte.delete(0,END)
            
        if entra_diez.get() == "0":
            entra_diez.delete(0,END)       

    except ValueError:
        mostrar_dosmil.config(text="$0")

def total_mil(*Args):                                         #Nombre de la funcion
    global total_mil                                          #Para que se pueden usar todas las variables de las lineas
    try:                                                      #Para agarrar las excepciones 
        if entra_mil.get() == "":                             #Para detectar si borra todo el entry o no hay nada escrito, reproduce el siguiente codido
            entra_mil.insert(0,"0")                           #Pone un 0 para poder hacer despues la cuenta
            
        mostrar_total.config(text="$0")                       #Pone el texto de la derecha en 0
        entero_mil = int(entra_mil.get()) * 1000              #Agarra el valor del entry y lo multiplica por el billete que sea
        mostrar_mil.config(text=f"${entero_mil}")             #Pone el resultado en el texto de la derecha
        
        if entra_dosmil.get() == "":
            entra_dosmil.insert(0,"0")
        
        if entra_quinientos.get() == "" :                     #Verifica si no hay nada escrito en los otros entry
            entra_quinientos.insert(0,"0")                    #Si no hay nada pone un 0 para poder hacer la cuenta despues
            
        if entra_doscientos.get() == "":
            entra_doscientos.insert(0,"0")
            
        if entra_cien.get() == "":
            entra_cien.insert(0,"0")
            
        if entra_cincuenta.get() == "":
            entra_cincuenta.insert(0,"0")
            
        if entra_veinte.get() == "":
            entra_veinte.insert(0,"0")
            
        if entra_diez.get() == "":
            entra_diez.insert(0,"0")
        
        entero_dosmil = int(entra_dosmil.get()) * 2000
        mostrar_dosmil.config(text=f"${entero_dosmil}")
        
        entero_quinientos = int(entra_quinientos.get()) * 500                    #Multiplica el valor del entry y lo multiplica por el billete
        mostrar_quinientos.config(text=f"${entero_quinientos}")                  #Muestra el resultado a la derecha
        
        entero_doscientos = int(entra_doscientos.get()) * 200
        mostrar_doscientos.config(text=f"${entero_doscientos}")
        
        entero_cien = int(entra_cien.get()) * 100
        mostrar_cien.config(text=f"${entero_cien}")
        
        entero_cincuenta = int(entra_cincuenta.get()) * 50
        mostrar_cincuenta.config(text=f"${entero_cincuenta}")
        
        entero_veinte = int(entra_veinte.get()) * 20
        mostrar_veinte.config(text=f"${entero_veinte}")
        
        entero_diez = int(entra_diez.get()) * 10
        mostrar_diez.config(text=f"${entero_diez}")
        
        total_resultado = entero_dosmil + entero_mil + entero_quinientos + entero_doscientos + entero_cien + entero_cincuenta + entero_veinte +  entero_diez
        mostrar_total.config(text=f"${total_resultado}")        #Suma todas las cuentas anteriores     #Pone el resultado en el total de abajo
        
        if entra_mil.get() == "0":                   #En donde no habia nada y puso un 0, ahora lo saca
            entra_mil.delete(0,END)                  #Saca el 0
        
        if entra_quinientos.get() == "0" :
            entra_quinientos.delete(0,END)
        
        if entra_dosmil.get() == "0":
            entra_dosmil.delete(0,END)
            
        if entra_doscientos.get() == "0":
            entra_doscientos.delete(0,END)
            
        if entra_cien.get() == "0":
            entra_cien.delete(0,END)
            
        if entra_cincuenta.get() == "0":
            entra_cincuenta.delete(0,END)
            
        if entra_veinte.get() == "0":
            entra_veinte.delete(0,END)
            
        if entra_diez.get() == "0":
            entra_diez.delete(0,END)       

    except ValueError:                             #Agarra las excepciones
        mostrar_mil.config(text="$0")              #Pone 0 a la derecha
        
def total_quinientos(*Args):
    try:
        if entra_quinientos.get() == "":
            entra_quinientos.insert(0,"0")
            
        mostrar_total.config(text="$0")
        entero_quinientos = int(entra_quinientos.get()) * 500
        mostrar_quinientos.config(text=f"${entero_quinientos}")
        
        if entra_mil.get() == "" :
            entra_mil.insert(0,"0")
            
        if entra_doscientos.get() == "":
            entra_doscientos.insert(0,"0")
            
        if entra_dosmil.get() == "":
            entra_dosmil.insert(0,"0")
            
        if entra_cien.get() == "":
            entra_cien.insert(0,"0")
            
        if entra_cincuenta.get() == "":
            entra_cincuenta.insert(0,"0")
            
        if entra_veinte.get() == "":
            entra_veinte.insert(0,"0")
            
            
        if entra_diez.get() == "":
            entra_diez.insert(0,"0")
        
        entero_dosmil = int(entra_dosmil.get()) * 2000
        mostrar_dosmil.config(text=f"${entero_dosmil}")
        
        entero_mil = int(entra_mil.get()) * 1000
        mostrar_mil.config(text=f"${entero_mil}")
        
        entero_doscientos = int(entra_doscientos.get()) * 200
        mostrar_doscientos.config(text=f"${entero_doscientos}")
        
        entero_cien = int(entra_cien.get()) * 100
        mostrar_cien.config(text=f"${entero_cien}")
        
        entero_cincuenta = int(entra_cincuenta.get()) * 50
        mostrar_cincuenta.config(text=f"${entero_cincuenta}")
        
        entero_veinte = int(entra_veinte.get()) * 20
        mostrar_veinte.config(text=f"${entero_veinte}")
        
        entero_diez = int(entra_diez.get()) * 10
        mostrar_diez.config(text=f"${entero_diez}")
        
        total_resultado = entero_dosmil + entero_mil + entero_quinientos + entero_doscientos + entero_cien + entero_cincuenta + entero_veinte +  entero_diez
        mostrar_total.config(text=f"${total_resultado}")
        
        if entra_quinientos.get() == "0":
            entra_quinientos.delete(0,END)
        
        if entra_mil.get() == "0" :
            entra_mil.delete(0,END)
        
        if entra_dosmil.get() == "0":
            entra_dosmil.delete(0,END)
            
        if entra_doscientos.get() == "0":
            entra_doscientos.delete(0,END)
            
        if entra_cien.get() == "0":
            entra_cien.delete(0,END)
            
        if entra_cincuenta.get() == "0":
            entra_cincuenta.delete(0,END)
            
        if entra_veinte.get() == "0":
            entra_veinte.delete(0,END)
            
        if entra_diez.get() == "0":
            entra_diez.delete(0,END)       

    except ValueError:
        mostrar_quinientos.config(text="$0")

def total_doscientos(*Args):
    try:
        if entra_doscientos.get() == "":
            entra_doscientos.insert(0,"0")
        
        mostrar_total.config(text="$0")
        entero_doscientos = int(entra_doscientos.get()) * 200
        mostrar_doscientos.config(text=f"${entero_doscientos}")
        
        if entra_mil.get() == "" :
            entra_mil.insert(0,"0")
            
        if entra_dosmil.get() == "" :
            entra_dosmil.insert(0,"0")
            
        if entra_quinientos.get() == "":
            entra_quinientos.insert(0,"0")
        
        if entra_cien.get() == "":
            entra_cien.insert(0,"0")
            
        if entra_cincuenta.get() == "":
            entra_cincuenta.insert(0,"0")
            
        if entra_veinte.get() == "":
            entra_veinte.insert(0,"0")
            
        if entra_diez.get() == "":
            entra_diez.insert(0,"0")
        
        entero_mil = int(entra_mil.get()) * 1000
        mostrar_mil.config(text=f"${entero_mil}")
        
        entero_quinientos = int(entra_quinientos.get()) * 500
        mostrar_quinientos.config(text=f"${entero_quinientos}")
        
        entero_dosmil = int(entra_dosmil.get()) * 2000
        mostrar_dosmil.config(text=f"${entero_dosmil}")
        
        entero_cien = int(entra_cien.get()) * 100
        mostrar_cien.config(text=f"${entero_cien}")
        
        entero_cincuenta = int(entra_cincuenta.get()) * 50
        mostrar_cincuenta.config(text=f"${entero_cincuenta}")
        
        entero_veinte = int(entra_veinte.get()) * 20
        mostrar_veinte.config(text=f"${entero_veinte}")
        
        entero_diez = int(entra_diez.get()) * 10
        mostrar_diez.config(text=f"${entero_diez}")
        
        total_resultado = entero_dosmil + entero_mil + entero_quinientos + entero_doscientos + entero_cien + entero_cincuenta + entero_veinte +  entero_diez
        mostrar_total.config(text=f"${total_resultado}")
        
        if entra_mil.get() == "0" :
            entra_mil.delete(0,END)
            
        if entra_quinientos.get() == "0":
            entra_quinientos.delete(0,END)
        
        if entra_dosmil.get() == "0":
            entra_dosmil.delete(0,END)
            
        if entra_doscientos.get() == "0":
            entra_doscientos.delete(0,END)
        
        if entra_cien.get() == "0":
            entra_cien.delete(0,END)
            
        if entra_cincuenta.get() == "0":
            entra_cincuenta.delete(0,END)
            
        if entra_veinte.get() == "0":
            entra_veinte.delete(0,END)
            
        if entra_diez.get() == "0":
            entra_diez.delete(0,END)       

    except ValueError:
        mostrar_doscientos.config(text="$0")
        
def total_cien(*Args):
    try:
        if entra_cien.get() == "":
            entra_cien.insert(0,"0")
            
        mostrar_total.config(text="$0")
        entero_cien = int(entra_cien.get()) * 100
        mostrar_cien.config(text=f"${entero_cien}")
        
        if entra_dosmil.get() == "":
            entra_dosmil.insert(0,"0")
        
        if entra_mil.get() == "" :
            entra_mil.insert(0,"0")
            
        if entra_quinientos.get() == "":
            entra_quinientos.insert(0,"0")
            
        if entra_doscientos.get() == "":
            entra_doscientos.insert(0,"0")
        
        if entra_cincuenta.get() == "":
            entra_cincuenta.insert(0,"0")
            
        if entra_veinte.get() == "":
            entra_veinte.insert(0,"0")
            
        if entra_diez.get() == "":
            entra_diez.insert(0,"0")
        
        entero_dosmil = int(entra_dosmil.get()) * 2000
        mostrar_dosmil.config(text=f"${entero_dosmil}")
        
        entero_quinientos = int(entra_quinientos.get()) * 500
        mostrar_quinientos.config(text=f"${entero_quinientos}")
        
        entero_mil = int(entra_mil.get()) * 1000
        mostrar_mil.config(text=f"${entero_mil}")
        
        entero_doscientos = int(entra_doscientos.get()) * 200
        mostrar_doscientos.config(text=f"${entero_doscientos}")
        
        entero_cincuenta = int(entra_cincuenta.get()) * 50
        mostrar_cincuenta.config(text=f"${entero_cincuenta}")
        
        entero_veinte = int(entra_veinte.get()) * 20
        mostrar_veinte.config(text=f"${entero_veinte}")
        
        entero_diez = int(entra_diez.get()) * 10
        mostrar_diez.config(text=f"${entero_diez}")
        
        total_resultado = entero_dosmil + entero_mil + entero_quinientos + entero_doscientos + entero_cien + entero_cincuenta + entero_veinte +  entero_diez
        mostrar_total.config(text=f"${total_resultado}")
        
        if entra_dosmil.get() == "0" :
            entra_dosmil.delete(0,END)
        
        if entra_mil.get() == "0" :
            entra_mil.delete(0,END)
            
        if entra_quinientos.get() == "0":
            entra_quinientos.delete(0,END)
            
        if entra_doscientos.get() == "0":
            entra_doscientos.delete(0,END)
        
        if entra_cien.get() == "0":
            entra_cien.delete(0,END)
        
        if entra_cincuenta.get() == "0":
            entra_cincuenta.delete(0,END)
            
        if entra_veinte.get() == "0":
            entra_veinte.delete(0,END)
            
        if entra_diez.get() == "0":
            entra_diez.delete(0,END)       

    except ValueError:
        mostrar_cien.config(text="$0")
        
def total_cincuenta(*Args):
    try:
        if entra_cincuenta.get() == "":
            entra_cincuenta.insert(0,"0")
            
        mostrar_total.config(text="$0")
        entero_cincuenta = int(entra_cincuenta.get()) * 50
        mostrar_cincuenta.config(text=f"${entero_cincuenta}")
        
        if entra_quinientos.get() == "" :
            entra_quinientos.insert(0,"0")
        
        if entra_dosmil.get() == "":
            entra_dosmil.insert(0,"0")
            
        if entra_doscientos.get() == "":
            entra_doscientos.insert(0,"0")
            
        if entra_cien.get() == "":
            entra_cien.insert(0,"0")
            
        if entra_mil.get() == "":
            entra_mil.insert(0,"0")
        
        if entra_veinte.get() == "":
            entra_veinte.insert(0,"0")
            
        if entra_diez.get() == "":
            entra_diez.insert(0,"0")
        
        entero_quinientos = int(entra_quinientos.get()) * 500
        mostrar_quinientos.config(text=f"${entero_quinientos}")
        
        entero_doscientos = int(entra_doscientos.get()) * 200
        mostrar_doscientos.config(text=f"${entero_doscientos}")
        
        entero_dosmil = int(entra_dosmil.get()) * 2000
        mostrar_dosmil.config(text=f"${entero_dosmil}")
        
        entero_cien = int(entra_cien.get()) * 100
        mostrar_cien.config(text=f"${entero_cien}")
        
        entero_mil= int(entra_mil.get()) * 1000
        mostrar_mil.config(text=f"${entero_mil}")
        
        entero_veinte = int(entra_veinte.get()) * 20
        mostrar_veinte.config(text=f"${entero_veinte}")
        
        entero_diez = int(entra_diez.get()) * 10
        mostrar_diez.config(text=f"${entero_diez}")
        
        total_resultado = entero_dosmil + entero_mil + entero_quinientos + entero_doscientos + entero_cien + entero_cincuenta + entero_veinte +  entero_diez
        mostrar_total.config(text=f"${total_resultado}")
        
        if entra_mil.get() == "0" :
            entra_mil.delete(0,END)
            
        if entra_doscientos.get() == "0":
            entra_doscientos.delete(0,END)
            
        if entra_dosmil.get() == "0":
            entra_dosmil.delete(0,END)
            
        if entra_cien.get() == "0":
            entra_cien.delete(0,END)
            
        if entra_quinientos.get() == "0":
            entra_quinientos.delete(0,END)
        
        if entra_cincuenta.get() == "0":
            entra_cincuenta.delete(0,END)
        
        if entra_veinte.get() == "0":
            entra_veinte.delete(0,END)
            
        if entra_diez.get() == "0":
            entra_diez.delete(0,END)       

    except ValueError:
        mostrar_cincuenta.config(text="$0")

def total_veinte(*Args):
    try:
        if entra_veinte.get() == "":
            entra_veinte.insert(0,"0")
            
        mostrar_total.config(text="$0")
        entero_veinte = int(entra_veinte.get()) * 20
        mostrar_veinte.config(text=f"${entero_veinte}")
        
        if entra_quinientos.get() == "" :
            entra_quinientos.insert(0,"0")
        
        if entra_dosmil.get() == "":
            entra_dosmil.insert(0,"0")
            
        if entra_doscientos.get() == "":
            entra_doscientos.insert(0,"0")
            
        if entra_cien.get() == "":
            entra_cien.insert(0,"0")
            
        if entra_cincuenta.get() == "":
            entra_cincuenta.insert(0,"0")
            
        if entra_mil.get() == "":
            entra_mil.insert(0,"0")
        
        if entra_diez.get() == "":
            entra_diez.insert(0,"0")
        
        entero_quinientos = int(entra_quinientos.get()) * 500
        mostrar_quinientos.config(text=f"${entero_quinientos}")
        
        entero_doscientos = int(entra_doscientos.get()) * 200
        mostrar_doscientos.config(text=f"${entero_doscientos}")
        
        entero_dosmil = int(entra_dosmil.get()) * 2000
        mostrar_dosmil.config(text=f"${entero_dosmil}")
        
        entero_cien = int(entra_cien.get()) * 100
        mostrar_cien.config(text=f"${entero_cien}")
        
        entero_cincuenta = int(entra_cincuenta.get()) * 50
        mostrar_cincuenta.config(text=f"${entero_cincuenta}")
        
        entero_mil = int(entra_mil.get()) * 1000
        mostrar_mil.config(text=f"${entero_mil}")
        
        entero_diez = int(entra_diez.get()) * 10
        mostrar_diez.config(text=f"${entero_diez}")
        
        total_resultado = entero_dosmil + entero_mil + entero_quinientos + entero_doscientos + entero_cien + entero_cincuenta + entero_veinte +  entero_diez
        mostrar_total.config(text=f"${total_resultado}")
        
        if entra_mil.get() == "0" :
            entra_mil.delete(0,END)
            
        if entra_doscientos.get() == "0":
            entra_doscientos.delete(0,END)
        
        if entra_dosmil.get() == "0":
            entra_dosmil.delete(0,END)
            
        if entra_cien.get() == "0":
            entra_cien.delete(0,END)
            
        if entra_cincuenta.get() == "0":
            entra_cincuenta.delete(0,END)
            
        if entra_quinientos.get() == "0":
            entra_quinientos.delete(0,END)
        
        if entra_veinte.get() == "0":
            entra_veinte.delete(0,END)
            
        if entra_diez.get() == "0":
            entra_diez.delete(0,END)       

    except ValueError:
        mostrar_veinte.config(text="$0")
        
def total_diez(*Args):
    try:
        if entra_diez.get() == "":
            entra_diez.insert(0,"0") 
            
        mostrar_total.config(text="$0")
        entero_diez = int(entra_diez.get()) * 10
        mostrar_diez.config(text=f"${entero_diez}")
        
        if entra_quinientos.get() == "" :
            entra_quinientos.insert(0,"0")
            
        if entra_doscientos.get() == "":
            entra_doscientos.insert(0,"0")
        
        if entra_dosmil.get() == "":
            entra_dosmil.insert(0,"0")
            
        if entra_cien.get() == "":
            entra_cien.insert(0,"0")
            
        if entra_cincuenta.get() == "":
            entra_cincuenta.insert(0,"0")
            
        if entra_veinte.get() == "":
            entra_veinte.insert(0,"0")   
            
        if entra_mil.get() == "":
            entra_mil.insert(0,"0")
        
        entero_quinientos = int(entra_quinientos.get()) * 500
        mostrar_quinientos.config(text=f"${entero_quinientos}")
        
        entero_doscientos = int(entra_doscientos.get()) * 200
        mostrar_doscientos.config(text=f"${entero_doscientos}")
        
        entero_dosmil = int(entra_dosmil.get()) * 2000
        mostrar_dosmil.config(text=f"${entero_dosmil}")
        
        entero_cien = int(entra_cien.get()) * 100
        mostrar_cien.config(text=f"${entero_cien}")
        
        entero_cincuenta = int(entra_cincuenta.get()) * 50
        mostrar_cincuenta.config(text=f"${entero_cincuenta}")
        
        entero_veinte = int(entra_veinte.get()) * 20
        mostrar_veinte.config(text=f"${entero_veinte}")
        
        entero_mil = int(entra_mil.get()) * 1000
        mostrar_mil.config(text=f"${entero_mil}")
        
        total_resultado = entero_dosmil + entero_mil + entero_quinientos + entero_doscientos + entero_cien + entero_cincuenta + entero_veinte +  entero_diez
        mostrar_total.config(text=f"${total_resultado}")
        
        if entra_mil.get() == "0" :
            entra_mil.delete(0,END)
            
        if entra_doscientos.get() == "0":
            entra_doscientos.delete(0,END)
        
        if entra_dosmil.get() == "0":
            entra_dosmil.delete(0,END)
            
        if entra_cien.get() == "0":
            entra_cien.delete(0,END)
            
        if entra_cincuenta.get() == "0":
            entra_cincuenta.delete(0,END)
        
        if entra_diez.get() == "0":
            entra_diez.delete(0,END)
        
        if entra_veinte.get() == "0":
            entra_veinte.delete(0,END)
            
        if entra_quinientos.get() == "0":
            entra_quinientos.delete(0,END)       

    except ValueError:
        mostrar_diez.config(text="$0")
        
################################################

#Creando botones    

borrar = Button(ventana, text="Borrar", bg="white", command=todo_a_cero)
borrar.place(x=50, y=440, width=140 , height=30)

################################################

#Detecta cuando se escribe en los entry y ejecuta las funciones de arriba

entra_dosmil.bind('<KeyRelease>', total_dosmil) 
entra_mil.bind('<KeyRelease>', total_mil) 
entra_quinientos.bind('<KeyRelease>', total_quinientos)
entra_doscientos.bind('<KeyRelease>', total_doscientos)
entra_cien.bind('<KeyRelease>', total_cien)
entra_cincuenta.bind('<KeyRelease>', total_cincuenta)
entra_veinte.bind('<KeyRelease>', total_veinte)
entra_diez.bind('<KeyRelease>', total_diez)

################################################

#Funciones para moverse por los entry con las teclas

def funcion_enter(event):
    event.widget.tk_focusNext().focus()      
    return "break"

def flecha_arriba(event):
    event.widget.tk_focusPrev().focus()
    return "break"

#Para que al tocar una tecla ejecute las funciones de arriba

entra_dosmil.bind("<Return>", funcion_enter)
entra_mil.bind("<Return>", funcion_enter)               #Return = Enter
entra_quinientos.bind("<Return>", funcion_enter) 
entra_doscientos.bind("<Return>", funcion_enter)
entra_cien.bind("<Return>", funcion_enter)
entra_cincuenta.bind("<Return>", funcion_enter)
entra_veinte.bind("<Return>", funcion_enter)

entra_mil.bind("<Up>", flecha_arriba)
entra_quinientos.bind("<Up>", flecha_arriba)            #Up = Flecha para arriba
entra_doscientos.bind("<Up>", flecha_arriba)
entra_cien.bind("<Up>", flecha_arriba)
entra_cincuenta.bind("<Up>", flecha_arriba)
entra_veinte.bind("<Up>", flecha_arriba)
entra_diez.bind('<Up>', flecha_arriba)

entra_dosmil.bind("<Down>", funcion_enter)
entra_mil.bind("<Down>", funcion_enter)                  #Down = Flecha para abajo
entra_quinientos.bind("<Down>", funcion_enter)
entra_doscientos.bind("<Down>", funcion_enter)
entra_cien.bind("<Down>", funcion_enter)
entra_cincuenta.bind("<Down>", funcion_enter)
entra_veinte.bind("<Down>", funcion_enter)

################################################

#Loop de la ventana
ventana.mainloop()