import tkinter
import customtkinter
from PIL import Image
import csv
from tkinter import StringVar,IntVar,DoubleVar
#from telas import Tela
from model.tela_dao import Tela,guardar, CrearTabla
customtkinter.set_appearance_mode("light")

#TELAS LIST

telas = []
"""CrearTabla()"""

##VENTANA

ventana = tkinter.Tk()
ventana.title("Inventario Nicteel")
ventana.state("zoomed")
ventana.iconbitmap("img/N.ico")



##FRAME

frame = tkinter.Frame(ventana)
frame.config(bg="white")

#LOGO
logo = tkinter.PhotoImage(file="img/Logo.png")
img = tkinter.Label(frame, image=logo, width=600,height=150,bg="white")
img.place(relx=0.5,y=140, anchor=tkinter.CENTER)
frame.pack(expand=1,fill=tkinter.BOTH)



    #LECTOR DE ARCHIVOS
"""def lectorInventario():
    with open("inventario ofi.csv","r") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        for fila in lector:
            #AHORA QUE TENEMOS LA LISTA, ASIGNAREMOS POSICIONES
            estanteRepisa = str(fila[0])
            codigo = str(fila[1])
            nombre = str(fila[2])
            tipo = str(fila[3])
            precioYarda = str(fila[4])  
            precioVenta = str(fila[5])
            stock = float(fila[7])         
            print(estanteRepisa,codigo,nombre,tipo,precioVenta,precioYarda,stock)           

            tela = Tela(estanteRepisa,codigo,nombre,tipo,precioYarda,precioVenta,stock)
            guardar(tela)
"""
#LÓGICA



