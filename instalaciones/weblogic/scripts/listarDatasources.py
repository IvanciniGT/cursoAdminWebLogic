

# Obtengamos los datos de la conexion <<<<<


connect("admin","welcome1","t3://localhost:7001")

listado_datadources=cmo.getJDBCSystemResources()

for datasource in listado_datadources:
    print("Hay un datasource llamado: " + datasource.getName() )
    print("     Máximo de conexiones anterior: " + str( datasource.getJDBCResource().getJDBCConnectionPoolParams().getMaxCapacity() ))

disconnect()