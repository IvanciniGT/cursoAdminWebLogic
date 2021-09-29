WEBLOGIC

Servidor de Aplicaciones WEB, JAVA JEE

J2EE > JEE > JEE?
Java Enterprise Edition > Jakarta Enterprise Edition

JEE  Framework para desarrollar aplicaciones web Java

Aplicaciones WEB < Backend        FrontEnd > Javascript   <<<<<<<<<<< JEE
Apps para dispositivos Android

    JDBC < BBDD
    JNDI < Identificación de recursos
    JMS  < Mensajería

Servidores de aplicaciones  <<<<<<
-----   S.A. Clase Empresarial
Weblogic            Pastizal                    Soporte
    Operar automatizadamente el Weblogic:
        wlst   <<<   scripts 
WAS- Websphere      Otro pastizal               Soporte
JBOSS               Esta mejor de precio        Soporte    - RedHat
Wildfly < Upstream JBoss
Glassfish
-----   S.A. Clase Web(solo debe implementar cierta funcionalidad)
Tomcat              Gratis

--------------------------------------
Linea comandos   <<<<<< Más directo... más funcionalidad... más rápido
                        Automatizable <<<<< Scripts                    <<<<< Devops

Dev--->ops = Automatizar   <<<< ? Ganar eficiencia, seguridad
Docker
Metodologías ágiles / SCRUM    <<<<< 
    Entregas de forma iterativa e incremental de la funcionalidad
Servicios WEB, microservicios
    Arquitectura de software    <>     Apps Monoliticas

AWS < Cloud

App X
    Dia 1 - 10000 usuarios
    Dia 10 - 40000 usuarios
    Dia 20 - 100000 usuarios
    Dia 300 - 1000000 usuarios

App Y
    Dia n - 100 usuarios
    Dia n+1 - 100000 usuarios    Black Friday
    Dia n+2 - 10000 usuarios
    Dia n+3 - 1000000 usuarios  Ciber Monday

Entorno de producción:
    Escalabilidad
    Alta disponilidad


Escalabilidad
    Capacidad de adaptar los recursos de una app/sis a las necesidades de cada momento

Alta disponibilidad
    Capacidad de garantizar un determinado tiempo de servicio de la app
    90%     99%       99,9%       99,99%
    Cada 9 que implica?   PASTA !

    Redundancia < Cluster   Activo / Pasivo
                            Activo / Activo    < HA + Escalabilidad


Cluster 5 serv. apps. Activo/Activo
Cluster 50 servidores de apps       <<<<<<   HW? Lo tengo en el almacen? 
    Alquilamos ? a quién? Cloud 

Cloud?
Conjunto de servicios (IT) que una empresa ofrece por Internet
    AUTOMATIZADOS   -      HW 

Que implica un servidor nuevo de aplicaciones en el cluster?
    Instalar SO
    Instalar JavaVirtualMachine JVM         Ansible
    Instalar Weblogic                       Ansible /Bash
    Configurar WL                           Ansible / Bash / WLST
        Añadirlo al cluster                 WLST
    Despliegue de mi app                    WLST
    ------------------------------------------------->      Contenedores: Docker 

Kubernetes + Openshift <<<<<< 
    Kubernetes 4 clusters (50 máquinas)

---------------------------------------------------------------------
Weblogic es un Servidor de apps web JAVA que cumple con el estandar JEE

Arquitectura de software - WEB? Servicio ofrecido sobre internet:   Tim Berners Lee
    Arquitectura Cliente      -    Servidor
                  Navegador             Wlogic
    Protocolo:                              http(s)     <<<<  Protocolo de transferencia de hipertextos
    Formato de intercambio de información:  html        <<<<  Lenguaje de Marcado de hipertexto

Servidores WEB:
    Apache httpd   > surge como servidor web +++++   Proxy reverso / BC
    IIS
    Nginx          < Proxy reverso / BC      +++++    Servidor web

Que hacía un servidor WEB?
    Escucha en un puerto y si recibe una petición por HTTP la sirve

