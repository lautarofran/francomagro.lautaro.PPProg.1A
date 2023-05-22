# Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena

def reemplazarCaracteres(cadena:str, caracter_uno:str, caracter_dos:str) -> int:
    contador_reemplazos = 0
    for caracter in cadena:
        if caracter == caracter_uno:
            caracter = caracter_dos
            contador_reemplazos += 1
    return contador_reemplazos

print(reemplazarCaracteres("Hola como estas espero que estes bien", "o", "a"))