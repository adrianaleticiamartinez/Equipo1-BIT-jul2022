import restrictedQuery
import credentialsQuery
import manager
import permisoMedio

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
    permisoMedio.permisoIntermedio(idCliente)
elif tipoUsuario =="Manager":
    manager.managerQuery(idCliente)