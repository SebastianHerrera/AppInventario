from ast import Str
from cProfile import label
from cmath import exp
from email.mime import image
from fileinput import filename
from glob import glob
from logging import root
import tkinter
from tkinter import BOTH, E, LEFT, RIDGE, RIGHT, VERTICAL, W, Y, Canvas, IntVar, StringVar, YView, filedialog
from tkinter import ttk
from turtle import bgcolor, color
from tkinter.ttk import *
import csv


global state
state = 0

## METODOS

def abrir_cargar_archivos(): 
      
    
    
    nueva_ventana = tkinter.Toplevel(ventana) 
    nueva_ventana.title("Cargar Archivo")   
    ancho_cargar_archivo= 250
    alto_cargar_archivo= 300
    x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
    y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
    posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)
    nueva_ventana.geometry(posicion)
    nueva_ventana.config(bg="#212F3C")
    nueva_ventana.resizable(0,0)
    
    
    texto_cargar_archivo = tkinter.Label(nueva_ventana, text ="Ruta del Archivo")
    texto_cargar_archivo.place(x=80,y=50)
    texto_cargar_archivo.config(bg="#212F3C", fg="white")

    boton_explorar = tkinter.Button(nueva_ventana, text = "Buscar Archivo", command = browseFiles)
    boton_explorar.place(x=80,y=100)  
    boton_explorar.config(bg="#17202A", fg="white", cursor="hand2")

def abrir_gestionar_cursos(): 
      
    
    
    nueva_ventana = tkinter.Toplevel(ventana) 
    nueva_ventana.title("Gestionar Cursos")   
    ancho_cargar_archivo= 250
    alto_cargar_archivo= 300
    x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
    y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
    posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)
    nueva_ventana.geometry(posicion)
    nueva_ventana.config(bg="#212F3C")
    nueva_ventana.resizable(0,0)
    
    listar_cursos_boton= tkinter.Button(nueva_ventana, text="Listar Cursos", command=listar_cursos)
    listar_cursos_boton.place(x=80,y=50)  
    listar_cursos_boton.config(bg="#17202A", fg="white", cursor="hand2")
    
    mostrar_cursos_boton= tkinter.Button(nueva_ventana, text="Mostrar Curso", command=mostrar_cursos)
    mostrar_cursos_boton.place(x=75,y=90)  
    mostrar_cursos_boton.config(bg="#17202A", fg="white", cursor="hand2")

    agregar_cursos_boton= tkinter.Button(nueva_ventana, text="Agregar Curso", command=agregar_cursos)
    agregar_cursos_boton.place(x=75,y=130)  
    agregar_cursos_boton.config(bg="#17202A", fg="white", cursor="hand2")

    editar_cursos_boton= tkinter.Button(nueva_ventana, text="Editar Cursos", command=editar_cursos)
    editar_cursos_boton.place(x=78,y=170)  
    editar_cursos_boton.config(bg="#17202A", fg="white", cursor="hand2")

    eliminar_curso_boton= tkinter.Button(nueva_ventana, text="Eliminar Cursos", command=eliminar_curso)
    eliminar_curso_boton.place(x=73,y=210)  
    eliminar_curso_boton.config(bg="#17202A", fg="white", cursor="hand2")

def cerrar_ventana():
    ventana.destroy()

##FUNCIONES CARGAR_ARCHIVO

def browseFiles(): 
    
    filename = filedialog.askopenfilename(initialdir = "C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab Lenguajes Formales y de Programación/Práctica 1/Programa/Archivos de Entrada"
    , title = "Seleccione un Archivo de Entrada", filetypes = (("Archivos de Datos","*.csv*"),("all files","*.*")))
    print(filename)
    global nombre_archivo
    nombre_archivo = str(filename)
    global state
    state=1


## FUNCIONES GESTIONAR CURSOS

