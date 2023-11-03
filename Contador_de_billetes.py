############################################################

#IMPORTs
from tkinter import END, Tk, Label, Button, Entry, PhotoImage
from tkinter.font import Font
import os

############################################################

#Ventana
ventana = Tk()

############################################################

#DEFs
def Borrar():
    Entrys = [entra_dosmil, entra_mil, entra_quinientos, entra_doscientos, entra_cien, entra_cincuenta, entra_veinte, entra_diez]
    Labels = [mostrar_dosmil, mostrar_mil, mostrar_quinientos, mostrar_doscientos, mostrar_cien, mostrar_cincuenta, mostrar_veinte, mostrar_diez]
    for i in Entrys:
        i.delete(0,END)
    for i in Labels:
        i.config(text="$0")
    entra_dosmil.focus()
    
def Sumar(event):
    Entrys = [entra_dosmil.get(),entra_mil.get(),entra_quinientos.get(),entra_doscientos.get(),entra_cien.get(),entra_cincuenta.get(),entra_veinte.get(),entra_diez.get()]
    Numeros = []
    for i in Entrys:
        if i == "":
            i=0
            Numeros.append(int(i))
        else:
            Numeros.append(int(i))
    
    mostrar_dosmil.config(text=f"${Numeros[0]*2000}")
    mostrar_mil.config(text=f"${Numeros[1]*1000}")
    mostrar_quinientos.config(text=f"${Numeros[2]*500}")
    mostrar_doscientos.config(text=f"${Numeros[3]*200}")
    mostrar_cien.config(text=f"${Numeros[4]*100}")
    mostrar_cincuenta.config(text=f"${Numeros[5]*50}")
    mostrar_veinte.config(text=f"${Numeros[6]*20}")
    mostrar_diez.config(text=f"${Numeros[7]*10}")
    mostrar_total.config(text=f"${Numeros[0]*2000+Numeros[1]*1000+Numeros[2]*500+Numeros[3]*200+Numeros[4]*100+Numeros[5]*50+Numeros[6]*20+Numeros[7]*10}")
    
def Siguiente(event):
    event.widget.tk_focusNext().focus()      
    return "break"

def Anterior(event):
    event.widget.tk_focusPrev().focus()
    return "break"

############################################################

#CONFIG VENTANA
ventana.geometry("450x500")
ventana.resizable(0,0)
ventana.title("Contador de billetes")

photopath = os.path.join(os.path.dirname(__file__), "billetes.png")
icono = PhotoImage(file=photopath)
ventana.iconphoto(True, icono)

photopath = os.path.join(os.path.dirname(__file__), "fondo_azul.png")
imagen_fondo = PhotoImage(file=photopath)
fondo = Label(ventana, image = imagen_fondo)
fondo.place(x=0,y=0,relheight=1,relwidth=1) 

############################################################

#ENTRYs
entra_dosmil = Entry(ventana, font=Font(size=10))
entra_dosmil.place(x=175,y=99,width=45,height=30)

entra_mil = Entry(ventana,font=Font(size=10))
entra_mil.place(x=175,y=142,width=45,height=30)

entra_quinientos = Entry(ventana,font=Font(size=10))
entra_quinientos.place(x=175,y=182,width=45,height=30)

entra_doscientos = Entry(ventana,font=Font(size=10))
entra_doscientos.place(x=175,y=222,width=45,height=30)

entra_cien = Entry(ventana,font=Font(size=10))
entra_cien.place(x=175,y=262,width=45,height=30)

entra_cincuenta = Entry(ventana,font=Font(size=10))
entra_cincuenta.place(x=175,y=302,width=45,height=30)

entra_veinte = Entry(ventana,font=Font(size=10))
entra_veinte.place(x=175,y=342,width=45,height=30)

entra_diez = Entry(ventana,font=Font(size=10))
entra_diez.place(x=175,y=382,width=45,height=30)

############################################################

#LABELs
mostrar_dosmil = Label(ventana, bg="#30327f", fg="white", font=Font(size=15), text="$0")
mostrar_dosmil.place(x=300,y=97)

mostrar_mil = Label(ventana, bg="#30327f", fg="white", font=Font(size=15), text="$0")
mostrar_mil.place(x=300,y=140)

mostrar_quinientos = Label(ventana, bg="#30327f", fg="white", font=Font(size=15), text="$0")
mostrar_quinientos.place(x=300,y=185)

mostrar_doscientos = Label(ventana, bg="#30327f", fg="white", font=Font(size=15), text="$0")
mostrar_doscientos.place(x=300,y=225)

mostrar_cien = Label(ventana, bg="#30327f", fg="white", font=Font(size=15), text="$0")
mostrar_cien.place(x=300,y=262)

mostrar_cincuenta = Label(ventana, bg="#30327f", fg="white", font=Font(size=15), text="$0")
mostrar_cincuenta.place(x=300,y=302)

mostrar_veinte = Label(ventana, bg="#30327f", fg="white", font=Font(size=15), text="$0")
mostrar_veinte.place(x=300,y=342)

mostrar_diez= Label(ventana, bg="#30327f", fg="white", font=Font(size=15), text="$0")
mostrar_diez.place(x=300,y=382)

mostrar_total = Label(ventana, bg="#30327f", fg="white", font=Font(size=19), text="$0")
mostrar_total.place(x=315,y=437)

############################################################

#BOTON
borrar = Button(ventana, text="Borrar", bg="white", command=Borrar)
borrar.place(x=50, y=440, width=140 , height=30)

############################################################

#BINDs
entra_dosmil.bind('<KeyRelease>', Sumar)
entra_mil.bind('<KeyRelease>', Sumar)
entra_quinientos.bind('<KeyRelease>', Sumar)
entra_doscientos.bind('<KeyRelease>', Sumar)
entra_cien.bind('<KeyRelease>', Sumar)
entra_cincuenta.bind('<KeyRelease>', Sumar)
entra_veinte.bind('<KeyRelease>', Sumar)
entra_diez.bind('<KeyRelease>', Sumar)

entra_dosmil.bind("<Return>", Siguiente)
entra_mil.bind("<Return>", Siguiente)
entra_quinientos.bind("<Return>", Siguiente) 
entra_doscientos.bind("<Return>", Siguiente)
entra_cien.bind("<Return>", Siguiente)
entra_cincuenta.bind("<Return>", Siguiente)
entra_veinte.bind("<Return>", Siguiente)

entra_mil.bind("<Up>", Anterior)
entra_quinientos.bind("<Up>", Anterior)
entra_doscientos.bind("<Up>", Anterior)
entra_cien.bind("<Up>", Anterior)
entra_cincuenta.bind("<Up>", Anterior)
entra_veinte.bind("<Up>", Anterior)
entra_diez.bind('<Up>', Anterior)

entra_dosmil.bind("<Down>", Siguiente)
entra_mil.bind("<Down>", Siguiente)
entra_quinientos.bind("<Down>", Siguiente)
entra_doscientos.bind("<Down>", Siguiente)
entra_cien.bind("<Down>", Siguiente)
entra_cincuenta.bind("<Down>", Siguiente)
entra_veinte.bind("<Down>", Siguiente)

############################################################

#MAINLOOP
ventana.mainloop()