HTTP?
    URL      protocolo://servidor:puerto/ruta?parametros
             http://miservidor:80/app1/home.html
    BODY de la petición
    Metadatos (HEADERS)

    Request (Petición) + Response (la devolución , la respuesta por parte del servidor)
     Method: GET *          Status / Response-code
             POST *                 2XX         OK
             DELETE                 3XX         Redirección
             PUT                    4XX         Error en cliente
             HEAD                   5XX         Error en servidor

    Servidor web: Document ROOT : Estructura de carpetas con archivos

Antaño, los ficheros HTML eran estáticos... Alguien los había escrito.
Quien escribe hoy en dia esos HTML?
    Un programa (Java, Javascript, )

Antes los servidores web, solo tenían que buscar un fichero en un directorio y devolverlo
Hoy en dia, los servidores web, tienen que pedir a un programa que genere un fichero y devolverlo. Estos servidores web evolucionados son nuestros servidores de apps.

JEE > 3 formas de montar estos programas:
        - Servlets              <<<<<<<<    Backend
        ----------------------------------------------------   FRONTEND VVVV Javascript
        - JSP        Mezclar código JAVA con HTML       
        - JFC        Montar componentes reutilizables          Angular, React, Polymer, Vue
                                                                 ExpressJS
                                                                 NodeJS   <<<< La maquina virtual de JS

Arquitectura WEB
    Estandarizar el cliente < Navegador web
    Protocolo de comunicación < http(s)
    Parte de lo que hay en el servidor < Servidor de apps
                                            Capacidad de escucha de peticiones http > Programas (JAVA)
                                            Gestionar las conexiones a BBDD   <<<<< JDBC

Existen muchas cosas que hacemos en el servidor que las podría también estandarizar:
    - Acceder a una BBDD (Oracle, mysql)       Todo el tema de xonexionado a una BBDD y lo estandarizo 
      dentro del Serv. Apps.
    - Enviar un email
    - Mensajería 


Mensajería:        JMS
    Nos ayuda a montar una comunicación asincrona (vs sincronas)  <<<<<
    Servicios WEB / Microservicios

App web tradicional:
    jsp   |
    jfc   |    >>> HTML

Servicio WEB:
    Un programa que su cliente final es quién? Otro programa
    Aquí no tiene sentido usar HTML. Qué formatos usamos?
        XML         SOAP          <<<<<   SOA     Muy pesado. Da lugar a servicios fuertemente acoplados entre si
        JSON        REST          <<<<<   APIs restful   Muy ligero. <<<<<<  Microservicios. Débilmente acoplados
                    ^^^ Protocolos montados sobre HTTP  <   TCP/IP

HTML es un formato orientado a personas humanas, con ojos que ven
    Parrafo
    Negrita
    Tabla
    Lista
    Imagen
    Lista ordenada
    Enlace



Servicio de cargo en tarjeta <    Programa de cargo en tarjeta      <<<< Otro programa 
TPV 
Cajero

Esas comunicaciones. Sincronas o Asincronas?
Mercadona comprando y pago <<<<   Sincrona. Respuesta inmediata..... Quiero esperar a la respuesta
Pago en un peaje           <<<<   Asincrono ? Por que?

Sistemas asincronos de mensajería?    JMS
    - Whatsapp      Emisor    >>  Serv whatsapp  >>    Receptor
                                     -> Garante de la entrega del mensaje
    - MQ
    - RabbitMQ
    - Kafka - Apache



Aplicaciones desarrolladas con un lenguaje que es JAVA

Lenguajes de programación:
- Compilados: (Traducción estática)        C
- Interpretados    Depende del uso de un interprete que hace la tradución en tiempo real:       Python,Bash

JAVA? .java Compilado > bytecode (.class)  >>>> Es interpretado bajo demanda en cada SO por un programa:
    La máquina virtual de java :   Memoria, Configuración de RED
        JIT               Just in time compiler
        GC                Garbage Collector
        ClassLoader       Cargador de programas


JAVA
C
Python   >>>>> Convertir al lenguaje que habla el SO en cuestión

Aplicaciones
SO
HIERRO


Como de eficiente es JAVA en cuanto a memoria RAM?
    JAVA hace un uso INEFICIENTE DE LA RAM..... Garbage collector  <<<<< 
    Por que lo hace? Criterio de diseño de JAVA
        A cambio de qué? Muchas menos horas de desarrollo

    C: Permite hacer un uso muy eficiente de la RAM... a quién? Al desarrollador
                                                        a cambio de qué? Muchas horas de desarrollo

