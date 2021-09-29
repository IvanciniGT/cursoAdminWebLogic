contenedores
Contenedor:             Entorno aislado donde ejecutar procesos dentro de un sistema operativo Linux
Ventajas:               AISLADO: 
                            Cada proceso corre en un entorno seguro, donde no afecta a otros procesos
                                                                     donde otros procesos no le afecta a él
                                                                     con su propio filesystem que nadie puede tocarle
                        ESTANDARIZAR DISTRIBUICIONES/INSTALACION DE SOFTWARE
                        ESTANDARIZACION > Herramientas que faciliten (al extremo) la AUTOMATIZACION
Imágen de contenedor:   Un fichero comprimido que contenía un programa ya instalado, configurable pero ya instalado
                        Uno o muchos programas ya instalados
                        Y con las dependencias necesarias para poder ejecutarse

---------------------------------------
jee - Estandar Jakarta Enterprise Edition
Cómo montar aplicaciones WEB de java
    JDBC
    JMS
    JNDI
Disponer de un tipo de software donde ejecutar las aplicaciones WEB de JAVA:
    Servidor de aplicaciones:
        De clase Web         < Tomcat
        De clase Empresarial < Weblogic
Los ficheros HTML se genera a través de 3 formas diferentes:
    - servlet   .class
    - jsps      .jsp
    - jfcs      .jfc
---------------------------------------
WEB  -  Servicio ofrecido a través de Internet
Se caracteriza por el uso de:
    - Basado en una arquitectura cliente / servidor
    - Cliente: Navegador de internet
    - Protocolo de comunicación: http(s)
        Petición: URL (método http)
        Respuesta     (código de estado)
            2XX OK
            3XX Redirect    
            4XX Error de cliente
            5XX Error de servidor
    - Formato de intercambio de información: html
---------------------------------------
Aplicación web vs página WEB
- Sitios web montados a través de páginas web estáticas (desarrolladores web que creaban ficheros HTML)
- Aplicación web. Páginas web dinámicas, generadas por programas
---------------------------------------
java
    Es un lenguaje compilado e interpretado
        .java -> (javac) -> .class (bytecode)
    La interpretación del código compilado de java (bytecode) la realiza la "máquina virtual" de java
    .class << En general bastantes ficheros. Cómo se distribuyen? Comprimidos en ZIP
        .jar    >>>"Librerias"<<< o aplicaciones autoejecutables
        .war    Aplicación WEB:
                    Clases
                    Recursos: Imágenes, HTML, CSS
                    Librerias
                    Configuraciones
        -------------VVVVVV--------------------  Solamente en serv de apps de clase empresarial
        .ear    Grupo de apps web y ejbs que trabajan conjuntamente
    Quién está detrás de Java < Oracle (Sun microsystems)
        Sun microsystems:
            Arquitectura de microprocesador: sparc
            Solaris UNIX®
            JAVA    <<<<<< Le interesaba un cagao!
    Nichos:
        Web                     Backend
        Android (Linux)         Google 

    Distribuciones de JAVA
        JRuntimeEdition
            java < máquina virtual que puedo ejecutar
        JDevelopmentKit
            java
            javac < Que permite compilar... Esto es lo que usan los desarrolladores

---------------------------------------
Weblogic
Servidor de apps de clase empresarial.
Quien lo desarrolla? Oracle (Bea systems)

Se ejecuta dentro de una máquina virtual JAVA > Necesito tener instalado: JDK o JRE?
    A priori me parecería pensar que con JRE me sirve... pero no es así.
    Necesitamos JDK, ya que SI SE NECESITA javac.
    Los ficheros .jsp .jfc se distribuyen sin compilar por los desarrolladores (según el estandar JEE)
    Es responsabilidad del Serv. de apps su compilación.

Entornos de producción:
    - Alta disponibilidad       |
    - Escalabilidad             |       Implementación/Uso de clusters
    
Cuando arrancamos un weblogic, ese servidor(instancia) va a llevar asociado (va a pertener a) un dominio

DOMINIO:  Agrupación lógica de un Conjunto de recursos que son compartidos entre unas instancias de Weblogic
Machine:  Máquina física o virtual donde tenemos en ejecución: NodeManager
NodeManager: Una aplicación que viene dentro de la suite Weblogic, que permite:
    - Arrancar servidores remotamente desde consola (UI) / WLST
    - Monitorizar instancias / reiniciarlas si es necesario
    - Distribuir configuraciones
WLST: Linea de comandos de weblogic.... Interprete que permite ejecutar comandos/scripts contra un server weblogic / nodemanager
        connect  < conectar contra un servidor de weblogic
        nmconnect < conectar con un nodemanager
