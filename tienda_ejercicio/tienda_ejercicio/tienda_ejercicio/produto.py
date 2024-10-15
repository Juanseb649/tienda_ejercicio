__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

import constantes
from tipos import tipo

class Producto:
    """----------------------------------------------------------------------------------------------
    # Constructor
    ----------------------------------------------------------------------------------------------"""
    def __init__(self,valorUnitario:float,subsidiado:bool,calidad):

        """----------------------------------------------------------------------------------------------
        # Atributos
        ----------------------------------------------------------------------------------------------"""

        self.valorUnitario = valorUnitario
        self.subsudiado= subsidiado
        self.calidad = calidad

    """----------------------------------------------------------------------------------------------
    # self.subsidiado = true
    # self.subsidiado = false
    ----------------------------------------------------------------------------------------------"""

    tipo = [tipo.drogueria]

    """----------------------------------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------------------------------"""

    def __init__(self,cantidad, cantidadMinima, nombre, tipo, valorUnitario:float,subsidiado:bool,calidad):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__valorUnitario = valorUnitario
        self.__subsidiado = subsidiado
        self.__calidad = calidad
        self.__cantidadBodega = cantidad
        self.__cantidadMinima = cantidadMinima
        self.__cantidadUnidadesVendidas = 0

    """----------------------------------------------------------------------------------------------
    # Metodo
    ----------------------------------------------------------------------------------------------"""

    __metohd__= "CalcularPrecioPapeleria"
    __parameter__= "ninguno"
    __returns__= "ninguna"
    __Description__ = "metodo que retorna el precio de un producto tipo papeleria"
    
    def calcularPrecioPapeleria(self):
        self.precio=self.valorUnitario + (self.valorUnitario * constantes.IVA_PAPELERIA)

    __metohd__= "Dar Nombre"
    __parameter__= "ninguno"
    __returns__= "nombre del producto"
    __Description__ = "metodo que retorna el nombre del producto "
    def darNombre(self):
        return self.darNombre

    __metohd__= "Dar tipo"
    __parameter__= "ninguno"
    __returns__= "tipo del producto"
    __Description__ = "metodo que retorna el tipo del producto "
    def darTipo(self):
        return self.darTipo

    __metohd__= "Dar valor unitario"
    __parameter__= "ninguno"
    __returns__= "valor unitario"
    __Description__ = "retorna el valor unitario "


    
    __metohd__= "Dar cantidad bodega"
    __parameter__= "ninguno"
    __returns__= "Cantidad Bodega"
    __Description__ = "retorna la cantidad minima en bodega "
    def daRCantidadMinima(self):
        return self.__cantidadMinima
    
    
    
    __metohd__= "DarPublicidad"
    __parameter__= "ninguno"
    __returns__= "Mensaje publicitario de un producto"
    __Description__ = "Metodo que brinda publicidad sobre un producto"
    def darpublicidad(self):
        #return "Compre el producto"+self.__nombre+ "por solo$ "+self.__valorUnitario
        return f"Compre el producto {self.darNombre()} por solo ${self.__valorUnirario()}

    __metohd__= ""Es Igual"
    __parameter__= "producto"
    __returns__= "True or False segun el resultado"
    __Description__ = "Metodo que permite comprar el producto con otro ingresado por el usuario"
    def esIgual(self,producto):
        return self.darNombre() is producto  