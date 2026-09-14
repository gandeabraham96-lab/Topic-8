class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"Car: {self.make} {self.model}"