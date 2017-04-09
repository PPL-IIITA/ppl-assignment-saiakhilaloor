class boys:
    def __init__(self,name,attractiveness,intelligence,budget,minRequirement,category):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget
        self.minRequirement = minRequirement
        self.category = category
        self.status = "single"
        self.happiness = 0

class geekboys(boys):
    def __init__(self):
        self.category = "The Geek"

class miserboys(boys):
    def __init__(self):
        self.category = "The Miser"

class generousboys(boys):
    def __init__(self):
        self.category = "The Generous"
