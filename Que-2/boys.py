class boys(object):
	"""docstring for boys"""
	def __init__(self, name, intelligence, attractiveness, budget, minRequirement, category ):
		''' Method to initialise boys object
		Arguments:
			-name=Name
			-intelligence = intelligence
			-attractiveness = attractiveness
			-budget = budget
			-minRequirements = minRequirements
			-category = category
			-status = single
			-happiness = 0
			-girlfriendName=''
		'''
		self.name = name
		self.intelligence = intelligence
		self.attractiveness = attractiveness
		self.budget = budget
		self.minRequirement = minRequirement
		self.category = category
		self.status = "single"
		self.happiness = 0
		self.girlfriendName=''

		