def listar_cursos():
    if state == 1:
        global listar_cursos_ventana
        listar_cursos_ventana = tkinter.Toplevel(ventana) 
        listar_cursos_ventana.title("Listar Cursos")   

        canvas = Canvas(listar_cursos_ventana)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar = ttk.Scrollbar(listar_cursos_ventana, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set,bg="#283747")
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        second_frame= tkinter.Frame(canvas)
        canvas.create_window((0,0),window=second_frame,anchor="nw")
        second_frame.config(bg="#283747")


        ancho_cargar_archivo= 600
        alto_cargar_archivo= 300
        x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
        y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2

        ###TITULOS

        titulo_codigo = tkinter.Label(second_frame,text="Código")
        titulo_codigo.grid(column=0,row=0)
        titulo_codigo.config(bg="#17202A", fg="white")

        titulo_curso = tkinter.Label(second_frame,text="Curso")
        titulo_curso.grid(column=1,row=0)
        titulo_curso.config(bg="#17202A", fg="white")

        titulo_prerrequisitos = tkinter.Label(second_frame,text="Prerrequisitos")
        titulo_prerrequisitos.grid(column=2,row=0)
        titulo_prerrequisitos.config(bg="#17202A", fg="white")

        titulo_obligatorio = tkinter.Label(second_frame,text="Obligatorio")
        titulo_obligatorio.grid(column=3,row=0)
        titulo_obligatorio.config(bg="#17202A", fg="white")

        titulo_semestre = tkinter.Label(second_frame,text="Semestre")
        titulo_semestre.grid(column=4,row=0)
        titulo_semestre.config(bg="#17202A", fg="white")

        titulo_creditos = tkinter.Label(second_frame,text="Creditos")
        titulo_creditos.grid(column=5,row=0)
        titulo_creditos.config(bg="#17202A", fg="white")

        titulo_estado = tkinter.Label(second_frame,text="Estado")
        titulo_estado.grid(column=6,row=0)
        titulo_estado.config(bg="#17202A", fg="white")

        ##LECTOR DE ARCHIVOS
        def lector_archivos():
                with open(nombre_archivo,"r") as archivo:
                    lector = csv.reader(archivo, delimiter=",")
                    i=0
                    for fila in lector:
                        #AHORA QUE TENEMOS LA LISTA, ASIGNAREMOS POSICIONES
                        global obligatorio
                        codigo = int(fila[0])
                        curso = str(fila[1])
                        prerrequisitos = str(fila[2])
                        obligatorio = int(fila[3])
                        semestre = int(fila[4])
                        creditos = int(fila[5])
                        estado = float(fila[6])

                        ###IF'S

                        if obligatorio==1:
                            obligatorio="Obligatorio"
                        elif obligatorio ==0:
                            obligatorio="Opcional"

                        if estado==1:
                            estado = "Cursando"
                        elif estado ==0:
                            estado = "Aprobado"
                        elif estado ==-1:
                            estado ="Pendiente"
                        
                        

                        label_codigo = tkinter.Label(second_frame,text=codigo)
                        label_codigo.grid(column=0,row=1+i)
                        label_codigo.config(bg="#283747", fg="white")

                        label_curso = tkinter.Label(second_frame,text=curso)
                        label_curso.grid(column=1,row=1+i)
                        label_curso.config(bg="#283747", fg="white")

                        label_prerrequisitos = tkinter.Label(second_frame,text=prerrequisitos)
                        label_prerrequisitos.grid(column=2,row=1+i)
                        label_prerrequisitos.config(bg="#283747", fg="white")
                        
                        label_obligatorio = tkinter.Label(second_frame,text=obligatorio)
                        label_obligatorio.grid(column=3,row=1+i)
                        label_obligatorio.config(bg="#283747", fg="white")

                        label_semestre = tkinter.Label(second_frame,text=semestre)
                        label_semestre.grid(column=4,row=1+i)
                        label_semestre.config(bg="#283747", fg="white")

                        label_creditos = tkinter.Label(second_frame,text=creditos)
                        label_creditos.grid(column=5,row=1+i)
                        label_creditos.config(bg="#283747", fg="white")
                        
                        label_estado = tkinter.Label(second_frame,text=estado)
                        label_estado.grid(column=6,row=1+i)
                        label_estado.config(bg="#283747", fg="white")

                        i=i+1                   
        
        lector_archivos()
        posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)
        listar_cursos_ventana.geometry(posicion)
        listar_cursos_ventana.config(bg="#212F3C")
        listar_cursos_ventana.resizable(0,0)

    elif state == 0:
        listar_cursos_ventana = tkinter.Toplevel(ventana) 
        listar_cursos_ventana.title("Listar Cursos")   
        ancho_cargar_archivo= 600
        alto_cargar_archivo= 300
        x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
        y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2

        label = tkinter.Label(listar_cursos_ventana, text="El archivo aun no se ha cargado")
        label.place(x=220,y=145)
        label.config(bg="#212F3C", fg="white")

        posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)
        listar_cursos_ventana.geometry(posicion)
        listar_cursos_ventana.config(bg="#212F3C")
        listar_cursos_ventana.resizable(0,0)

