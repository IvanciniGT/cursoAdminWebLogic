from java.io import FileInputStream
nombre_usuario=""
contrasena=""


for indice in range(1,len(sys.argv)):
    if sys.argv[indice] == "--user-name" or sys.argv[indice] == "-u":
        nombre_usuario=sys.argv[indice+1]
    elif sys.argv[indice] == "--password" or sys.argv[indice] == "-p":
        contrasena=sys.argv[indice+1]
    elif sys.argv[indice] == "--connection-properties" or sys.argv[indice] == "-c":
        ruta_fichero=sys.argv[indice+1]
        
        buffer_lectura_al_fichero=FileInputStream( ruta_fichero )
        propiedades_conexion=Properties()
        propiedades_conexion.load(buffer_lectura_al_fichero)
        
        if propiedades_conexion.get("user-name") is not None:
            nombre_usuario=propiedades_conexion.get("user-name") 
        if propiedades_conexion.get("password") is not None:
            contrasena=propiedades_conexion.get("password") 
            

print("Usuario: " + nombre_usuario)
print("Contraseña: " + contrasena)


#./wlst.sh controlarMemoriaServer.py usuario contraseña protocolo servidor puerto
#./wlst.sh controlarMemoriaServer.py -u admin -p welcome1
#./wlst.sh controlarMemoriaServer.py --user-name admin --password welcome1
#                    0                    1        2       3          4