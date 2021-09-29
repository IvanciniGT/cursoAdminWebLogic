connect("admin","welcome1","t3://localhost:7001")

listado_servidores=cmo.getServers()

for servidor in listado_servidores:
    print("Hay un servidor llamado: " + servidor.getName() )
    print("        Su Puerto es el: " + str(servidor.getListenPort()) )
    print("               Su IP es: " + servidor.getListenAddress() )

disconnect()