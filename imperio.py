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

class StockInsuficienteError(Exception):
    pass

class ParametroInvalidoError(Exception):
    pass

class Repuesto:
    def __init__(self, nombre, proveedor, cantidad, precio):

        if cantidad < 0 or precio < 0:
            raise ParametroInvalidoError("El stock  y el precio tienen que ser positivos")

        self.nombre = nombre
        self.proveedor =proveedor
        self.__cantidad = cantidad
        self.precio =precio

    def usar_stock(self,cantidad_a_usar):
        if cantidad_a_usar <= 0:
            raise ParametroInvalidoError("La cantidad a usar debe tener valor")

        if cantidad_a_usar > self.__cantidad:
            raise StockInsuficienteError("No hay stock suficiente")
        self.__cantidad -= cantidad_a_usar

    def añadir_stock(self,cantidad_a_añadir):
        if cantidad_a_añadir <= 0:
            raise ParametroInvalidoError("La cantidad a añadir debe ser mayor a cero")

        self.__cantidad += cantidad_a_añadir

    def ver_cantidad(self):
        return self.__cantidad

class Almacen:
    def __init__(self,nombre,ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.repuestos_dis = []

    def buscar_pieza(self,nombre_buscado):
        for pieza in self.repuestos_dis:
            if pieza.nombre == nombre_buscado:
                return pieza
        return None
    
    def registrar_pieza_nueva(self,repuesto):
        if not isinstance(repuesto, Repuesto):
            raise ParametroInvalidoError("Se deben registrar objetos que sean Repuestos")
        self.repuestos_dis.append(repuesto)

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
        self.clase = clase_nave

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
        if not isinstance(almacen, Almacen):
            raise ParametroInvalidoError("El almacen no existe")
        self.__almacenes.append(almacen)

    def registrar_nave(self,nave):
        if not isinstance(nave, Nave):
            raise ParametroInvalidoError("La nave no existe")
        self.__naves.append(nave)

    #METODOS DEL COMANDANTE
    def consultar_repuestos(self, nombre_pieza):
        resultados = []
        for almacen in self.__almacenes:
            pieza_encontrada = almacen.buscar_pieza(nombre_pieza)
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
        except ParametroInvalidoError as e:
            print(f"operación cancelada: {e} ")

    #METODOS DEL OPERARIO
    def mantener_lista_repuestos(self, almacen, repuesto_nuevo):
        try: 
            almacen.registrar_pieza_nueva(repuesto_nuevo)
            print(f"Nuevo repuesto registrado {repuesto_nuevo.nombre} en {almacen.nombre}")
        except ParametroInvalidoError as e:
            print(f"error al registrar: {e}")

    def atualizar_stocks(self,almacen,repuesto,cantidad_a_añadir):
        try:
            repuesto.añadir_stock(cantidad_a_añadir)
            print(f"stock de {repuesto.nombre} actualizado, ahora hay {repuesto.ver_cantidad()} unidades")
        except ParametroInvalidoError as e:
            print(f"error de inventario: {e}")


#PRUEBAS Y TEST
if __name__ == "__main__":
    sistema = MiImperio("Imperio General")

    almacen_endor = Almacen("Almacen principal", Lugar.ENDOR)
    sistema.registrar_almacen(almacen_endor)

    motor = Repuesto("Motor 1", "Audi", 5, 1500)
    pantalla = Repuesto("Pantalla 1", "lg", 3, 500)

    sistema.mantener_lista_repuestos(almacen_endor, motor)
    sistema.mantener_lista_repuestos(almacen_endor, pantalla)

    caza = Caza_estelar("Nave de ataque", 1111, "nave de darth vader", 1)
    sistema.registrar_nave(caza)

    sistema.adquirir_repuesto(caza,motor,2)
    print(f"Catalogo de la nave ahora: {caza.nombre}: {caza.repuestos}")

    #PROBAMOS A COMPRAR MAS DE LO QUE HAY
    sistema.adquirir_repuesto(caza,pantalla, 10)
    