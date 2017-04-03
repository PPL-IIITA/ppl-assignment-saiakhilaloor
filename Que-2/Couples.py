from girls import girls
from boys import boys
from gifts import gifts

class Couples(object):
	"""docstring for Couples"""
	def __init__(self, boy, girl):
		'''Method to initalise Couples object
		Arguments:
			-boy=boy (object)
			-girl=girl (object)
			-happiness=0
			-totalgiftcost=0
			-gift[] =[]
			-compatibility = 0
		'''
		super(Couples, self).__init__()
		self.boy = boy
		self.girl = girl
		self.happiness = 0
		self.totalgiftcost=0
		self.gift = []
		self.compatibilty=0
