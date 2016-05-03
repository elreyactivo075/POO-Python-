class persona():
	def __init__(self):
		pass
	def brincar(self):
		print "estoy brincando lol "

	@classmethod
	def corre(cls):
		print "estoy corriendo lol "

	@staticmethod
	def nadar():
		print "estoy nadando lol "

jose = persona()
jose.nadar()