def mostrar_cursos():
    if state == 1:
        nueva_ventana = tkinter.Toplevel(ventana) 
        nueva_ventana.title("Mostrar Cursos")   
        ancho_cargar_archivo= 500
        alto_cargar_archivo= 400
        x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
        y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
        posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

        ##LABELS

        label_codigo_del_curso = tkinter.Label(nueva_ventana, text="Código del curso")
        label_codigo_del_curso.place(x=50,y=50)
        label_codigo_del_curso.config(bg="#212F3C", fg="white",anchor=W)
        
        label_nombre_del_curso = tkinter.Label(nueva_ventana, text="Nombre del curso")
        label_nombre_del_curso.place(x=50,y=110)
        label_nombre_del_curso.config(bg="#212F3C", fg="white",anchor=W)

        label_prerrequisitos = tkinter.Label(nueva_ventana, text="Prerrequisitos")
        label_prerrequisitos.place(x=50,y=140)
        label_prerrequisitos.config(bg="#212F3C", fg="white",anchor=W)

        label_obligatorio = tkinter.Label(nueva_ventana, text="Obligatorio")
        label_obligatorio.place(x=50,y=170)
        label_obligatorio.config(bg="#212F3C", fg="white",anchor=W)

        label_semestre = tkinter.Label(nueva_ventana, text="Semestre")
        label_semestre.place(x=50,y=200)
        label_semestre.config(bg="#212F3C", fg="white",anchor=W)
        
        label_creditos = tkinter.Label(nueva_ventana, text="Creditos")
        label_creditos.place(x=50,y=230)
        label_creditos.config(bg="#212F3C", fg="white",anchor=W)
        
        label_estado = tkinter.Label(nueva_ventana, text="Estado")
        label_estado.place(x=50,y=260)
        label_estado.config(bg="#212F3C", fg="white",anchor=W)

        ##VARIABLES DE LOS ENTRYS

        num_codigo = IntVar()
        nombre_del_curso = StringVar()
        prerrequisitos_del_curso=StringVar()
        obligatorio_del_curso=StringVar()
        semestre_del_curso=IntVar()
        creditos_del_curso=IntVar()
        estado_del_curso=StringVar()

        ##ENTRYS

        codigo = tkinter.Entry(nueva_ventana, textvariable=num_codigo)
        codigo.config(width=45,bg="#1C2833", fg="white")
        codigo.place(x=160,y=50)

        nombre = tkinter.Entry(nueva_ventana, textvariable=nombre_del_curso)
        nombre.config(width=45,bg="#1C2833", fg="white")
        nombre.place(x=160,y=110)

        prerrequisitos = tkinter.Entry(nueva_ventana, textvariable=prerrequisitos_del_curso)
        prerrequisitos.config(width=45,bg="#1C2833", fg="white")
        prerrequisitos.place(x=160,y=140)

        obligatorio = tkinter.Entry(nueva_ventana, textvariable=obligatorio_del_curso)
        obligatorio.config(width=45,bg="#1C2833", fg="white")
        obligatorio.place(x=160,y=170)

        semestre = tkinter.Entry(nueva_ventana, textvariable=semestre_del_curso)
        semestre.config(width=45,bg="#1C2833", fg="white")
        semestre.place(x=160,y=200)

        creditos = tkinter.Entry(nueva_ventana, textvariable=creditos_del_curso)
        creditos.config(width=45,bg="#1C2833", fg="white")
        creditos.place(x=160,y=230)

        estado = tkinter.Entry(nueva_ventana, textvariable=estado_del_curso)
        estado.config(width=45,bg="#1C2833", fg="white")
        estado.place(x=160,y=260)


        def buscar_codigo():

            global codigo_de_curso
            codigo_de_curso=int(num_codigo.get())

            print(codigo_de_curso)

            with open(nombre_archivo,"r") as archivo:
                    lector = csv.reader(archivo, delimiter=",")
                    i=0
                    for fila in lector:
                        #AHORA QUE TENEMOS LA LISTA, ASIGNAREMOS POSICIONES
                        global obligatorio
                        codigo = int(fila[0])
                        curso = str(fila[1])
                        prerrequisitos = str(fila[2])
                        obligatorio = int(fila[3])
                        semestre = int(fila[4])
                        creditos = int(fila[5])
                        estado = float(fila[6])

                        ###IF'S

                        if obligatorio==1:
                            obligatorio="Obligatorio"
                        elif obligatorio ==0:
                            obligatorio="Opcional"

                        if estado==1:
                            estado = "Cursando"
                        elif estado ==0:
                            estado = "Aprobado"
                        elif estado ==-1:
                            estado ="Pendiente"
                        
                        if codigo_de_curso == codigo:
                            print("Ya estamos bien hasta el momento")
                            nombre_del_curso.set(curso)
                            prerrequisitos_del_curso.set(prerrequisitos)
                            obligatorio_del_curso.set(obligatorio)
                            semestre_del_curso.set(semestre)
                            creditos_del_curso.set(creditos)
                            estado_del_curso.set(estado)
                            

        
        ##BOTON

        boton = tkinter.Button(nueva_ventana, text="Buscar curso", command=buscar_codigo)
        boton.config(bg="#17202A", fg="white", cursor="hand2")
        boton.place(x=210,y=320) 
        


        nueva_ventana.geometry(posicion)
        nueva_ventana.config(bg="#212F3C")
        nueva_ventana.resizable(0,0)

    elif state == 0:
        nueva_ventana = tkinter.Toplevel(ventana) 
        nueva_ventana.title("Mostrar Cursos")   
        ancho_cargar_archivo= 500
        alto_cargar_archivo= 400
        x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
        y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
        posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

        label = tkinter.Label(nueva_ventana, text="El archivo aun no se ha cargado")
        label.place(x=175,y=195)
        label.config(bg="#212F3C", fg="white")

        nueva_ventana.geometry(posicion)
        nueva_ventana.config(bg="#212F3C")
        nueva_ventana.resizable(0,0)