Sabe un desarrollador cuanta RAM usará su app? NPI 
Quién puede saber esto? >>>>   Monitorización



App1    |   App2
-----------------
    SO
-----------------
    HIERRO

Problemas:
    Unas apps pueden afectar a otras
Beneficios:
    Ejecución muy eficiente: App -> SO -> Hierro


    App1 |  App2
-----------------
    SO   |  SO
-----------------
    MV1  |  MV2
-----------------
    Hipervisor       (VBox, VMWare, HyperV, Citrix, kvm)
-----------------
    SO
-----------------
    HIERRO

Problemas:
    Ejecución menos eficiente: App1 -> SO -> Hierro virtual -> Hipervisor -> SO -> Hierro
Beneficios:
    Unas apps NO pueden afectar a otras. Cada una se ejecuta en un entorno aislado: MAQUINA VIRTUAL



    App1 |  App2
-----------------
    C1   |  C2      <<<<<  Son entornos aislados y contenidos (Uso de CPU, RAM, FS, RED) donde ejecutar procesos
-----------------
    Gestor de contenedores    (Docker, Podman, CRIO, ContainerD)
-----------------
    SO LINUX
-----------------
    HIERRO

Instalo office en mi ordenador
    Me bajo el instalador de office
    Ejecuto el instalador
        Copiar archivos a unas carpetas, hacer configuraciones....

Imagen de contenedor <<< Es un ZIP con un programa YA INSTALADO + Configuraciones
    VVVV
Contenedor 1
Contenedor 2

Repositorios de imágenes de contenedores: Docker hub

Software :
    Aplicación: Navegador, Office       Un programa que está pensado para ejecutarse en primer plano,
                                        con interacción con un usuario persona física,
                                        de forma indefinida en el tiempo
------------------- VVVVVVVVVVV                                        
    Servicio                            Un programa que está pensado para ejecutarse en segundo plano,
                                        con interacción con otros programas,
                                        de forma indefinida en el tiempo
    Demonio                             Un programa que está pensado para ejecutarse en segundo plano,
                                        ellos saben que hacer,
                                        de forma indefinida en el tiempo
    Script                              Un programa que ejecuta una serie de tareas predefinidas... hasta que acaba
    --------------
    SO
    Driver

Crear una cuenta en docker hub
Configurar un maquina que vamos a alquilar AWS.


CONTENEDOR:
Entorno aislado dentro de un SO Linux donde ejecutar procesos.
    Configuración de Recursos HW a los que puede acceder
    Configuración de RED: IP ? Interfaz de red?
    

Interfaz de red:
 Ethernet (Cableado)   172.31.0.66
 Wifi
 Loopback    --- Red virtual . No existe realmente 
                 Existe solamente dentro de mi ordenador
    localhost - 127.0.0.1
 Docker      --- Red virtual que vive solo dentro de mi maquina
    El host tiene IP: 172.17.0.1
    Contenedor que tenemos dentro del host APACHE :80
        172.17.0.2:80

Configurar un NAT: Redirección de puertos
 
-----------------------------------------

DOMINIO DENTRO DE UN WEBLOGIC

Conjunto lógico de recursos + Configuración dentro de un conjunto de ejecuciones de WL


Instancias de Weblogic - Server
                                    MI_DOMINIO
Maquina 1:
    WL1 - Proceso (server1)         conf+recursos
    
    WL2 - Proceso (server2)         conf+recursos   ----
                                                        | > Compartan configuración
Maquina 2:                                              |
    WL3 - Proceso (server3)         conf+recursos   ----
    
    
Grupo lógico de servidores     
Cluster de Weblogic?
    Agrupación de servidores que tienen exactamente la misma configuración y recursos
    
Dentro del contenedor:
    Tiene su propio FileSystem: Sistema de archivos

Los SA (Filesystem) de los contenedores están montados mediante la superposición de capas
    Volumenes: Capa adicional en el FS del contenedor. Capas cuyo ciclo de vida no va a asociado al del contenedor
    Capa 1: A nivel del contenedor
    Capa 0: Capa de la imagen del contenedor   <<< Inalterable (a bajo nivel)
        bin         opt         etc         tmp         home
        
        
