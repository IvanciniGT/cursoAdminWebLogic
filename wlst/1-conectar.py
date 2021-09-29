# Función propia de WLST
# Sirve para conectar con un servidor
# connect( usuario, contraseña, t3://servidor:puerto ) 

def entrada_dato_obligatorio(mensaje):

    dato = ""
    intentos = 0
    
    while dato == "" :
        # Solicitar por consola al usuario: nombre_usuario
        dato=input(mensaje)
        # Que pasa si al usuario de le ha ido la chola.... y pulso ENTER sin meter ningún texto
        if dato == "" :
            #intentos = intentos + 1
            intentos += 1
            if intentos == 3:
                print("Eres un cafre... intentalo de nuevo después de un par de cafés...")
                return 
            else:
                print("No has escrito un valor válido. Intentalo de nuevo.")
    
    return dato
            
#funcion conectar con un servidor
def superconnect():
    
    nombre_usuario  = entrada_dato_obligatorio("Nombre del usuario administrador de WL: ")
    password        = entrada_dato_obligatorio("Contraseña del usuario administrador de WL: ")
    protocolo       = entrada_dato_obligatorio("Protocolo del servidor de WL: ")
    servidor        = entrada_dato_obligatorio("IP del servidor de WL: ")
    puerto          = entrada_dato_obligatorio("Puerto del servidor de WL: ")
    
    # Después hace la conexión
    print()
    print("Me voy a conectar con el usuario: "+ nombre_usuario)
    print("                     al servidor: "+ servidor)
    print("                    en el puerto: "+ puerto)
    print("                   con protocolo: "+ protocolo)
    print()
    print("Estableciendo conexión...")
    
superconnect()    