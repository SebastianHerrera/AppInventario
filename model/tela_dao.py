from .conexion_db import ConexionDB
from tkinter import messagebox

def CrearTabla():
    conexion = ConexionDB()
    sql = '''
    CREATE TABLE telas(
    estanteRepisa VARCHAR(100),
    codigo VARCHAR (100),
    nombre VARCHAR (100),
    tipo VARCHAR (100),
    precioYarda VARCHAR (100),
    precioVenta VARCHAR (100),
    stock FLOAT
    )
    '''
    conexion.cursor.execute(sql)
    conexion.cerrar()
    
class Tela:
    def __init__(self,estanteRepisa,codigo,nombre,tipo,precioYarda,precioVenta,stock):
        self.estanteRepisa = estanteRepisa
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.precioYarda = precioYarda
        self.precioVenta = precioVenta
        self.stock = stock
    def __str__(self):
        return f'Tela[{self.estanteRepisa},{self.codigo},{self.nombre},{self.tipo},{self.precioYarda},{self.precioVenta},{self.stock}]'

def guardar(tela):
    conexion = ConexionDB()
    sql = f"""INSERT INTO telas (estanteRepisa, codigo, nombre, tipo, precioYarda, precioVenta, stock)
    VALUES('{tela.estanteRepisa}','{tela.codigo}','{tela.nombre}','{tela.tipo}','{tela.precioYarda}','{tela.precioVenta}','{tela.stock}')
    """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        messagebox.showerror("Error","El nuevo objeto que intentaste guardar no es correcto.")