"""
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Crie uma função que retorne dois valores em uma tupla contendo a quantidade de
latas de tinta a serem compradas e o preço total a partir do tamanho de
uma parede(em m²).
"""

import math


def calculate_ink_cost(size):

    GALLON_YIELD = 54
    GALLON_PRICE = 80.00
    quantity_gallon = math.ceil(size / GALLON_YIELD)
    total_price = quantity_gallon * GALLON_PRICE
    result = (quantity_gallon, total_price)
    return result


assert calculate_ink_cost(54) == (1, 80.0)
