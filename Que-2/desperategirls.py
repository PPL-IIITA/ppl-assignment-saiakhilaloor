
class desperategirls:
    def __init__(self, name, attractiveness, intelligence, mainCost):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.mainCost = mainCost
        self.status = 'single'
        self.boyname = ''
        self.happiness = 0

    def gethappiness(self):
        return self.happiness