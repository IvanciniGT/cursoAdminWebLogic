# Comentarios en linea en python
123                 # Entero # Poner en la RAM 123          > BASURA
87.9                # Decimales                             > BASURA

True                # Valores lógicos                       > BASURA
False   

"Hola amigo"        # Textos                                > BASURA
'Hasta luego'

# En ocasiones usamos el texto multilinea como alternativa al comentario en bloque
"""                                                          > BASURA
Esto es un texto multilinea
Este texto puede ocupar varias lineas

Incluso dejar espacios en blanco entre medias
"""

numero=17
texto="Hola"
llueve=True

# Funcion # Metodo
print("Como tu tas?")
print(texto)

def saluda(nombre="Cristian"):
    print("Hola "+nombre)
    
saluda("Ivan")
saluda("Alicia")
saluda("Adrian")
saluda("Pau")
saluda()

def doblar(numero):
    print("Estoy calculando el doble del numero: "+ str(numero))
    return numero*2

numero_a_doblar=7
el_doble_del_numero=doblar(numero_a_doblar)
print(el_doble_del_numero)

# Operadores
    #   =              Asignar
    # Textos 
        # +            Concatenar textos
        # *            Replicar un texto
    # Numeros
        # +            Suma aritmetica
        # -
        # *
        # /
        # //           Division entera
        # %            Resto de la division entera
    # Relacionales
        # >
        # <
        # >=
        # <=
        # ==           Igual de comparacion
        # !=           Igual de comparacion
    # Operadores lógicos
        # and
        # or
        # not
    
print(7/3)              # 2.333333333 
print(7//3)             # 2
print(7%3)              # 1

print("WEBLOGIC"*3)

# Controlar el flujo de nuestro script
# En ocasiones quiero que se ejecute o no un trozo de codigo... en funcion de unas condiciones

edad=input("Dame tu edad: ")
if int(edad)>18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 70% python 
# colecciones: Lista, diccionario
# Bucles: for, while