def agregar_cursos():
    if state == 1:
        nueva_ventana = tkinter.Toplevel(ventana) 
        nueva_ventana.title("Agregar Cursos")   
        ancho_cargar_archivo= 500
        alto_cargar_archivo= 400
        x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
        y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
        posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

        ##LABELS

        label_codigo_del_curso = tkinter.Label(nueva_ventana, text="Código del curso")
        label_codigo_del_curso.place(x=50,y=50)
        label_codigo_del_curso.config(bg="#212F3C", fg="white",anchor=W)
        
        label_nombre_del_curso = tkinter.Label(nueva_ventana, text="Nombre del curso")
        label_nombre_del_curso.place(x=50,y=80)
        label_nombre_del_curso.config(bg="#212F3C", fg="white",anchor=W)

        label_prerrequisitos = tkinter.Label(nueva_ventana, text="Prerrequisitos")
        label_prerrequisitos.place(x=50,y=110)
        label_prerrequisitos.config(bg="#212F3C", fg="white",anchor=W)

        label_obligatorio = tkinter.Label(nueva_ventana, text="Obligatorio")
        label_obligatorio.place(x=50,y=130)
        label_obligatorio.config(bg="#212F3C", fg="white",anchor=W)

        label_semestre = tkinter.Label(nueva_ventana, text="Semestre")
        label_semestre.place(x=50,y=170)
        label_semestre.config(bg="#212F3C", fg="white",anchor=W)
        
        label_creditos = tkinter.Label(nueva_ventana, text="Creditos")
        label_creditos.place(x=50,y=200)
        label_creditos.config(bg="#212F3C", fg="white",anchor=W)
        
        label_estado = tkinter.Label(nueva_ventana, text="Estado")
        label_estado.place(x=50,y=230)
        label_estado.config(bg="#212F3C", fg="white",anchor=W)

        ##VARIABLES DE LOS ENTRYS

        num_codigo = IntVar()
        nombre_del_curso = StringVar()
        prerrequisitos_del_curso=StringVar()
        obligatorio_del_curso=StringVar()
        semestre_del_curso=IntVar()
        creditos_del_curso=IntVar()
        estado_del_curso=StringVar()

        ##ENTRYS

        codigo = tkinter.Entry(nueva_ventana, textvariable=num_codigo)
        codigo.config(width=45,bg="#1C2833", fg="white")
        codigo.place(x=160,y=50)

        nombre = tkinter.Entry(nueva_ventana, textvariable=nombre_del_curso)
        nombre.config(width=45,bg="#1C2833", fg="white")
        nombre.place(x=160,y=80)

        prerrequisitos = tkinter.Entry(nueva_ventana, textvariable=prerrequisitos_del_curso)
        prerrequisitos.config(width=45,bg="#1C2833", fg="white")
        prerrequisitos.place(x=160,y=110)

        obligatorio = tkinter.Entry(nueva_ventana, textvariable=obligatorio_del_curso)
        obligatorio.config(width=45,bg="#1C2833", fg="white")
        obligatorio.place(x=160,y=140)

        semestre = tkinter.Entry(nueva_ventana, textvariable=semestre_del_curso)
        semestre.config(width=45,bg="#1C2833", fg="white")
        semestre.place(x=160,y=170)

        creditos = tkinter.Entry(nueva_ventana, textvariable=creditos_del_curso)
        creditos.config(width=45,bg="#1C2833", fg="white")
        creditos.place(x=160,y=200)

        estado = tkinter.Entry(nueva_ventana, textvariable=estado_del_curso)
        estado.config(width=45,bg="#1C2833", fg="white")
        estado.place(x=160,y=230)


        def nuevo_curso():
            with open(nombre_archivo,"r") as archivo:
                lector = csv.reader(archivo, delimiter=",")
                global contador
                contador = 0
                for fila in lector:
                    codigo = int(fila[0])
                    compar_codigo = int(num_codigo.get())
                    codigo_de_curso=str(num_codigo.get())
                    nombre_de_curso=str(nombre_del_curso.get())
                    prerrequisitos_de_curso=str(prerrequisitos_del_curso.get())
                    obligatorio_de_curso=str(obligatorio_del_curso.get())
                    semestre_de_curso=str(semestre_del_curso.get())
                    creditos_de_curso=str(creditos_del_curso.get())
                    estado_de_curso=str(estado_del_curso.get())
                    if codigo == compar_codigo:
                        contador=1
            if contador ==0:
                with open(nombre_archivo,"a") as archivo:
                    archivo.write("\n")
                    archivo.write(codigo_de_curso+","+nombre_de_curso+","+prerrequisitos_de_curso+","+obligatorio_de_curso+","+semestre_de_curso
                    +","+creditos_de_curso+","+estado_de_curso)
            if contador ==1:
                nueva_ventana = tkinter.Toplevel(ventana) 
                nueva_ventana.title("Error")   
                ancho_cargar_archivo= 300
                alto_cargar_archivo= 50
                x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
                y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
                posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

                label = tkinter.Label(nueva_ventana, text="El curso que intenta agregar ya existe")
                label.place(x=40,y=15)
                label.config(bg="#212F3C", fg="white")

                nueva_ventana.geometry(posicion)
                nueva_ventana.config(bg="#212F3C")
                nueva_ventana.resizable(0,0)

        
        ##BOTON

        boton = tkinter.Button(nueva_ventana, text="Agregar curso", command=nuevo_curso)
        boton.config(bg="#17202A", fg="white", cursor="hand2")
        boton.place(x=210,y=320) 
        


        nueva_ventana.geometry(posicion)
        nueva_ventana.config(bg="#212F3C")
        nueva_ventana.resizable(0,0)

    elif state == 0:
        nueva_ventana = tkinter.Toplevel(ventana) 
        nueva_ventana.title("Agregar Cursos")   
        ancho_cargar_archivo= 500
        alto_cargar_archivo= 400
        x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
        y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
        posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

        label = tkinter.Label(nueva_ventana, text="El archivo aun no se ha cargado")
        label.place(x=175,y=195)
        label.config(bg="#212F3C", fg="white")

        nueva_ventana.geometry(posicion)
        nueva_ventana.config(bg="#212F3C")
        nueva_ventana.resizable(0,0)




