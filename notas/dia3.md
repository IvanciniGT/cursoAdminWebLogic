Poll de ejecutores (threads) < Gestionado por Weblogic

- Cuando llega una petición entra en la COLA de peticiones.
- Del poll de ejecutores, en cuanto hay uno libre, se elige un ejecutor para procesar la siguiente petición que hay en la
cola de peticiones

Podemos tener más peticiones que ejecutores? SI, pero se van quedando en la cola

Tamaño máximo del poll, depende de:
- Recursos de HW
- Naturaleza de la app: Se usan los recursos de una forma u otra

App cuyas peticiones tardan en procesarse 1 seg... de pura CPU.
¿Cuantos ejecutores puedo tener? Tantos como cores.
Cualquier ejecutor adicional no mejora rendimiento, si acaso lo empeora.

El poll de ejecutores puede ser un cuello de botella si?
- Si tengo más peticiones que ejecutores ... y tengo capacidad para más ejecutores.

Si tengo más peticiones que ejecutores ... pero no tengo capacidad para más ejecutores?
Aquí el poll de ejecutores no es un cuello de botella. Quien es el cuello de botella? El HW, recursos
Que hago?
- Más recursos en mi server
- Nuevo server

Poll de conexiones a BBDD
Necesito tantas conexiones como ejecutores? NO
De cuál más? Más ejecutores, muchos más.
RATIO que debemos calcular y mantener en la configuración

Quién limita en el número de conexiones a BBDD que puedo abrir? 
Recursos BBDD, Admin BBDD

Datasources:
    Configuración de un datasource:
        - Servidor
        - Puerto
        - Usuario
        - Contraseña
        - BBDD
        - Driver   < Programa que es el que al final se comunica con la BBDD
                     Programa JAVA. Viene dentro de una libreria .jar
                     Dentro del .jar (zip) habrá una clase .class con el driver
                     
                     De donde lo saco:
                        - WEBLOGIC trae muchos
                        - Si no trae el que necesito, pues que me lo de ADMIN BBDD
                            o lo descargo y tendré que instalarlo
                            
Dominio de weblogic:
    Carpeta que existe dentro de la ruta: WEBLOGIC/user_projects/domains/
    Subcarpetas:
        bin
        config
        servers       < logs
        nodemanager   < Solo si montabamos nodemanager por dominio

WLST
    - Consola interactiva de linea de comandos
    - Script < Jython
    
Jython?

Python es una sintaxis de un lenguaje de programación. > Interpretado en tiempo de ejecución.
Interprete de Python < cython
                       wlst    < JAVA    < python
WLST está instalado en oracle_common/common/bin/wlst.sh

Software:
    Demonios
    Servicios
    Aplciaciones
    Scripts      <<<<<<
    
    
    
Puerto de administración de WL
    En que servidor de WL está instalado la consola de administración?
        AdminServer:7001   http
        AdminServer:7002   https
    
    PUERTO DE ADMINISTRACION: 9002      <<<<<<<<
    Ese puerto se abría donde ? En todos los servidores del dominio y 
    desde ahí se reenvían las peticiones al AdminServer


/base_domain/

serverConfig/


pwd()
ls()
cd(ruta)

dr--
^      Tipo: directorio | propiedad
 Read
  Write
   Execution



edit()
startEdit()


Cambios

save()
activate()

cd("/")
cmo.getServers()[0].getListenPort()

for servidor in cmo.getServers():
    print(servidor.getName())
    

for color in colores:
    print(color)
    
    
    
serverConfig            < Configuracion del servidor al que conecté (connect)
serverRuntime           < Estado de ejecución del servidor al que conecté (connect)

Solo invocables cuando estoy conectado al ADMINSERVER
VVVVVVVVVVVVV
domainConfig            < Configuracion de cualquier servidor del dominio
domainRuntime           < Estado de ejecucion de cualquier servidor del dominio
En el adminserver, los arboles Server y Domain son equivalentes. Da igual entrar en uno o en otro

-----------------
Script:
Mire el número máximo de ejecutores en un servidor CONCRETO     <  Config
El número actual de ejecutores                                  <  Runtime


conectados al AdminServer
serverRuntime() > Admin
domainRuntime()/ServerRuntimes/AdminServer
                              /Servidor1