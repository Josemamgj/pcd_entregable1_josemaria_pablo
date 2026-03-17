from enum import Enum
from abc import ABCMeta, abstractmethod

class Lugar(Enum):
    ENDOR = 1
    CUMULO = 2
    NEBULOSA = 3

class Clase(Enum):
    EJECUTOR=1
    ECLIPSE=2
    SOBERANO = 3

class Repuesto:
    def __init__(self, nombre, proveedor, cantidad, precio):
        self.nombre = nombre
        self.proveedor =proveedor
        self.__cantidad = cantidad
        self.precio =precio

class Almacen:
    def __init__(self,nombre,ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.repuestos_dis = []

class Unidad_combate(metaclass = ABCMeta):
    def __init__(self, id_combate, clave):
        self.id_combate = id_combate
        self.clave = clave

class Nave(Unidad_combate):
    def __init__(self,id_combate,clave,nombre):
        super().__init__(id_combate,clave)
        self.nombre=nombre
        self.repuestos = []

    def instalar_repuesto(self,nombre_pieza):
        self.repuestos.append(nombre_pieza)

class Estacion_espacial(Nave):
    def __init__(self, id_combate, clave, nombre,tripulacion,pasaje,ubicacion):
        super().__init__(id_combate, clave, nombre)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = ubicacion

class Nave_estelar(Nave):
    def __init__(self, id_combate, clave, nombre, tripulacion, pasaje, clase_nave):
        super().__init__(id_combate, clave, nombre)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self-clase = clase_nave

class Caza_estelar(Nave):
    def __init__(self, id_combate, clave, nombre, dotacion):
        super().__init__(id_combate, clave, nombre)
        self.dotacion = dotacion

