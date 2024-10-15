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
    def darCantidadMinima(self):
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
    
    __metohd__= "Vender "
    __parameter__= "Cantidad de producto a vender"
    __returns__= "Ninguno"
    __Description__ = "Metodo que permite vender"
    def vender (self,CProducto):
        if CProducto > self.darCantidadBodega():
            self.__cantidadUnidadesVendidas += self.darCabtidadBodega()
            self.__cantidadBodega= 0
        else:
            self.__cantidadUnidadesVendidas += self.cProducto
            self.__cantidadBodega -= self.cProducto

    __metohd__= "VenderdeTodo "
    __parameter__= "Ninguno"
    __returns__= "Ninguno"
    __Description__ = "Metodo que Calcula la cantidad disponible del producto 1 y vende esa cantidad de los demas"
    def VenderdeTodo (self):
        cuanto = self.__producto1.darCantidadBodega()
        self.producto2.vender(cuanto)
        self.producto3.vender(cuanto)
        self.producto4.vender(cuanto)
    
    __metohd__= "AgregarNuevaUnidadBodega "
    __parameter__= "Ninguno"
    __returns__= "Ninguno"
    __Description__ = "Metodo que permite agregar un producto en bodega"
    #self.__cantidadBodega =self.__cantidadBodega + 1

    __metohd__= "Pedir"
    __parameter__= "Cantidad"
    __returns__= "Ninguno"
    __Description__ = "Metodo que permite pedir unidades para la bodega"
    def pedir(self,cantidad):
        self.__cantidadBodega *= cantidad
        self.__cantidadBodega =self.__cantidadBodega+cantidad 
        def haySuficiete (self,Cproducto):
            suficiente = False
            if (Cproducto<= self.__darCantidadBodega()):
                suficiente = True
            else:
                suficiente = False
                return suficiente
            
            return Cproducto <= self.__darCantidadBodega()
        
    __metohd__= "dar precio Papeleria"
    __parameter__= "conIva"
    __returns__= "Precio final"
    __Description__ = "metodo que calcula el precio de un producto con IVA o sin IVA "
    def darPrecioPapeleria (self, conIva):
        preciofinal= self.darValorUnitario()
        if(conIva):
            precioFinal= precioFinal * (1+self.IVAPAPELERIA)
            return precioFinal
    
        __metohd__= "AjustarPrecio"
    __parameter__= "Ninguno"
    __returns__= "Ninguna"
    __Description__ = "metodo que permite ajustar el precio si no se han vendido 100 unidades"
    def AjustarPrecio (self):
        if (self.darCantidadUnidadesVendidas() < 100):
            self.__valorUnitario = self.__valorUnitario*80/100
        else:
            self.valorUnitario = self.__valorUnitario = self.__ValorUnitario *1.1

            __metohd__= "DarIva"
    __parameter__= "Ninguno"
    __returns__= "Iva"
    __Description__ = "metodo que permite retornar el IVA segun su tipo"

    #forma 
    #if self.darTipo()==tipo.PAPELERIA:
        #iva= self.IVAPAPELERA
    #elif self.darTipo()==tipo.DROGUERIA:
        #iva= self.IVADROGUERIA
    #else:
        #iva= self.IVADROGUERIA
    
    
    __method__ = "DarIVA"
    __parameter__ = "Ninguno"
    __returns__ = "valor del iva en 0.0"
    __Description__ = "metodo que retorna el iva del producto en base a su tipo"
    def DarIVA(self):
        if(self.DarTipo == 1):
            return 0.16
        elif(self.DarTipo == 2):
            return 0.4
        elif(self.DarTipo == 3):
            return 0.12
    
        __method__ = "Abastecer"
    __parameter__ = "cantidad a abastecer"
    __returns__ = "Ninguno"
    __Description__ = "Agrega el numero de unidades a abastecer al producto"
    def Abastecer(self, pCantidad):
        self.__cantidadBodega += pCantidad
        
    def ejercicio(self):
        self.__nombre = 'telefono'
        
    def subirValorUnitario(self):
        if self.__valorUnitario < 1000:
            return self.__valorUnitario + (self.__valorUnitario*0.001)
        elif self.__valorUnitario >= 1000 and self.__valorUnitario <= 5000:
            return self.__valorUnitario + (self.__valorUnitario*0.002)
        elif self.__valorUnitario > 5000:
            return self.__valorUnitario + (self.__valorUnitario*0.003)
        
    def hacerPedido(self,cantidad):
        if self.__cantidadMinima > self.__cantidadBodega:
            self.__cantidadBodega += cantidad

    def ejercicio(self):
        self.__dineroCaja += (self.producto1.DarCantidadUnidadesVendidas() * self.producto1.DarValorUnitario()) + (self.producto1.DarIVA() * self.producto1.DarValorUnitario())
        self.__dineroCaja += (self.producto2.DarCantidadUnidadesVendidas() * self.producto2.DarValorUnitario()) + (self.producto2.DarIVA() * self.producto2.DarValorUnitario())
        self.__dineroCaja += (self.producto3.DarCantidadUnidadesVendidas() * self.producto3.DarValorUnitario()) + (self.producto3.DarIVA() * self.producto3.DarValorUnitario())
        self.__dineroCaja += (self.producto4.DarCantidadUnidadesVendidas() * self.producto4.DarValorUnitario()) + (self.producto4.DarIVA() * self.producto4.DarValorUnitario())
        
    def venderProduto(self, pNombreProducto, pCantidad:int):
        if pNombreProducto == self.producto1.DarNombre():
            cantidadPrevia = self.producto1.DarCantidadBodega()
            self.producto1.Vender(pCantidad)
            cantidadPosterior = self.producto1.DarCantidadBodega()
            return cantidadPrevia - cantidadPosterior
        elif pNombreProducto == self.producto2.DarNombre():
            cantidadPrevia = self.producto2.DarCantidadBodega()
            self.producto2.Vender(pCantidad)
            cantidadPosterior = self.producto2.DarCantidadBodega()
            return cantidadPrevia - cantidadPosterior
        elif pNombreProducto == self.producto3.DarNombre():
            cantidadPrevia = self.producto3.DarCantidadBodega()
            self.producto3.Vender(pCantidad)
            cantidadPosterior = self.producto3.DarCantidadBodega()
            return cantidadPrevia - cantidadPosterior
        elif pNombreProducto == self.producto4.DarNombre():
            cantidadPrevia = self.producto4.DarCantidadBodega()
            self.producto4.Vender(pCantidad)
            cantidadPosterior = self.producto4.DarCantidadBodega()
            return cantidadPrevia - cantidadPosterior
        
    def cuantosPapeleria(self):
        cantidadUnidadesVendidasPapeleria = 0
        if self.producto1.DarTipo() == tipo.Papeleria:
            cantidadUnidadesVendidasPapeleria += self.producto1.DarCantidadUnidadesVendidas()
        elif self.producto2.DarTipo() == tipo.Papeleria:
            cantidadUnidadesVendidasPapeleria += self.producto2.DarCantidadUnidadesVendidas()
        elif self.producto3.DarTipo() == tipo.Papeleria:
            cantidadUnidadesVendidasPapeleria += self.producto3.DarCantidadUnidadesVendidas()
        elif self.producto4.DarTipo() == tipo.Papeleria:
            cantidadUnidadesVendidasPapeleria += self.producto4.DarCantidadUnidadesVendidas()