def editar_cursos():
    nueva_ventana = tkinter.Toplevel(ventana) 
    nueva_ventana.title("Editar Cursos")   
    ancho_cargar_archivo= 500
    alto_cargar_archivo= 400
    x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
    y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
    posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

    ##LABELS

    label_codigo_del_curso = tkinter.Label(nueva_ventana, text="Código del curso")
    label_codigo_del_curso.place(x=50,y=50)
    label_codigo_del_curso.config(bg="#212F3C", fg="white",anchor=W)
    
    label_nombre_del_curso = tkinter.Label(nueva_ventana, text="Nombre del curso")
    label_nombre_del_curso.place(x=50,y=80)
    label_nombre_del_curso.config(bg="#212F3C", fg="white",anchor=W)

    label_prerrequisitos = tkinter.Label(nueva_ventana, text="Prerrequisitos")
    label_prerrequisitos.place(x=50,y=110)
    label_prerrequisitos.config(bg="#212F3C", fg="white",anchor=W)

    label_obligatorio = tkinter.Label(nueva_ventana, text="Obligatorio")
    label_obligatorio.place(x=50,y=130)
    label_obligatorio.config(bg="#212F3C", fg="white",anchor=W)

    label_semestre = tkinter.Label(nueva_ventana, text="Semestre")
    label_semestre.place(x=50,y=170)
    label_semestre.config(bg="#212F3C", fg="white",anchor=W)
    
    label_creditos = tkinter.Label(nueva_ventana, text="Creditos")
    label_creditos.place(x=50,y=200)
    label_creditos.config(bg="#212F3C", fg="white",anchor=W)
    
    label_estado = tkinter.Label(nueva_ventana, text="Estado")
    label_estado.place(x=50,y=230)
    label_estado.config(bg="#212F3C", fg="white",anchor=W)

    ##VARIABLES DE LOS ENTRYS

    num_codigo = IntVar()
    nombre_del_curso = StringVar()
    prerrequisitos_del_curso=StringVar()
    obligatorio_del_curso=StringVar()
    semestre_del_curso=IntVar()
    creditos_del_curso=IntVar()
    estado_del_curso=StringVar()

    ##ENTRYS

    codigo = tkinter.Entry(nueva_ventana, textvariable=num_codigo)
    codigo.config(width=45,bg="#1C2833", fg="white")
    codigo.place(x=160,y=50)

    nombre = tkinter.Entry(nueva_ventana, textvariable=nombre_del_curso)
    nombre.config(width=45,bg="#1C2833", fg="white")
    nombre.place(x=160,y=80)

    prerrequisitos = tkinter.Entry(nueva_ventana, textvariable=prerrequisitos_del_curso)
    prerrequisitos.config(width=45,bg="#1C2833", fg="white")
    prerrequisitos.place(x=160,y=110)

    obligatorio = tkinter.Entry(nueva_ventana, textvariable=obligatorio_del_curso)
    obligatorio.config(width=45,bg="#1C2833", fg="white")
    obligatorio.place(x=160,y=140)

    semestre = tkinter.Entry(nueva_ventana, textvariable=semestre_del_curso)
    semestre.config(width=45,bg="#1C2833", fg="white")
    semestre.place(x=160,y=170)

    creditos = tkinter.Entry(nueva_ventana, textvariable=creditos_del_curso)
    creditos.config(width=45,bg="#1C2833", fg="white")
    creditos.place(x=160,y=200)

    estado = tkinter.Entry(nueva_ventana, textvariable=estado_del_curso)
    estado.config(width=45,bg="#1C2833", fg="white")
    estado.place(x=160,y=230)


    def buscar_codigo():
        with open(nombre_archivo,"r") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            global contador
            contador = 0
            for fila in lector:
                codigo = int(fila[0])
                compar_codigo = int(num_codigo.get())
                codigo_de_curso=str(num_codigo.get())
                nombre_de_curso=str(nombre_del_curso.get())
                prerrequisitos_de_curso=str(prerrequisitos_del_curso.get())
                obligatorio_de_curso=str(obligatorio_del_curso.get())
                semestre_de_curso=str(semestre_del_curso.get())
                creditos_de_curso=str(creditos_del_curso.get())
                estado_de_curso=str(estado_del_curso.get())
                if codigo == compar_codigo:
                    contador=1

        codigo_de_curso=int(num_codigo.get())
        with open(nombre_archivo,"r") as archivo:
                lector = csv.reader(archivo, delimiter=",")
                i=-1
                for fila in lector:
                    #AHORA QUE TENEMOS LA LISTA, ASIGNAREMOS POSICIONES
                    codigo = int(fila[0])
                    i=i+1
                    ###IF'S
                    if codigo_de_curso == codigo:
                        print(i)
                        with open(nombre_archivo,"r") as documento:
                            lineas=documento.readlines()
                        with open (nombre_archivo,"w") as documento:
                            linea=lineas[i]
                            lineas.remove(linea)
                            for linea in lineas:
                                documento.write(linea)

        if contador ==0:

            nueva_ventana = tkinter.Toplevel(ventana) 
            nueva_ventana.title("Error")   
            ancho_cargar_archivo= 300
            alto_cargar_archivo= 50
            x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
            y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
            posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

            label = tkinter.Label(nueva_ventana, text="El curso que intenta editar no existe")
            label.place(x=40,y=15)
            label.config(bg="#212F3C", fg="white")

            nueva_ventana.geometry(posicion)
            nueva_ventana.config(bg="#212F3C")
            nueva_ventana.resizable(0,0)

        if contador ==1:

            with open(nombre_archivo,"a") as archivo:
                archivo.write("\n")
                codigo_de_curso = str(num_codigo.get())
                archivo.write(codigo_de_curso+","+nombre_de_curso+","+prerrequisitos_de_curso+","+obligatorio_de_curso+","+semestre_de_curso
                +","+creditos_de_curso+","+estado_de_curso)

    
    ##BOTON

    boton = tkinter.Button(nueva_ventana, text="Editar curso", command=buscar_codigo)
    boton.config(bg="#17202A", fg="white", cursor="hand2")
    boton.place(x=210,y=320) 

    nueva_ventana.geometry(posicion)
    nueva_ventana.config(bg="#212F3C")
    nueva_ventana.resizable(0,0)

