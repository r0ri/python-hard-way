class AAA(object):
	def funktion_a(self):
		print("AAA-funktion_a")
	def funktion_b(self):
		print("AAA-funktion_b")
class BBB(object):
	def funktion_b(self):
		print("BBB-funktion_b")
	def funktion_c(self):
		print("BBB-funktion_c")
class CCC(BBB,AAA):
	def funktion_c(self):
		print("CCC-funktion_c")
	def funktion_d(self):
		print("CCC-funktion_d")
 
x = CCC()
x.funktion_a()
x.funktion_b()
x.funktion_c()
x.funktion_d()