
Contenedor miweblogic
    AdminServer   512Mb RAM
    NodeManager
    Server-0      400Mb RAM

Contenedor miMariaDB
Despliegue de una app webapp-test

Server-0, que si hay un error de memoria, se haga un volcado de la RAM a disco
            -XX:+HeapDumpOnOutOfMemoryError
            -XX:HeapDumpPath=/var/log/volcado_memoria.hprof
            
Contenedores:
    Los procesos que se ejecutan dentro de un contenedor.... 


Servidor
    systemd <<<< gestor de servicios en linux
                    Servicio ---> Comando bash
                        Servicio de NodeManager
                            ---> $WL_HOME/user_proyectos/domains/base_domain/bin/startNodeManager.sh
                        
                        Servicio de Server-0
                            depends NodeManage
                            ---> $WL_HOME/oracle_common/common/bin/wlst.sh RUTA/start_server_0.py
                        Servicio de Server-1
                            depends NodeManage
                            ---> $WL_HOME/oracle_common/common/bin/wlst.sh RUTA/start_server_1.py
     ^^^
    systemctl
    
Me obliga a mantener la configuración de la JVM en 2 sitios diferentes, y a mantenerla sinconizada.

start_server_0.py
------------------
nmConnect(usuario,password, ruta)
nmStart('Server-0')



WebLogic: Era multiTenant
    Un programa que permite tener espacios / zonas de ejecucion independientes 
        para dar servicio con una unica instalacion a multiples clientes
    Particiones
    
    
[4295615900 bytes in 60-80 secs]
2 -3 minutos de generacion del volcado de memoria



visualvm
---------------


Server-0
AdminServer

Modulos de diagnostico incorporados:
    Server-0 - Perfil de monitorización bajo, medio, alto    <
        El sistema empieza a recopilar un conjunto de metricas predefinido en función del nivel

Modulos de diagnostico:
    Server-0  <<<< Estableces manualmente qué metricas concretas son las que quieres ir capturando y con que periodicidad
    
    
    
Entorno de producción
Instancia 1 : Servidor 1: AppX
Instancia 2 : Servidor 2: AppX
Instancia 3 : Servidor 3: AppX
Instancia 4 : Servidor 4: AppX

Balanceador de carga

Tareas operación/administración:
    Asegurar que los servidores están funcionamiento - NodeManager
    Escalar el cluster
        scaleUp() scaleDown() <<< Consola Web + WLST
    
Cluster (Estático)
Cluster Dinámico

Cluster: Conjunto de servidores, con los mismo recursos y despliegues, pero pueden tener diferente configuración

Contenedores <<<< 


Quien se encarga de operar el sistema
    Weblogic?
    Kubernetes? / Openshift?   <<<<<<<<<<<<<<<<<<<<<<
    
    
    DESARROLLADOR
    war, ear, jar          <<<<<<<<<<<<<<
    
        VVVVVVV
        DEVOPS  ---->>>  HELM, KUBERNETES, OPENSHIFT, DOCKER
        VVVVVVV
    
    DESARROLLO >
    imagen de contenedor   <<<<<<<<<<<<<<
        Weblogic
            Con el war... desplegado
            
    WEBLOGIC --- Tradicional, NodeManager
        Configurar unos servidores <<<< Cluster    <<< Definir politicas de autoescalado / Escalado manual
            <<<< Despliegue
    
    Kubernetes/Openshift
        Quien si se cae un server lo reinicia < Ya no Node Manager... Ya no tengo nodemanager
        Si es necesario una version nueva de la app... no redespliego en weblogic
            Monto un contenedor nuevo, que ya incluya la nueva versión de la app   <<<<< Kubernetes
        
            Cluster de Weblogic / Balanceador de carga (Nginx, HAProxy, Oracle HTTP Server, Apache httpd)
                Escalado
        Kubernetes va a estar monitorizando los recursos de mis contenedores
            Si los contenedores se quedan sin recursos, crea nuevos contenedores
            
            
        Namespace
            Limits Requests
            
Apps WEB - http(s)  <<<<<<<<< SIEMPRE 
Cluster
    Servidor 1      << https <<        
    Servidor 2      << https <<            BC          << https (TLS 1)<<            Usuarios (Contraseña, pin)
    Servidor 3      << https <<
    Servidor 4
    Servidor 5
    Servidor 6
    
    Qué implica?
        Generar certificados para Servidor1, Servidor2, Servidor3, BC
        Quien los firma? Los de los Servers, YO (Entidad Certificadora que yo genero)
                         BC ... CA reconocida
                         
            Tengo que mantenerlos / renovando             
            
        Tengo que configurar a cada servidor su certificado y clave privada
        Tengo que configurar a todo el mundo (Servers, BC) la CA que yo he generado como de confianza
            
    Sale totalmente gratis con un kubernetes - 5 minutos. Además kubernetes se va a encargar de mantenerlo en el futuro.. Me olvido
    
    
    
    Contenedor 
        Weblogic
        Proxy
        
    Contenedor
        BBDD
        Proxy
        
    Contenedor 
        Balanceador de carga
        Proxy
        
        
Webphere - IBM
Liberty? 




DEV--->OPS     <<<<<      AUTOMATIZAR !!!!   Corriente, Cultura, Filosofía
            Perfil Devops

Cluster 1
    Servidor 1 * SESION_U1   
    Servidor 2 * SESION_U1   GNS         * FECHA-Backup de BBDD
    
    
Singleton   <<    Proveedores de algo

Un unico objeto en memoria capaz de suministrarnos un determinado ALGO
        Generar numeros secuenciales
        Generar conexiones a BBDD 