def eliminar_curso():
    if state == 1:
        nueva_ventana = tkinter.Toplevel(ventana) 
        nueva_ventana.title("Eliminar Curso")   
        ancho_cargar_archivo= 400
        alto_cargar_archivo= 140
        x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
        y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
        posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

        ##LABELS

        label_codigo_del_curso = tkinter.Label(nueva_ventana, text="Código del curso")
        label_codigo_del_curso.place(x=35,y=50)
        label_codigo_del_curso.config(bg="#212F3C", fg="white",anchor=W)
        
        ##VARIABLE ENTRYS

        num_codigo = IntVar()

        ##ENTRY'S

        codigo = tkinter.Entry(nueva_ventana, textvariable=num_codigo)
        codigo.config(width=35,bg="#1C2833", fg="white")
        codigo.place(x=135,y=50)

        def buscar_codigo():

            global codigo_de_curso
            codigo_de_curso=int(num_codigo.get())
            with open(nombre_archivo,"r") as archivo:
                    lector = csv.reader(archivo, delimiter=",")
                    i=-1
                    for fila in lector:
                        #AHORA QUE TENEMOS LA LISTA, ASIGNAREMOS POSICIONES
                        codigo = int(fila[0])
                        i=i+1
                        ###IF'S
                        if codigo_de_curso == codigo:
                            print(i)
                            with open(nombre_archivo,"r") as documento:
                                lineas=documento.readlines()
                            with open (nombre_archivo,"w") as documento:
                                linea=lineas[i]
                                lineas.remove(linea)
                                for linea in lineas:
                                    documento.write(linea)

        ##BOTON

        boton = tkinter.Button(nueva_ventana, text="Eliminar", command=buscar_codigo)
        boton.config(bg="#17202A", fg="white", cursor="hand2")
        boton.place(x=290,y=90) 

        nueva_ventana.geometry(posicion)
        nueva_ventana.config(bg="#212F3C")
        nueva_ventana.resizable(0,0)

    elif state == 0:
        
        nueva_ventana = tkinter.Toplevel(ventana) 
        nueva_ventana.title("Eliminar Curso")   
        ancho_cargar_archivo= 400
        alto_cargar_archivo= 200
        x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
        y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2
        posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

        label = tkinter.Label(nueva_ventana, text="El archivo aun no se ha cargado")
        label.place(x=120,y=95)
        label.config(bg="#212F3C", fg="white")

        nueva_ventana.geometry(posicion)
        nueva_ventana.config(bg="#212F3C")
        nueva_ventana.resizable(0,0)


