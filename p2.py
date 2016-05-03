
class persona():
	def __init__(self):
		pass
	def saludar(self):
		print ("como te va idiotas")

	@classmethod
	def despedir(cls, nombre):
		print ("vete a la mierda " + nombre)
persona.despedir("Ariel")
