class Motorcycle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"Motorcycle: {self.make} {self.model}"