def conteo_creditos():
    print("Hola")
    if state == 1:
        global conteo_creditos_ventana
        conteo_creditos_ventana = tkinter.Toplevel(ventana) 
        conteo_creditos_ventana.title("Conteo de  Creditos")   
        ancho_cargar_archivo= 600
        alto_cargar_archivo= 500
        x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
        y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2


        ##LECTOR DE ARCHIVOS
        def lector_archivos():
            with open(nombre_archivo,"r") as archivo:
                lector = csv.reader(archivo, delimiter=",")
                creditos_aprobados = 0
                creditos_cursando = 0
                creditos_pendientes = 0
                for fila in lector:
                    #AHORA QUE TENEMOS LA LISTA, ASIGNAREMOS POSICIONES
                    global obligatorio
                    obligatorio = int(fila[3])
                    creditos = int(fila[5])
                    estado = float(fila[6])

                    ###IF'S
                    
                    if estado == 0:
                        creditos_aprobados = creditos_aprobados+creditos

                    if estado == 1:
                        creditos_cursando = creditos_cursando+creditos
                    
                    if obligatorio ==1:
                        if estado ==-1:
                            creditos_pendientes = creditos_pendientes+creditos

                
            print(creditos_aprobados)
            print(creditos_cursando)

            ##LABELS CREDITOS APROBADOS

            label_creditos_aprobados = tkinter.Label(conteo_creditos_ventana, text="Creditos Aprobados:")
            label_creditos_aprobados.place(x=200,y=50)
            label_creditos_aprobados.config(bg="#212F3C", fg="white")

            creditos1= tkinter.Label(conteo_creditos_ventana, text=creditos_aprobados)
            creditos1.place(x=350,y=50)
            creditos1.config(bg="#212F3C", fg="white")

            ##LABELS CREDITOS APROBADOS

            label_creditos_cursando = tkinter.Label(conteo_creditos_ventana, text="Creditos Cursando:")
            label_creditos_cursando.place(x=200,y=100)
            label_creditos_cursando.config(bg="#212F3C", fg="white")

            creditos2= tkinter.Label(conteo_creditos_ventana, text=creditos_cursando)
            creditos2.place(x=350,y=100)
            creditos2.config(bg="#212F3C", fg="white")
            
            ##LABELS CREDITOS PENDIENTES

            label_creditos_pendientes = tkinter.Label(conteo_creditos_ventana, text="Creditos Pendientes:")
            label_creditos_pendientes.place(x=200,y=150)
            label_creditos_pendientes.config(bg="#212F3C", fg="white")

            creditos1= tkinter.Label(conteo_creditos_ventana, text=creditos_pendientes)
            creditos1.place(x=350,y=150)
            creditos1.config(bg="#212F3C", fg="white")

            ##LABELS CREDITOS OBLIGATORIOS HASTA SEMESTRE N

            valor=""
            label_creditos_hasta_semestre_n = tkinter.Label(conteo_creditos_ventana, text=("Creditos obligatorios hasta Semestre:" + valor))
            label_creditos_hasta_semestre_n.place(x=100,y=200)
            label_creditos_hasta_semestre_n.config(bg="#212F3C", fg="white")

            cantidad = tkinter.Label(conteo_creditos_ventana, text="Semestre:")
            cantidad.place(x=150,y=250)
            cantidad.config(bg="#212F3C", fg="white")

            global opciones
            opciones= ttk.Combobox(conteo_creditos_ventana,state="readonly", values=[1,2,3,4,5,6,7,8,9,10])
            opciones.place(x=215,y=250)
            valor = opciones.get()

            ##LABELS CREDITOS HASTA N SEMESTRE

            valor=""
            label_creditos_hasta_semestre_n = tkinter.Label(conteo_creditos_ventana, text=("Creditos del Semestre: "))
            label_creditos_hasta_semestre_n.place(x=100,y=300)
            label_creditos_hasta_semestre_n.config(bg="#212F3C", fg="white")

            global opciones2
            opciones2= ttk.Combobox(conteo_creditos_ventana,state="readonly", values=[1,2,3,4,5,6,7,8,9,10])
            opciones2.place(x=235,y=300)
            valor2 = opciones2.get()

            ##METODO PARA OBTENER SEMESTRE

        def semestre():
            valor = opciones.get()
            label_creditos_hasta_semestre_n = tkinter.Label(conteo_creditos_ventana, text=("Creditos obligatorios hasta Semestre " + valor+":"))
            label_creditos_hasta_semestre_n.place(x=100,y=200)
            label_creditos_hasta_semestre_n.config(bg="#212F3C", fg="white")
            with open(nombre_archivo,"r") as archivo:
                lector = csv.reader(archivo, delimiter=",")
                credis = 0
                for fila in lector:
                    #AHORA QUE TENEMOS LA LISTA, ASIGNAREMOS POSICIONES
                    global obligatorio
                    obligatorio = int(fila[3])
                    semestre = int(fila[4])
                    creditos = int(fila[5])

                    ###IF'S
                    valor = int(valor)
                    if semestre <= valor:
                        if obligatorio ==1:
                                credis = credis+creditos
            creditos_obliga= tkinter.Label(conteo_creditos_ventana, text=credis)
            creditos_obliga.place(x=350,y=200)
            creditos_obliga.config(bg="#212F3C", fg="white")

        def por_semestre():
            valor2 = opciones2.get()
            with open(nombre_archivo,"r") as archivo:
                lector = csv.reader(archivo, delimiter=",")
                creditos_aprobados_1 = 0
                creditos_cursando_1 = 0
                creditos_pendientes_1 = 0
                for fila in lector:
                    #AHORA QUE TENEMOS LA LISTA, ASIGNAREMOS POSICIONES
                    global obligatorio
                    semestre = int(fila[4])
                    obligatorio = int(fila[3])
                    creditos = int(fila[5])
                    estado = float(fila[6])

                    ###IF'S
                    valor2= int(valor2)
                    if semestre == valor2:
                        if estado == 0:
                            creditos_aprobados_1 = creditos_aprobados_1+creditos

                    if semestre == valor2:
                        if estado == 1:
                            creditos_cursando_1 = creditos_cursando_1+creditos
                    
                    if semestre == valor2:
                        if estado ==-1:
                            creditos_pendientes_1 = creditos_pendientes_1+creditos

            aprobados = tkinter.Label(conteo_creditos_ventana, text="Aprobados: "+str(creditos_aprobados_1))
            aprobados.place(x=150, y=340)
            aprobados.config(bg="#212F3C", fg="white")

            cursando = tkinter.Label(conteo_creditos_ventana, text="Cursando: "+str(creditos_cursando_1))
            cursando.place(x=260, y=340)
            cursando.config(bg="#212F3C", fg="white")

            pendientes = tkinter.Label(conteo_creditos_ventana, text="Pendientes: "+str(creditos_pendientes_1))
            pendientes.place(x=360, y=340)
            pendientes.config(bg="#212F3C", fg="white")

        ##BOTON

        boton = tkinter.Button(conteo_creditos_ventana, text="Contar", command=semestre)
        boton.config(bg="#17202A", fg="white", cursor="hand2")
        boton.place(x=380,y=250) 

        boton = tkinter.Button(conteo_creditos_ventana, text="Contar", command=por_semestre)
        boton.config(bg="#17202A", fg="white", cursor="hand2")
        boton.place(x=400,y=300) 


        lector_archivos()
        posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)
        conteo_creditos_ventana.geometry(posicion)
        conteo_creditos_ventana.config(bg="#212F3C")
        conteo_creditos_ventana.resizable(0,0)

    elif state == 0:
        conteo_creditos_ventana = tkinter.Toplevel(ventana) 
        conteo_creditos_ventana.title("Listar Cursos")   
        ancho_cargar_archivo= 600
        alto_cargar_archivo= 300
        x_cargar_archivo = cargar_archivo.winfo_screenwidth()//2-ancho_cargar_archivo//2
        y_cargar_archivo = cargar_archivo.winfo_screenheight()//2-alto_cargar_archivo//2

        label = tkinter.Label(conteo_creditos_ventana, text="El archivo aun no se ha cargado")
        label.place(x=220,y=145)
        label.config(bg="#212F3C", fg="white")

        posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)
        conteo_creditos_ventana.geometry(posicion)
        conteo_creditos_ventana.config(bg="#212F3C")
        conteo_creditos_ventana.resizable(0,0)




