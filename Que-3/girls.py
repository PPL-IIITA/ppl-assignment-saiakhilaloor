class girls:
    def __init__(self,name,attractiveness,intelligence,mainCost,category):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.mainCost = mainCost
        self.category = category
        self.status = 'single'
        self.happiness = 0

class desperategirls(girls):
    def __init__(self):
        self.category="The Desperate"

class normalgirls(girls):
    def __init__(self):
        self.category = "The Normal"

class choosygirls(girls):
    def __init__(self):
        self.category = "The Choosy"