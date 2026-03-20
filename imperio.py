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

class MiImperio:
    def __init__(self,nombre):
        self.nombre = nombre
        self.__almacenes = []
        self.__naves = []

    def registrar_almacen(self,almacen):
        self.__almacenes.append(almacen)

    def registrar_nave(self,nave):
        self.__naves.append(nave)

    #METODOS DEL COMANDANTE
    def consultar_repuestos(self, nombre_pieza):
        resultados = []
        for almacen in self.__almacenes:
            pieza_encontrada = almacenes.buscar_pieza(nombre_pieza)
            if pieza_encontrada is not None:
                resultados.append((almacen.nombre, pieza_encontrada))
        
        return resultados
    
    def adquirir_repuesto(self,nave,repuesto,cantidad):
        try:
            repuesto.usar_stock(cantidad)
            for _ in range(cantidad):
                nave.instalar_repuesto(repuesto.nombre)
            print(f"{cantidad} - {repuesto.nombre} instalados en {nave.nombre}")
        except StockInsuficienteError as e:
            print(f"operacion cancelada: {e}")

    #METODOS DEL OPERARIO
    def mantener_lista_repuestos(self, almacen, repuesto_nuevo):
        almacen.registrar_pieza_nueva(repuesto_nuevo)
        print(f"Nuevo repuesto registrado {repuesto_nuevo.nombre} en {almacen.nombre}")

    def atualizar_stocks(self,almacen,repuesto,cantidad_a_añadir):
        repuesto.añadir_stock(cantidad_a_añadir)
        print(f"stock de {repuesto.nombre} actualizado, ahora hay {repuesto.ver_cantidad()} unidades")

        