Servidor/Instancia (Server): Una ejecución de WEBLOGIC con una determinada configuración
De una instalación de weblogic, cuantos servers puedo arrancar? Los que quiera/pueda
Clusters: Grupo de servers que tienen la misma "configuración" y comparten recursos
-------------------------------------------------
Jenkins         <<<<<<       Hudson
MariaDB         <<<<<<       MySQL
LibreOffice     <<<<<<       OpenOffice (Sun microsystems   ....    StarOffice)

--------------------------------------------------
NodeManager:
Es necesario disponier de NodeManagers en las máquinas que forman mi instalación de Weblogic?
NO
Y si no lo tengo?
Los arranques de servidores los tengo que hacer mediante la ejecución del comando startManagedWebLogic.sh / startWebLogic.sh


Que pasa si en un momento dado se cae en administrador (el server donde se ejecuta la consola... nuestro AdminServer)
- No puedo acceder a la consola
- Sigue funcionando todo? El resto de servers? SI
-   Pero no puedo controlarlas/configurarlas


Tipo de objeto que existe en JAVA muy especial,
que independiemente de su naturaleza conozco como comunicarme con él para interrogarle: BeaNS
--------------------------------------------------

Transacción:
    Conjunto de operaciones/cambios que al final puedo:
        - Aplicar al mismo tiempo
            - Tengo garantizado que: 
                - O se aplican todos
                - O ninguno, si alguno da un problema
        - Descartar
        
MiDOMINIO               Puertos:   http    https                Puerto de administración: 9002
    Host 1
        WLS1                        7001     7002               9002
        WLS2                        7003     7004               9003    >    Consola de administración
    Host 2
        AdminServer                 7001     7002               9002
            console                 XXXX     XXXX
        WLS3                        7003     7004               9003
        
Instalacion host
    Weblogic
        Generando un dominio
            Servidores
            Clusters
            VirtualServers
            Nodemanagers
            
    pack.sh   -> ZIP .jar
Instalacion host2
    Weblogic
    unpack.sh ZIP .jar



Instalacion Weblogic
    user_projects
        domains
            dominio1
            dominio2
        nodemanager

En la carpeta servers:
    Veo dentro de cada host los servidores que se han ejecutado o se están ejecutando dentro de ese host
    
    
----------------------------------------
                DOMINIO1
host 1 - WL   
    systemd - nodemanager, startWebLogic.sh

    AdminServer   <<<< Arranque con conf estandar           proceso SO: JVM             startWebLogic.sh
    Server1                                                 proceso SO: JVM
host 2 - WL
    systemd - nodemanager

    Server2                                                 proceso SO: JVM
host 3 - WL
    systemd - nodemanager

    Server3                                                 proceso SO: JVM
    
----------------------------------------
THREADS - HILOS

HILO?
Lo que ejecuta código dentro de un SO
¿Cuantos hilos se pueden ejecutar "simultaneamente" en un ordenador? Tantos hilos como cores.
SO de uso compartido de CPU

2 cores
10 hilos "Simultaneamente" (uso compartido)

PROCESO SO?
    Programa en estado compatible con ejecución
    Copia del programa en memoria
    Reservar ciertas zonas en RAM 
        HEAP COMUN
    ThreadStack
        Variables -> HEAP

Un proceso siempre tiene asociado al menos 1 hilo (EJECUTOR)


Cliente1    >>
Cliente2    >>
Cliente3    >>          Serv Weblogic           >>>>> app1
...                                             >>>>> app2
Cliente n   >>
                        ^^^^ HILOS (JVM)
                        100 hilos
101 peticiones 
                >>>>>
            COLA PETICIONES
                    >>>> EJECUCION DE LAS PETICIONES
                            (hilos limitan : Cuantas peticiones simultaneas voy a procesar)
                            
        ¿ De que depende el número de hilos que voy a configurar?
            - Carga que espero en mi servidor (RUINA !!!!!!) NADA ... no me vale.. ni un poquito
            - Recursos que tengo (TOTAL)
            - Naturaleza de la app . Recursos que usa la app en sus peticiones
            
        Rango de hilos (ejecutores)
            20 - 100 ejecutores    
        
            POLL de ejecutores: Entre n y m


10000 peticiones <--- 10000 hilos NI DE COÑA... porque recursos recursos <<<<< ESCALABILIDAD NUMERO DE SERVIDORES 

Servidor   RECURSOS
    App1   <<<<<<<<<      Cuantas peticiones aguanta      1000 peticiones
    
