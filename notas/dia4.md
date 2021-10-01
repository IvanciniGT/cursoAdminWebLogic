App Word  ----   Quien la ejecuta ? S.O.

JAVA ---- Compila (bytecode)    ---- Interpretarlo (JVM)
C               -----> Compilo      ---> SO destino
C#              -----> Compilo      ---> SO
Python  ---------------------------- Interpreta (Python)


JAVA - JIT (JVM) JustInTimeCompiler     HotSpot

Warmup time

------



Cuando llamamos a un programa: JSP / Servlet / JFC  (dentro de una webapp)

Servidor de apps:
    1 - Se recibe la petición por parte del serv. de apps.
    2 - Se recogen los parametros? URI
    3 - A la cola 
    4 - La petición espera hasta que hay un worker (thread) libre
    5 - El ejecutor toma la petición y?
    6 - Ejecuta el código de la aplicación (el programa concreto que se invoque en la petición)
    7 - Toma los parametros de la petición
    8 - En base a ellos hace sus tareas
        - Calculos
        - Consultas a BBDD              <<<<<<    BBDD Tardará un rato en contestar. Demora BBDD
            Hasta que la BBDD Conteste el ejecutor espera
        - Enviar un email
        - Conectar con un servicio WEB
    9 - Una vez realizadas sus tareas. Componer un resultado (Texto: HTML, JSON, YAML, XML, EXCEL, PDF...)
    10 - Se devuelve ese resultado
    
    
Para hacer sus tareas (8) el ejecutor tarda un rato... DEMORA
El ejecutor va poniendo en RAM una serie de datos (Respuesta BBDD, serv web, texto que compone para devolver al cliente)
Al final la peticion finaliza... 
Una vez finalizada, que pasa con todo lo que se ha ido poniendo en la RAM?
    No pasa NADA ... alli se queda en la RAM... si bien son datos que ya no valen para nada
        >>>> BASURA      Objetos por peticion: 5
        
Por el hecho de mi app estar funcionando, la app necesita una serie de datos cargados permanentemente en RAM
Además, mi app puede ir generando una cache <<<< Objetos en Cache: 50

DIA 1:
Me llega una nueva APP.
Qué hago?
Cómo configuro el WL?
    OPCION 1: Paso de todo ... Siguiente siguiente .... y que sea lo que dios quiera....
    OPCION 2: El desarrollador me da una config... la pongo.... y que sea lo que dios quiera...
        Me quito de responsabilidad
    OPCION 3: Intentar estimar esos parametros de forma más o menos realista... A priori
                Simular un comportamiento normal de la aplicación
                    Apache JMeter, LoadRunner (HP)
                Monitorizo
    OPCION 4: Poco a poco voy monitorizando la app y voy ajustando los paramtros de configuración. <<<<<
                                VVVVVVVVV
                                Me ayuda a entender las características de la app... su naturaleza    <<<<< Cambiante
                                                VVVVVVVVV
                                                Aqui puedo configurar bien WL   
                Requiere tiempo....



JMETER:
Arbol de pruebas:
    - Simulacion de carga a nuestro servidor <<<<< Manual
                                                        Escribir nosotros a mano las peticiones que haría un usuario
                                             <<<<< SemiAutomatica 
                                                        Activar JMETER como proxy : IP(JMETER)
                                                        Navegador de internet : Configurar esa IP como proxy
                                                        Uso la aplciacion desde el navegador
                                                        Una vez grabado el uso de la app.... 
    - Recopiladores de metricas
    
MONITORIZAR APP / ENTENDER APP
1º Entender el comportamiento de mi app con un unico usuario  <<<<<<   LINEA BASE. Lo mejor que puedo esperar de 
                                                                        la app instalada en mi infra.
        Si se quiere mejorar la linea base: Desarrollador, BBDD, ....                                                                        
        
        Mi objetivo de configuración: QUe en carga normal de la app la LINEA BASE "no se degrade" demasiado
    
    Linea base: 2040ms < Tiempo medio que tarda una peticion en procesarse
    10 usuario: 2040ms
    15 usuarios: 2040ms
    25 usuarios: 2080ms
    30 usuarios: 2045ms
    35 usuarios: 2400ms    <<<<<< Empieza la fiesta !!!!!!!!!!!
    
    A qué se puede deber?
        - Opcion 1: Me estoy quedando sin ejecutores
        - Opcion 2: Me estoy quedando sin CPU       <<<<<<<<<< Encolan ejecutores en CPU >>> Degradación de rendimiento
        - Opcion 3: Me estoy quedando sin RAM       <<<<<<<<<< Mucho Garbage Collection  >>> Degradación del rendimiento
                    Me quedo sin RAM                <<<<<<<<<< EXPLOSION GIGANTE: Out of memory... Aqui no atiendo
        - Opxión 4: Me quedo sin conexiones de BBDD <<<<<<<<<< Se encolan los ejecutores en BBDD >>> Degradación de rendimiento
        
        OPCION 1: NO HAY PROBLEMA AHORA MISMO !!! Hasta 400... y veo que hay parados 
            Si lo hubiera !!!!!
                Puedo poner más ejecutores? Qué implica cada ejecutor? CPU y Memoria
                    CPU : Sistema: top
                    MEMORIA: Memoria de JAVA   <<<<< Es una maquina virtual y tiene su conf. de memoria
                            Si se está llenado la memoria de JAVA, miro la de sistema... a ver si puedo subir
                                free
                    Si hay recursos: Poner más ejecutores
                    Si no hay recursos? Otra maquina al cluster o amplio recursos
                    
            
            
        
