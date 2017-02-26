class gifts(object):
	"""docstring for gifts"""
	def __init__(self, price, value, category):
		'''Method to initialise gifts object
		Arguments:
			-price=price
			-value=value
			-category = category
		'''
		super(gifts, self).__init__()
		self.price = price
		self.value = value
		self.category = category
		