Espero picos de 3000 peticiones > 3 servidores 

Servidores desde una plantilla
Clusters dinamicos


COLA > TIMEOUT

    100 peticiones / min    DEVUELVO 
    101
    102 explota CPU 100% swap
    hdd 
    150 peticiones    PUF !!!!! 0 peticiones 
    
COLA, weblogic dispone de ella en cualquier caso.
    
COLA? Quiero gente en la cola? 
    SI QUIERO gente en la COLA
    SI NO TENGO gente en la COLA? 
    
No quiero que la gente espere demaiado en la cola <<<


Carrefour, Primark, Mediamark  <<<<<< Cola unica
    Cajas abiertas
            Si que estoy teniendo clientes.... tiro billetes 
            No tengo clientes.... ruina !
            
    25% 
    
    
    4 servidores 100%       ----       25% <<<<< 
    3 de los servidores aquello siga funcionando
    
    

Mercadona, cada caja tiene su cola



Cuanto tarda en hacerse una peticion 100 ms CPU, 100Kbs de RAM , Tiempo de uso del buffer del hdd  <<< App


20 peticiones - 80 peticiones
Biblioteca / Archivo 100m2 / 25 m2
                                30 personas 
                                120 



20 ejecutores (maximo 100)

25 peticiones ? WL? 
    Encola 5 o abre 5 ejecutores   
    ^^^^^^^^   no abre 5 ejecutores... aunque quede hueco para abrirlos
    
    por qué? Abrir un hilo(ejecutor) conlleva un tiempo.
    
    Solamente cuando hay una carga sostenida en el tiempo, es cuando WL va a ir abriendo nuevos ejecutores
    
    
El poll de ejecutores es un conjunto de ejecutores ya arrancados y en espera de atender
                        
Cl1                            POLL DE EJECUTORES
Cl2     >>>>> COLA >>>>            Ej1                  S                   BUG     
Cl3                                Ej2                      <<<
                                   Ej3                  S
                                   Ej..                     <<<
                                   Ej 20                S
                                   
Stuck threads: Cuando un hilo lleva mucho tiempo con la misma ejecución (con la misma petición) 10 min.
Si una peticion pasa los 10 minutos de ejecución.
    
    
Un hilo atiende solo una peticion a la vez. A TOPE 
Una peticion es atenda por un solo ejecutor WL. 


Un hilo en uso desde hace 5 minutos puede ser que esté consumiendo 0% de recursos?
Sin problema... estando en espera? Totalmente normal ---> Lanzado una query a BBDD 

20 hilos maximos en el poll     18 están stuck
Cuantas peticiones puedo atender? de 2 en 2

                                                                        WL                                   VVV
Clientes > peticiones > Cola > Poll de ejecutores   > Query a BBDD >   COLA >  Poll de conexiones a BBDD >>> BBDD
                                                    > Envio de un mensaje
                                                    > Envio de emails
                                                    > LDAP
                                                    > LLamar a un microservicio
                                                    
Abrir un ejecutor que implica? a nivel de SO? Es una nueva entrada en el ThreadStack del proceso... y algo de ram que reservo para el hilo
            HILO
            
            
Abrir un proceso a nivel de SO que implica?
2 veces que pongo el programa en RAM


Qué pasa cuando abris una conexión a BBDD??
A qué da lugar aquello en el WL? La conexión abre un hilo
A qué da lugar una conexión en el host de la BBDD? Se abre también un hilo en el host de la BBDD?
                                                            un proceso !
                                                            
BBDD Oracle < conexión <<<<<< Insert 500 filas, borrar 2000 filas, crear una tabla y quiero queries? MEMORIA CONEXION
        COMMIT;
    POLL DE CONEXIONES A BBDD
EJECUTORES                 C1
EJ1                        C2
EJ2            COLA        C3
...                        ...
EJM                        Cn


COLA EJECUTORES      >>>>> COLA CONEXIONES A BBDD   
5     >>>>>>>>>>>>>>>>>>>>        1
100 ejecutores WL                 Si tengo un poll de 20    BIEN o MAL? npi
                                                                        Depende del uso de BBDD por parte de cada ejecutor:
                                                                            Naturaleza de la app.... Desarrollador? NPI
Tiempo medio de peticion            Tiempo medio de conexión
                                    Queries (usuarios)
                                    Conf de BBDD y sus recursos
                                    Diseño BBDD
                                    
200 ms               > 100% >>>>    50ms

% RATIO ENTRE POLLS        1 con BBDD-4 ejecutores
                            1 - 1   Se encolan las solicitudes de conexión
                                250ms <    Colas en peticiones a la app 500 timeouts
                                
                                
                                
                                
                                
                                
                                