Poll de conexiones : 17
Si tengo un poll de conexiones de BBDD de 15
1 peticion: 2 segundos 
    De los 2 segundos.... cuanto se dedica a BBDD? 1 segundo, la mitad 50%
    
                T1      T1+1        T1+2     T1+3
Ejecutor 1       wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
                 <<< PETICION >>>>>><<< PETICION >>>>>>
Ejecutor 2       wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 3          wwwwwwwbbbbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 4       wwwwwwwwwwwwwwwwwbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 5       wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 6         wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 7       wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 8       wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 9             wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 10      wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 11         wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 12      wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 13           wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 14      wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 15        wwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb

Ejecutor 16      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
                 <<< PETICION >>>>>>      <<< PETICION >>>>>>
Ejecutor 17      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 18      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 19      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 20      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 21      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 22      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 23      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 24      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 25      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 26      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 27      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 28      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 29      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb
Ejecutor 30      wwwwwwwww          bbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbbwwwwwwwwwbbbbbbbbbb


17 conexiones maximas - Ratio tiempo se emplea en BBDD 50%
34 conexiones

ME HE QUEDADO SIN CONEXIONES. Que hago?
    Miro a ver si puedo hacer más conexiones a BBDD?
        - BBDD??? A ver si me deja
            -  Si no me deja: Yo nada.... Estoy atado de pies y manos
        - Si me dejan?
            - Modificar el parametro ... el poll?.... puedo??? que me va a implicar???
                Que los ejecutores que están en espera... dejarán de estarlo y :
                    - Esos ejecutores Más uso de CPU y RAM. Lo aguanta mi maquina?
                        - SI : A por ello
                        - NO: Pues a ver que hago? Más maquina... más maquinas....
                        
                        
                        
MEMORIA:
Maximo de HEAP 500Mb
De los 500 la MV tenga reservados al SO: 400Mb.              <<<<<<< Amarilla
    Todavía podría JAVA pedir al SO: 100Mbs adicionales      <<<<<<< Azul
La linea roja es lo que tengo libre de los 400 que tengo reservados.
En uso tengo la azul menos la roja

470 lo reservado al SO
205 Libres
265 ocupados


17 -> 24 conexiones : 60 usuarios tiempos 2080 ms

Con un determinado uso de Recursos de CPU y RAM quiero 
    identificar a cuantos usuarios/peticiones soy capaz de atender: 500 usuarios

Miro el pico que puedo tener en el sistema: 2000 personas: 
    4 maquinas 

Cluster Producción:
    Serv WL 1 - 30%
    Serv WL 2 - 30%

Como se caiga uno de ellos... estoy vendido

app 1 seg java
    1 seg bbdd
    +- 500ms entre peticiones
    
serv. apps.
    Poll de ejecutores  -   Ratio, Relacion     100
    Poll de BBDD        -                        50    50%

BBDD 82-83-87
254 total - 86 espera = 168 ejecucion

85/170 = 50%



Degradación gigante de rendimiento debido a GC:
Decisiones:
    - 1º hace cuanto está el sistema en uso?
        - Si acabo de arrancar el sistema:
            Problema de recursos. Tengo el sistema mal configurado. Necesito más RAM. La app necesita más RAM.
        - Si el sistema lleva tiempo funcionando: horas, dias:
            >>>>   Memory leak. BUG ! en una cache
                    Procedimiento de emergencia: REINICIO DEL SERVER
                        Es pan para hoy y hambre para mañana MONITORIZAR 
                    En paralelo:
                        Notificar a desarrollo: HAY UN BUG EN LA APP
                            cri cri.....
                            Armas para ayudar al eq. de desarrollo
                                Volcado de RAM <<<<< 
                                    Incorpora un volcado de hilos
Un momento en que el GC tumba el rendimiento:
Cuando tarda más en borrar la RAM que la app en poner cosas. Aqui el sistema funciona, de por vida
    VVVVV DIAS 
Cuando ya no entran más cosas > EXPLOSION


visualvm

Argumentos JMV:
    Configuración de memoria:
        -Xms#####   La regla es configurarlos iguales entre si
        -Xmx#####
    Cuando tengo problemas de memoria: 
        1 - Afecta bastante al rendimiento
            
            MONITORIZAR EL USO DEL GC
            
            -XX:+useGCLogFileRotation
            -XX:NumberOfGCLogFiles=5
            -XX:GCLogFileSize=100M
            -Xloggc:/var/logs/gc.log         gc0.log    gc1.log
            
        2 - Requiere mucho espacio en HDD y provoca una demora en el reinicio de un servidor <<< Implica un menor compromiso !!!!!
            
            -XX:+HeapDumpOnOutOfMemoryError
            -XX:HeapDumpPath=/var/log/volcado_memoria.hprof
            
            -XX:OnOutOfMemoryError="    shutdown -r now   "


Docker hub <<<< Imagenes que contienen una instalación de Weblogic

Oracle - repo github
    dockerfile: Es un fichero que alimenta un programa "docker build" => generar una imagen de contenedor
    
    
dominio: base_domain
    AdminServer   JVM Weblogic
    Cluster                                 < Despliegue
        Server-0      JVM Weblogic
        Server-1      JVM Weblogic
    Server-2
    
    
Contenedor-Maquina Hierro-Servidor fisico
    Dominio
    Weblogic
    NodeManager

Maquina física - Instalacion nueva
    Weblogic
        server1
        server2
    NodeManager    ---- No respondería a peticiones del dominio
        Despues de instalar NodeManager
        WLST:
            nmenroll(host admin del dominio)    < Enrolar el nodemanager con el adminserver

----------