##VENTANA

ventana = tkinter.Tk()
ventana.title("Práctica 1")
ventana.state("zoomed")
ventana.iconbitmap("C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab Lenguajes Formales y de Programación/Práctica 1/Programa/logo.ico")
ventana.config(bg="#212F3C")

##FRAME

frame = tkinter.Frame(ventana, width=800, height=500)
ancho_frame= 800
alto_frame= 500
x_frame = frame.winfo_screenwidth()//2-ancho_frame//2
y_frame = frame.winfo_screenheight()//2-alto_frame//2
posicion=str(ancho_frame)+"x"+str(alto_frame)+"+"+str(x_frame)+"+"+str(y_frame)
ventana.geometry(posicion)
frame.config(bg="#212F3C")
frame.pack()


imagen=tkinter.PhotoImage(file="C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab Lenguajes Formales y de Programación/Práctica 1/Programa/Usac_logo.png")
tkinter.Label(frame, image=imagen).place(x=350,y=100)

nombre_curso = tkinter.Label(frame, text= "Nombre del Curso: Lab. Lenguajes Formales y de Programación")
nombre_curso.place(x=50, y=220)
nombre_curso.config(bg="#212F3C", fg="white")
 

nombre_estudiante = tkinter.Label(frame, text= "Nombre del Estudiante: Geovanny Sebastián Herrera Claudio")
nombre_estudiante.place(x=50, y=240)
nombre_estudiante.config(bg="#212F3C", fg="white")

carne_estudiante = tkinter.Label(frame, text= "Carnpe del Estudiante: 202110588")
carne_estudiante.place(x=50, y=260)
carne_estudiante.config(bg="#212F3C", fg="white")

cargar_archivo = tkinter.Button(frame, text="Cargar Archivo", command=abrir_cargar_archivos)
cargar_archivo.place(x=375, y=310)
cargar_archivo.config(bg="#17202A", fg="white", cursor="hand2")

gestionar_cursos = tkinter.Button(frame, text="Gestionar Cursos", command=abrir_gestionar_cursos)
gestionar_cursos.place(x=370, y=350)
gestionar_cursos.config(bg="#17202A", fg="white", cursor="hand2")

conteo_creditos = tkinter.Button(frame, text="Conteo de Créditos", command=conteo_creditos)
conteo_creditos.place(x=363, y=390)
conteo_creditos.config(bg="#17202A", fg="white", cursor="hand2")

salir = tkinter.Button(frame, text="Salir", command=cerrar_ventana)
salir.place(x=402, y=430)
salir.config(bg="#17202A", fg="white", cursor="hand2")

##MAINLOOP

ventana.mainloop()