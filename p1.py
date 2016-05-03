class persona():
	edad= 18 #variable de clase
	def __init__(self, nombre, nacionalidad):
		self.nombre=nombre	#variables de instancias
		self.nacionalidad=nacionalidad #variables de instancias
	def nadar(self):
		print "hola putos estoy nadando pendejos envidienme :v "


persona1=persona("carlos", "dominicano")
print (persona.edad)
print (persona1.nombre)
persona1.nadar()

