class miserboys():
    def __init__(self,name,attractiveness,intelligence,budget,minRequirement):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget
        self.minRequirement = minRequirement
        self.status = "single"
        self.girlname = ''
        self.happiness = 0
        self.amount = 0

    def gethappiness(self):
        return self.happiness