#Importamos la libreria
import camelcase

nombre = "dharma elizabeth bonifacio toledo"

print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'dharma','toledo' 
cam2 = camelcase.CamelCase('dharma','toledo')
print(cam2.hump(nombre))

