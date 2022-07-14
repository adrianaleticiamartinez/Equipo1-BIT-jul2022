import restrictedQuery

print("Ingrese el id cliente: ")
idCliente = input()
print("Ingrese usuario asesor: ")
usuarioAsesor = input()
print("Ingrese contraseña: ")
contrasenia = input()


restrictedQuery.searchClient(idCliente)
restrictedQuery.searchClient('1')
