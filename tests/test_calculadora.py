
from calculadora import sumar, restar, multiplicar, dividir


def test_sumar():
    assert sumar(5, 3) == 8
    assert sumar(-2, 2) == 0


def test_restar():
    assert restar(10, 4) == 6
    assert restar(5, 8) == -3


def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(-2, 5) == -10


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3


def test_dividir_entre_cero():
    assert dividir(10, 0) == "Error: no se puede dividir entre cero"