import restrictedQuery
import credentialsQuery

print("Ingrese el id cliente: ")
idCliente = input()
print("Ingrese usuario asesor: ")
usuarioAsesor = input()
print("Ingrese contraseña: ")
contrasenia = input()



credentialsQuery.searchUser(usuarioAsesor, contrasenia)

tipoUsuario = "algo"
if credentialsQuery.searchUser(usuarioAsesor, contrasenia) =="restringido":
   restrictedQuery.searchClient(idCliente)
elif tipoUsuario =="validador":
    '''Llamar funcion'''
elif tipoUsuario =="Manager":
    '''Llamar funcion'''