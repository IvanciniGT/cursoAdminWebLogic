connect("admin","welcome1","t3://localhost:7001")

edit()              # Solo si voy a hacer cambios
startEdit()         # Solo si voy a hacer cambios

listado_datadources=cmo.getJDBCSystemResources()

for datasource in listado_datadources:
    print("Hay un datasource llamado: " + datasource.getName() )
    print("     Máximo de conexiones anterior: " + str( datasource.getJDBCResource().getJDBCConnectionPoolParams().getMaxCapacity() ))
    datasource.getJDBCResource().getJDBCConnectionPoolParams().setMaxCapacity(17) 
    print("     Máximo de conexiones actual  : " + str( datasource.getJDBCResource().getJDBCConnectionPoolParams().getMaxCapacity() ))


save()             # Solo si he hecho cambios
activate()         # Solo si he hecho cambios
stopEdit()         # Solo si he hecho cambios

disconnect()