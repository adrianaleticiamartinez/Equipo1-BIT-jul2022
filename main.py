import restrictedQuery
import credentialsQuery
import manager

print("Ingrese el id cliente: ")
idCliente = input()
print("Ingrese usuario asesor: ")
usuarioAsesor = input()
print("Ingrese contraseña: ")
contrasenia = input()


tipoUsuario = credentialsQuery.searchUser(usuarioAsesor, contrasenia)
if tipoUsuario =="Restringido":
   restrictedQuery.searchClient(idCliente)
elif tipoUsuario =="Validador":
    '''Llamar funcion'''
elif tipoUsuario =="Manager":
    manager.managerQuery(idCliente)