maven        <<<<<      Gestion de dependencias
                        Empaquetado de mi app
                        Plantillas - Arquetipos


App                 JAVA                                JS
    Librerias  - 100-500 librerias                    1000-5000
        Libreria 1 - Dependencias   versiones 
        Libreria 2
        Libreria 3
        Libreria 4
        Libreria 5
        
        
        
        
> String nombre="Ivan";

Colocar el texto "Ivan" en la memoria RAM del ordenador (dentro de la zona reservada para el HEAP del proceso JAVA)
Defino la variable nombre de tipo texto
Referencia con la variable, el texto que acabo de poner en la RAM

> nombre="Lucas";

Colocar el texto "Lucas" en la memoria RAM... En el mismo sitio donde ponía Ivan? NOP En otro
Mueve el postit, cambia la referencia de la variable, para que apunte a Lucas


¿Cuantas cosas hay en RAM?    2: "Ivan" y "Lucas"
¿Cual está en uso?            1: "Lucas"
¿Que es Ivan?                 "Ivan" = BASURA

    Garbage collector     
    PASO 1
                            > Ivan? Tiene pegado al lado un postit... Esta siendo referenciado por una variable? NO      
                                        Es susceptible de ser borrado
    PASO 2                  Donde se borra todo lo susceptible de ser borradoç
    
    
    
WLS 1    IP 192.168.1.101:7001
    App 1
WLS 2    IP 192.168.1.102:7001
    App 1
    
    
BC : NGINX APACHE      Mantener asignación por sesion (STICKY_SESSION   JSESSIONID)
    IP 192.168.1.100:80     > 192.168.1.101:7001/app1
                            > 192.168.1.102:7001/app1




APP 4 pantallas
    Inicio
    PETICIONES
    Configuracion
    Cambiar la configuracion
    
Configuracion:
    - Tiempo de demora en cada peticion
    - Tiempo de demora en BBDD
    - Objetos en cache RAM   >          No son basura... Las quiero mantener en cache
    - Objetos en cada peticion RAM   >  BASURA !!!!
    
    
    
jdbc/miTestDB    Esto es lo que escribe el desarrollador para conectarse con la BBDD

Que hace falta para contectar con una BBDD?
RECURSO DE BBDD: DATASOURCE
    nombre: jdbc/miTestDB
    configuracion:
        URL:
            IP o nombre
            Puerto
        Usuario
        Contraseña
        NOMBRE_BBDD
        Driver? El que al final conecta con la BBDD <   Sabe cómo hablar con una determinada BBDD
                Depende de? la BBDD concreta con la que conecte... Modelo y versión
        
        Weblogic ya lleva integrados una serie de drivers... que a veces se me queda corto.
        
        El driver al final qué es???
            Programa (Clase) dentro de una librería (jar)

Quién configura esos datos en nuestra app?
    EL ADMINISTRADOR DEL WEBLOGIC
Por qué?
    1º Quien va a gestionar las conexiones con la BBDD va a ser WEBLOGIC
    2º Me fio del desarrollador???? Menos que del admin de Weblogic
    3º Qué pasa entre entornos?
            Todos tienen los mismos datos de BBDD? NO


Driver BBDD: 
    XA - Transacciones distribuidas / globales
    
Transacciones?
Conjunto de operaciones que realizaré o bien todas o ninguna

N BBDD
    Oracle
        >>> INSERTS    ----|
    MySQL                  |
        >>> INSERTS    ----|
        
JAVA >>>>>> Driver?

TEXTO < Analizar sintacticamente esa query: Parsear parsing
Validar los tipos de datos de los campos

    SELECT 
        campo1,
        campo2,
        campo3,
        campo4
    FROM 
        tabla1, tabla2
    WHERE 
        tabla1.id=tabla2.id
        and campo7>= %PARAMETRO%
        or campo5 LIKE "%%"
        
PreparedStatement




100Gbs
8 <- 15 maquinas
16 <- 8 maquinas


RAM HEAP
    Datos consumibles > basura < GC
    CACHE                                   <<<< Expediente
    
10 maquinas
    CACHE? Cada maquina <<<<<<<< Los tengo replicados en todas o muchas maquinas
    

1 maquina 8 Gbs RAM
3 Gbs son cache ---------- 5 Gbs

2 maquinas ---->          10 Gbs        

1 Maquina 16Gbs RAM
3 Gbs son cache ---------- 13 Gbs   < CADA GC que haga aqui el Weblogic lo flipo !!!!!


