class klasse(object):
	anzahl_lehrer = 0
	def __init__(self,lehrer):
		self.__class__.anzahl_lehrer += 1
		self.__klassenlehrer = lehrer
	def wer_ist_klassenlehrer(self):
		print (self.__klassenlehrer)
	def __del__(self):
		self.__class__.anzahl_lehrer -= 1
		print ("Die Instanz wurde geschlossen")
		
R10 = klasse("Meyer")
R10.wer_ist_klassenlehrer()
print (R10.anzahl_lehrer)
R11 = klasse("Michi")
print (R11.anzahl_lehrer)
del(R10)
print (R11.anzahl_lehrer)