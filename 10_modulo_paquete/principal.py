import calculadora
from utilidades import strings, numeros

a = 10
b = 5
print("Suma:", calculadora.sumar(a,b))
print("Resta:", calculadora.restar(a,b))
print("Multiplicacion:", calculadora.multiplicar(a,b))
print("Division:", calculadora.dividir(a,b))

cadena = "Hola"
numero = 13
print("Cadena invertida:",strings.invertir_cadena(cadena))
es_par = numeros.es_par(numero)
# print("Es par?",numeros.es_par(numero))
if es_par:
    print("El numero indicado es par")
else:
    print("El numero indicado es impar")