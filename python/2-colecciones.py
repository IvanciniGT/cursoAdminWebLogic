# Una coleccion en python, es un conjunto de valores agrupados

# tuplas: Conjunto ordenado e inalterable de valores
colores=("rojo", "verde", "azul", "blanco", "negro", "amarillo")
# posiciones 0      1       2         3        4          5

print( len(colores) )       # Cuantos colores tengo
print( colores[2] )         # Dame el tercer color
print( colores[2:4] )       # Dame los colores desde el que etá en la posicion 2 incluido 
                            # hasta el de la posicion 4 no incluido
                            
print( colores[-1] )        # Ultimo 
print( colores[-3] )        # Antepenultimo, blanco
print( colores[-3:] )       # Desde el Antepenultimo, todos

# Una tupla puede ser recorrida por un bucle for
for color in colores:
    print(color)

# Quiero recorrer todos los valores entre el 1 y el 100
for numero in range(1,101):
    print(numero)
    
texto="Hola compañeros"     # Tupla de caracteres
print(  len(texto)  )
print(  texto[3]  )
print(  texto[-3]  )
print(  texto[-10:]  )
print(  texto[:4]  )

for caracter in texto:
    print(caracter)


# lista: Conjunto ordenado y editable de valores
# Posicion 0        1        2        3         4        5
colores=["rojo", "verde", "azul", "blanco", "negro", "amarillo"]
print( colores[2] )
colores[2]="morado"
print( colores[2] )

# Diccionario: Otra coleccion de valores... 
    # en ella, cada valor, va identificado por una clave.... y los valores se guardan desordenados
    
# fruta   fresa     kiwi    arandano  piña     mora   platano
colores={"fresa": "rojo", "kiwi": "verde", "arandano": "azul", 
          "piña": "blanco", "mora": "negro", "platano": "amarillo"}

print(colores["platano"])

colores["platano"]="negro"
print(colores["platano"])
