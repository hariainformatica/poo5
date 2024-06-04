from coleccioncitas import ColeccionCitas
from cita import Cita

cc = ColeccionCitas()
#print(cc.leer())
#cc.buscar(Cita('La vida es bella'))

print(cc.buscar(Cita('La vida es bella')))
print(cc.insertar(Cita('Quedan 2 semanas de clase')))
#cc.borrar(Cita('La vida es bella'))
cc.actualizar("Quedan 2 semanas de clase", "Aguanta ahí")
print(cc.leer())