/HOST

/
    /datos_de_logs                  ...> /logs
                                            /log_dia1_log
    opt
    etc
    tmp
    home
    var/lib/docker
                 /contenedores
                            /prueba   ALTERABLE.... PERO VA ASOCIADA AL CONTENEDOR 
                                    /etc
                                        /apache/httpd.conf
                 /imagenes
                            /httpd      <<<<<<<<<<< Le hacemos creer que esto es el / ES INALTERABLE
                                    /bin
                                    /etc
                                        /apache/httpd.conf
                                    /opt
                                        /bin/httpd
                                    /home

Dentro de un contenedor: ls /               <<<<<<            chroot








Memoria JVM
    Stack
    heap: En esta zona se guardan los datos que los programas van necesitando poner en RAM

-Xms###     < Memoria HEAP inicial < garantizar
-Xmx###     < Memoria HEAP maximo

La recomendación es que sean iguales <<<<<<<<<<<<<<


Arrancamos JVM
    1,1 Gbs
        1Gbs -> HEAP

Datos que guardan los programas?
    Sesion
        Usuario / DNI
        Contraseña

CAIXABANK LOGIN   < Formulario  Datos acceso

Session: según JEE: Un almacen temporal de datos en la RAM de un serv de apps java 
    donde se almacenan datos temporales del usuario.

Cómo identifica WEBLogic / WAS / TOMCAT/ JBOSS a un usuario que está accediendo?
    Con un identificador de sesión <<< QUE SE GENERA
    
Clientes   ->     Servidor
        ---> Dame el form. de login
        < --- Ahi tienes el form de login (HTML) + Cookie que incluye un identificador de sesión
        --> Ahi tienes mis datos de login
        < --- HTML la pag principal de mis movimientos <<< existia está pagina (este HTML) ????
                No, no existía, se ha generado bajo demanda, para mi y en este momento.
                TEXTO (Secuencia de bytes) <<<<  RAM HEAP
                    ^^ Se borra eso de la HEAP, una vez devuelto? NO
                       Cuando se borra? NPI ... cuando pasa el GC
                       Cuando pasa el GC?       npi. JAVA lo decide.
                                                No lo puedo ni configurar
                                                Si el dato está en uso no se borra nunca
                                                
                                                Se pueden dar instrucciones a la MV de como tratar el GC
                                                que la jvm interpretará a su conveninecia y puede ignborar por completo
                                                
                                                NO TENGO CONTROL NINGUNO DEL GC
                                                
                                                Si hace falta RAM, entrará el GC. *****

JSESSION_ID  =   2398423798478293740937829658746523754809aebcf1323123123123

Cookie: Par de datos clave/valor que un servidor manda a un navegador y el navegador almacena 
            (normalmente en un fichero)
        Cada vez que el navegador hace una nueva petición que ocurre al servidor?
            Se le envían todas las cookies que el servidor hubiera mandado previamente
            
RAM            
^                   *                ***
|               *****            *******       *
|       *************       ************     ***
| *******************  ***************** *******
--------------------------------------------------> tiempo            

Necesitamos suficiente HEAP?
    1º   Tiene que entrar en RAM aquello que debe estar permanentemente en RAM
                Si no hay sufucuente espacio?  Problema?
                        OutOf Memory
    2º   Me tiene que entrar una buena dosis de CACHE.                          <<<<<<<<<<<<<<<<<<<<<<<
                Si no hay sufucuente espacio?  Problema?
                        Rendimiento
    3º   Asegurar suciente espacio para la generación de "basura"
                Si dejo poco? 
                        Muchos GC... Rendimiento
                Si dejo mucha?
                        Estoy tirando RAM

OutOfMemory?
        1. No hay suficiente RAM para el minimo de la app.   <   MAS RAM
        2. Memory leak. ??? Cosas que el GC no identifica para su eliminación   <<<<< BUG a ARREGLAR
            Cuanto tiempo puede llevar resolver el bug? De unas horas a unos años!!!!
                Entre tanto tengo que hacer algo con la APP. <<<< REINICIO
                
                
            OUT OF MEMORY >>>>>> REINICIO
            QUE VIENE EL LOBO .... REINICIO
                SI ESPERO AL LOBO .... QUE SE COMA UNA OVEJAS DE POR MEDIO
            
            
            OUT OF MEMORY? Problemas
                Que deja de funcionar....
                Pierdo datos....           <<<<<<< JODIDO
                Degradación previa del rendimiento  <<<<<<< 1 hora el sistema agonizando

