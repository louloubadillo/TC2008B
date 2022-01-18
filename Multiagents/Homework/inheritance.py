# Author: Lourdes Badillo
"""
Inheritance exercise
"""
class Vehiculo: 
  def __init__(self, capacidad, kilometraje):
    self.capacidad = capacidad
    self.kilometraje = kilometraje

  def tarifa(self):
    print(f"La tarifa es: {self.capacidad*100.0}")

  def anuncio(self): 
    print(f"Este vehículo tiene capacidad {self.capacidad} y kilometraje {self.kilometraje}")
  
class Autobus(Vehiculo): 
  def __init__(self, capacidad, kilometraje):
    super().__init__(capacidad, kilometraje)
  
  def tarifa(self):
    norm = self.capacidad*100
    extra = norm*0.1
    print(f"La tarifa es: {norm+extra}")
  
  def anuncio(self): 
    print(f"Este autobús tiene capacidad {self.capacidad} y kilometraje {self.kilometraje}")

#Ejemplos
v1 = Vehiculo(10,200)
v2 = Vehiculo(20,300)
a1 = Autobus(10,200)
a2 = Autobus(20,300)

v1.tarifa()
v2.tarifa()
a1.tarifa()
a2.tarifa()

v1.anuncio()
a1.anuncio()