def inventario():

    inventarioWindow = tkinter.Toplevel(frame) 
    inventarioWindow.title("Inventario")   
    inventarioWindow.iconbitmap("img/N.ico")

    canvas = tkinter.Canvas(inventarioWindow)
    canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    scrollbar = tkinter.Scrollbar(inventarioWindow, orient=tkinter.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    canvas.configure(yscrollcommand=scrollbar.set,bg="white")
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    second_frame= tkinter.Frame(canvas)
    canvas.create_window((0,0),window=second_frame,anchor="nw")
    second_frame.config(bg="white")


    ###TITULOS
    second_frame.columnconfigure(0,weight=20)

    titulo_codigo = tkinter.Label(second_frame,text="Estante y Repisa",font=("Roboto Black",18))
    titulo_codigo.grid(column=0,row=0,padx=15)
    titulo_codigo.config(bg="white", fg="#0e1111")

    titulo_curso = tkinter.Label(second_frame,text="Código",font=("Roboto Black",18))
    titulo_curso.grid(column=1,row=0,padx=15)
    titulo_curso.config(bg="white", fg="#0e1111")

    titulo_prerrequisitos = tkinter.Label(second_frame,text="Nombre",font=("Roboto Black",18))
    titulo_prerrequisitos.grid(column=2,row=0,padx=15)
    titulo_prerrequisitos.config(bg="white", fg="#0e1111")

    titulo_prerrequisitos = tkinter.Label(second_frame,text="Tipo",font=("Roboto Black",18))
    titulo_prerrequisitos.grid(column=3,row=0,padx=15)
    titulo_prerrequisitos.config(bg="white", fg="#0e1111")

    titulo_obligatorio = tkinter.Label(second_frame,text="Precio por Yarda",font=("Roboto Black",18))
    titulo_obligatorio.grid(column=4,row=0,padx=15)
    titulo_obligatorio.config(bg="white", fg="#0e1111")

    titulo_semestre = tkinter.Label(second_frame,text="Precio de Venta",font=("Roboto Black",18))
    titulo_semestre.grid(column=5,row=0,padx=15)
    titulo_semestre.config(bg="white", fg="#0e1111")

    titulo_semestre = tkinter.Label(second_frame,text="Stock",font=("Roboto Black",18))
    titulo_semestre.grid(column=6,row=0,padx=15)
    titulo_semestre.config(bg="white", fg="#0e1111")

    i=0
    for x in telas:
        label_codigo = tkinter.Label(second_frame,text=x.estanteRepisa,font=("Roboto Black",12))
        label_codigo.grid(column=0,row=1+i)
        label_codigo.config(bg="white", fg="#4D5656")

        label_curso = tkinter.Label(second_frame,text=x.codigo,font=("Roboto Black",12))
        label_curso.grid(column=1,row=1+i)
        label_curso.config(bg="white", fg="#4D5656")

        label_prerrequisitos = tkinter.Label(second_frame,text=x.nombre,font=("Roboto Black",12))
        label_prerrequisitos.grid(column=2,row=1+i)
        label_prerrequisitos.config(bg="white", fg="#4D5656")
        
        label_obligatorio = tkinter.Label(second_frame,text=x.tipo,font=("Roboto Black",12))
        label_obligatorio.grid(column=3,row=1+i)
        label_obligatorio.config(bg="white", fg="#4D5656")

        label_semestre = tkinter.Label(second_frame,text=x.precioYarda,font=("Roboto Black",12))
        label_semestre.grid(column=4,row=1+i)
        label_semestre.config(bg="white", fg="#4D5656")

        label_creditos = tkinter.Label(second_frame,text=x.precioVenta,font=("Roboto Black",12))
        label_creditos.grid(column=5,row=1+i)
        label_creditos.config(bg="white", fg="#4D5656")
        
        if x.stock >=10:
            label_estado = tkinter.Label(second_frame,text=x.stock,font=("Roboto Black",16))
            label_estado.grid(column=6,row=1+i)
            label_estado.config(bg="white", fg="#28B463")
        elif x.stock >=5:
            label_estado = tkinter.Label(second_frame,text=x.stock,font=("Roboto Black",16))
            label_estado.grid(column=6,row=1+i)
            label_estado.config(bg="white", fg="#F4D03F")
        elif x.stock>=0:
            label_estado = tkinter.Label(second_frame,text=x.stock,font=("Roboto Black",16))
            label_estado.grid(column=6,row=1+i)
            label_estado.config(bg="white", fg="#C0392B")

        i=i+1


    inventarioWindow.state("zoomed")
    inventarioWindow.config(bg="white")



def addYardas():
    agregarWindow = tkinter.Toplevel(ventana) 
    agregarWindow.title("Agregar yardas")   
    ancho_frame= 600
    alto_frame= 400
    x_frame = frame.winfo_screenwidth()//2-ancho_frame//2
    y_frame = frame.winfo_screenheight()//2-alto_frame//2
    posicion=str(ancho_frame)+"x"+str(alto_frame)+"+"+str(x_frame)+"+"+str(y_frame)
    agregarWindow.geometry(posicion)
    agregarWindow.config(bg="white")
    agregarWindow.resizable(0,0)

    ##LABELS

    codigoTela = tkinter.Label(agregarWindow, text="Código de la tela",width=14,anchor=tkinter.E)
    codigoTela.place(relx=0.2,rely=0.2)
    codigoTela.config(bg="white", fg="black",anchor=tkinter.E,font=("Roboto Black",18))
    
    cantidadAgregar = tkinter.Label(agregarWindow, text="Yardas a agregar")
    cantidadAgregar.place(relx=0.215,rely=0.4)
    cantidadAgregar.config(bg="white", fg="black",anchor=tkinter.W,font=("Roboto Black",18))

    ##VARIABLES DE LOS ENTRYS

    codigo_var = StringVar()
    agregar = DoubleVar()
    agregar.set(0)

    ##ENTRYS

    codigo_entry = customtkinter.CTkEntry(agregarWindow, textvariable=codigo_var,width=150,height=50,justify="right",font=("Roboto Black",32))
    codigo_entry.place(relx=0.55,rely=0.18)

    nombre = customtkinter.CTkEntry(agregarWindow, textvariable=agregar,width=150,height=50,justify="right",font=("Roboto Black",32))
    nombre.place(relx=0.55,rely=0.38)


    def añadir():
        for x in telas:
            if x.codigo==codigo_var.get():
                x.stock = x.stock+agregar.get()
                codigo_var.set("")
                agregar.set(0)

    #BUTTON

    buttonAddTela = customtkinter.CTkButton(master=agregarWindow,text="Agregar", command=añadir,fg_color=("#0e1111"),hover_color="#000000")
    buttonAddTela.configure(width=200,height=35)
    buttonAddTela.configure(font=("Roboto Black",24))
    imgAddTela = customtkinter.CTkImage(light_image=Image.open("img/plus.png"),size=(35,35))
    buttonAddTela.configure(image=imgAddTela)
    buttonAddTela.configure(border_spacing=14)
    buttonAddTela.place(relx=0.5, rely=0.74, anchor=tkinter.CENTER)


    
def lessYardas():
    quitarWindow = tkinter.Toplevel(ventana) 
    quitarWindow.title("Restar yardas")   
    ancho_frame= 600
    alto_frame= 400
    x_frame = frame.winfo_screenwidth()//2-ancho_frame//2
    y_frame = frame.winfo_screenheight()//2-alto_frame//2
    posicion=str(ancho_frame)+"x"+str(alto_frame)+"+"+str(x_frame)+"+"+str(y_frame)
    quitarWindow.geometry(posicion)
    quitarWindow.config(bg="white")
    quitarWindow.resizable(0,0)

    ##LABELS

    codigoTela = tkinter.Label(quitarWindow, text="Código de la tela",width=14,anchor=tkinter.E)
    codigoTela.place(relx=0.2,rely=0.2)
    codigoTela.config(bg="white", fg="black",anchor=tkinter.E,font=("Roboto Black",18))
    
    cantidadAgregar = tkinter.Label(quitarWindow, text="Yardas a restar")
    cantidadAgregar.place(relx=0.25,rely=0.4)
    cantidadAgregar.config(bg="white", fg="black",anchor=tkinter.W,font=("Roboto Black",18))

    ##VARIABLES DE LOS ENTRYS

    codigo = StringVar()
    quitar = DoubleVar()
    quitar.set(0)

    ##ENTRYS

    codigo = customtkinter.CTkEntry(quitarWindow, textvariable=codigo,width=150,height=50,justify="right",font=("Roboto Black",32))
    codigo.place(relx=0.55,rely=0.18)

    nombre = customtkinter.CTkEntry(quitarWindow, textvariable=quitar,width=150,height=50,justify="right",font=("Roboto Black",32))
    nombre.place(relx=0.55,rely=0.38)


    def less():
        for x in telas:
            if x.codigo==codigo.get():
                x.stock = x.stock-quitar.get()

    #BUTTON

    buttonLessTela = customtkinter.CTkButton(master=quitarWindow,text="Restar", command=less,fg_color=("#0e1111"),hover_color="#000000")
    buttonLessTela.configure(width=200,height=35)
    buttonLessTela.configure(font=("Roboto Black",24))
    imgLessTela = customtkinter.CTkImage(light_image=Image.open("img/less.png"),size=(35,35))
    buttonLessTela.configure(image=imgLessTela)
    buttonLessTela.configure(border_spacing=14)
    buttonLessTela.place(relx=0.5, rely=0.74, anchor=tkinter.CENTER)



def search():
    buscarWindow = tkinter.Toplevel(ventana) 
    buscarWindow.title("Buscar tela")   
    ancho_frame= 900
    alto_frame= 500
    x_frame = frame.winfo_screenwidth()//2-ancho_frame//2
    y_frame = frame.winfo_screenheight()//2-alto_frame//2
    posicion=str(ancho_frame)+"x"+str(alto_frame)+"+"+str(x_frame)+"+"+str(y_frame)
    buscarWindow.geometry(posicion)
    buscarWindow.config(bg="white")
    buscarWindow.resizable(0,0)

    ##LABELS

    codigoTela = tkinter.Label(buscarWindow, text="Código a buscar",width=14,anchor=tkinter.E)
    codigoTela.place(relx=0.02,rely=0.1)
    codigoTela.config(bg="white", fg="black",anchor=tkinter.E,font=("Roboto Black",18))
    
    cantidadAgregar = tkinter.Label(buscarWindow, text="Estante y repisa",width=14,anchor=tkinter.E)
    cantidadAgregar.place(relx=0.02,rely=0.3)
    cantidadAgregar.config(bg="white", fg="#1b1b1b",anchor=tkinter.E,font=("Roboto Black",18))

    nombreTela = tkinter.Label(buscarWindow, text="Nombre",width=14,anchor=tkinter.E)
    nombreTela.place(relx=0.02,rely=0.5)
    nombreTela.config(bg="white", fg="#1b1b1b",anchor=tkinter.E,font=("Roboto Black",18))
    
    tipoTela = tkinter.Label(buscarWindow, text="Tipo",width=14,anchor=tkinter.E)
    tipoTela.place(relx=0.02,rely=0.7)
    tipoTela.config(bg="white", fg="#1b1b1b",anchor=tkinter.E,font=("Roboto Black",18))

    yardaTela = tkinter.Label(buscarWindow, text="Precio por Yarda",width=14,anchor=tkinter.E)
    yardaTela.place(relx=0.5,rely=0.1)
    yardaTela.config(bg="white", fg="#1b1b1b",anchor=tkinter.E,font=("Roboto Black",18))

    ventaTela = tkinter.Label(buscarWindow, text="Precio de Venta",width=14,anchor=tkinter.E)
    ventaTela.place(relx=0.5,rely=0.3)
    ventaTela.config(bg="white", fg="#1b1b1b",anchor=tkinter.E,font=("Roboto Black",18))

    stockTela = tkinter.Label(buscarWindow, text="Stock",width=14,anchor=tkinter.E)
    stockTela.place(relx=0.5,rely=0.5)
    stockTela.config(bg="white", fg="#1b1b1b",anchor=tkinter.E,font=("Roboto Black",18))

    ##VARIABLES DE LOS ENTRYS

    codigoVar = StringVar()
    estanteVar = StringVar()
    nombreVar = StringVar()
    tipoVar = StringVar()
    yardaVar = StringVar()
    ventaVar = StringVar()
    stockVar = StringVar()


    ##ENTRYS

    codigo = customtkinter.CTkEntry(buscarWindow, textvariable=codigoVar,width=150,height=50,justify="right",font=("Roboto Black",32))
    codigo.place(relx=0.3,rely=0.08)

    estante = customtkinter.CTkEntry(buscarWindow, state=tkinter.DISABLED,textvariable=estanteVar,width=150,height=50,justify="right",font=("Roboto Black",32))
    estante.place(relx=0.3,rely=0.28)

    nombre = customtkinter.CTkEntry(buscarWindow, state=tkinter.DISABLED,textvariable=nombreVar,width=150,height=50,justify="right",font=("Roboto Black",32))
    nombre.place(relx=0.3,rely=0.48)

    tipo = customtkinter.CTkEntry(buscarWindow, state=tkinter.DISABLED,textvariable=tipoVar,width=150,height=50,justify="right",font=("Roboto Black",32))
    tipo.place(relx=0.3,rely=0.68)

    yarda = customtkinter.CTkEntry(buscarWindow, state=tkinter.DISABLED,textvariable=yardaVar,width=150,height=50,justify="right",font=("Roboto Black",32))
    yarda.place(relx=0.77,rely=0.08)

    venta = customtkinter.CTkEntry(buscarWindow, state=tkinter.DISABLED,textvariable=ventaVar,width=150,height=50,justify="right",font=("Roboto Black",32))
    venta.place(relx=0.77,rely=0.28)

    stock = customtkinter.CTkEntry(buscarWindow, state=tkinter.DISABLED,textvariable=stockVar,width=150,height=50,justify="right",font=("Roboto Black",32))
    stock.place(relx=0.77,rely=0.48)


    def searching():
        for x in telas:
            if x.codigo==codigo.get():
                estanteVar.set(x.estanteRepisa)
                nombreVar.set(x.nombre)
                tipoVar.set(x.tipo)
                yardaVar.set(x.precioYarda)
                ventaVar.set(x.precioVenta)
                stockVar.set(x.stock)

    buttonSearch = customtkinter.CTkButton(master=buscarWindow,text="Buscar", command=searching,fg_color=("#0e1111"),hover_color="#000000")
    buttonSearch.configure(width=200,height=35)
    buttonSearch.configure(font=("Roboto Black",24))
    imgSearch = customtkinter.CTkImage(light_image=Image.open("img/search.png"),size=(35,35))
    buttonSearch.configure(image=imgSearch)
    buttonSearch.configure(border_spacing=14)
    buttonSearch.place(relx=0.5, rely=0.90, anchor=tkinter.CENTER)




#BOTONES

buttonInventario = customtkinter.CTkButton(master=frame,text="Inventario", command=inventario,fg_color=("#0e1111"),hover_color="#000000")
buttonInventario.configure(width=200,height=35)
buttonInventario.configure(font=("Roboto Black",24))
imgInventario = customtkinter.CTkImage(light_image=Image.open("img/inventario.png"),size=(35,35))
buttonInventario.configure(image=imgInventario)
buttonInventario.configure(border_spacing=14)
buttonInventario.place(relx=0.5, rely=0.50, anchor=tkinter.CENTER)

buttonAddTela = customtkinter.CTkButton(master=frame,text="Buscar tela", command=search,fg_color=("#0e1111"),hover_color="#000000")
buttonAddTela.configure(width=200,height=35)
buttonAddTela.configure(font=("Roboto Black",24))
imgAddTela = customtkinter.CTkImage(light_image=Image.open("img/search.png"),size=(35,35))
buttonAddTela.configure(image=imgAddTela)
buttonAddTela.configure(border_spacing=14)
buttonAddTela.place(relx=0.5, rely=0.62, anchor=tkinter.CENTER)

buttonAddTela = customtkinter.CTkButton(master=frame,text="Añadir tela", command=addYardas,fg_color=("#0e1111"),hover_color="#000000")
buttonAddTela.configure(width=200,height=35)
buttonAddTela.configure(font=("Roboto Black",24))
imgAddTela = customtkinter.CTkImage(light_image=Image.open("img/plus.png"),size=(35,35))
buttonAddTela.configure(image=imgAddTela)
buttonAddTela.configure(border_spacing=14)
buttonAddTela.place(relx=0.5, rely=0.74, anchor=tkinter.CENTER)

buttonAddTela = customtkinter.CTkButton(master=frame,text="Quitar tela", command=lessYardas,fg_color=("#0e1111"),hover_color="#000000")
buttonAddTela.configure(width=200,height=35)
buttonAddTela.configure(font=("Roboto Black",24))
imgAddTela = customtkinter.CTkImage(light_image=Image.open("img/less.png"),size=(35,35))
buttonAddTela.configure(image=imgAddTela)
buttonAddTela.configure(border_spacing=14)
buttonAddTela.place(relx=0.5, rely=0.86, anchor=tkinter.CENTER)



"""lectorInventario()"""
##MAINLOOP

ventana.mainloop()