CACHE?
Datos de acceso rápido


En una instalación de Weblogic... cuantas MV de JAVA voy a tener arrancados?
1- Admin (no es sino, un server más)
#? NodeManager 1 por máquina "física"
1 por cada Server

NodeManager
    Una instancia de un programa (NodeManager)
    Entre el Admin y los servers
        Comunica el admin > servers
    Que se encarga de gestionar los servers de una máquina "física"


Necesito NodeManager siempre?
Puede instalar Weblogic sin NodeManager

Puedo para server si NodeManager desde el admin?
SI, sin problema
Incluso aunque esté en otra máquina?
SI. Porque la comunicación de apagado se realiza entre Admin y Server

Para que necesito NodeManager?
    Arrancar un servidor remoto
    Monitorizar los servers
    Distribuir la configuración de los dominios  <<<<<< config.xml y más archivos... que están donde?
    en que máquinas? En todas
    Cómo se sincronizan? NodeManager / Con comunicación directa entre admin / servers
    
CLASSPATH   <<<< Donde está el bytecode  (las clases)
PATH  <<<<< 

.java      <<<<  Un huevo
---> javac
.class     <<<<  N huevo
Esos ficheros, cómo se distribuyen por parte del desarrollador
Los metemos en un ZIP, al que le cambiamos la extension y le ponemos .jar

Libreria en JAVA <<<<< Weblogic ??? Si, cuando quiero cargar una librería. Ejemplo:
    Driver de Base de datos en JAVA (JDBC) es un .jar

APP WEB:   Se empaqueta: En otro ZIP que se le cambia la extensión y se le pone: .war
    Un conjunto de clases
    Un conjunto de librerias (otros .jar)
    Archivos de configuración     web.xml
    Y otros archivos de recuros (imágenes, css....)

Un EAR:
    Un empaquetado de apps que se usan de forma conjuntan... tienen dependencias
    
Dentro de un EAR hay WARs y JARs


CLASSPATH: Quiero acceder / ejecutar la clase XXXXXX.... Donde se busca el fichero XXXXXXX.class???
En el CLASSPATH




http (s)
Certificados
Claves públicas y privadas


https?? para qué???
Para frustrar 2 tipos de ataques:
- Man in the middle    <<<<    Encripción
- Phishing . Suplantación de identidad

Encripción: 
    2 tipos de algoritmos:
        Clave simetrica
            Cifra y descifra con la misma clave
        Clave asimética
            Cifra y descifra con distintas claves PAREJA DE CLAVES (publica/privada)

HTTPS ???
    Ambas
    El grueso de la comunicación se hace mediante clave simétrica. MAS RAPIDO
    La clave simetrica se genera bajo demanda y cada poco tiempo para cada pareja de interlocutores
    y es compartida entre ellos mediante un alg. de encripcion basado en clave publ/priv

Suplantación de identidad???
    Engaño al cliente haciendome pasar por el servidor.
    Pidiendome un DNI  <<<<<<  En que teneis confianza los procedimientos que usa la Policia Nacional, que es quien emite el DNI
    
    Necesito un documento que diga quien soy: IP, nombre dominio     CERTIFICADO (clave publica del identificado)
    Alguien que firme aquello .... Entidad Certificadora
    
    
jks ???
    Java Key Store
    Llavero... donde guardar información sensible:
        Certificados
        Claves privadas
        
BEAN: Ente que tengo guardado en la RAM de JAVA y al que sabemos
, sin conocer su naturaleza, como interrogarle


Coherence   CACHE DISTRIBUIDA
                
                                    
                                        >        WL1
Cliente (Paco)      >           BC                  app1
                                                        --> datos en RAM ---> usuario ->   SESION
                                        >        WL2         PUF !!!!                       ^^^
                                                    app1                                    ^^^
                                                        --> datos en RAM ---> usuario ->   SESION   PUFFF    



