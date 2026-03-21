import pytest 
from imperio import Repuesto, StockInsuficienteError, Almacen, MiImperio, Caza_estelar, ParametroInvalidoError

def test_usar_stock_bien():
    motor = Repuesto("Motor", "Lexus", 10, 100)

    motor.usar_stock(2)
    assert motor.ver_cantidad() == 8

    motor.añadir_stock(5)
    assert motor.ver_cantidad() == 13

def test_registrar_nave():
    sistema = MiImperio("Base general")
    caza = Caza_estelar("10", 2222, "caza de asalto", 1)
    sistema.registrar_nave(caza)


def test_añadir_stock():
    pantalla = Repuesto("Pantalla", "dell", 2, 40)
    with pytest.raises(StockInsuficienteError):
        pantalla.usar_stock(5)

def test_excepcion_stock_neg():
    with pytest.raises(ParametroInvalidoError):
        Repuesto("pieza rota", "111", -5, 100)

def test_excepcion_usar_neg():
    motor = Repuesto("Motor", "mercedes", 10, 1000)
    with pytest.raises(ParametroInvalidoError):
        motor.usar_stock(-2)

def test_excepcion_registrar_nave():
    sistema= MiImperio("Base endor")
    nave_error = "PONEMOS TEXTO PARA REGISTRAR ALGO MAL"

    with pytest.raises(ParametroInvalidoError):
        sistema.registrar_nave(nave_error)