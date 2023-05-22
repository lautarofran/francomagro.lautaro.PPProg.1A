import re

# Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicarAumento(precio:float) -> int:
    patron = r"^\d"
    retorno = 0.0
    if re.match(patron, precio):
        retorno = float(precio) * 1.05
        return round(retorno,2)
    else:
        return "Lo ingresado no es un numero"

print(aplicarAumento("4819.41"))