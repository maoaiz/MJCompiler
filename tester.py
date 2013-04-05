from src import mj_lex

class tester():

	def __init__(self):
		pass
	
	
	def testFile(self, file):
		try:
			f = open('test/%s'%file,'r')	#Load test file.
			s = f.read()				#Read the text of the file
			print "\n\n --------------------CODE------------------------\n\n",s
			_tester = mj_lex.MJLex()	#Create an object of the lexer
			f.close()
			return _tester.MJLexer(s)	#Do the test and return the result.
		except:
			return "\nHa ocurrido un error intentando abrir el archivo: %s \n"%file

			
	def testString(self, s):
		print "\n\n --------------------CODE------------------------\n\n",s
		_tester = mj_lex.MJLex()	#Create an object of the lexer
		return _tester.MJLexer(s)	#Do the test and return the result.