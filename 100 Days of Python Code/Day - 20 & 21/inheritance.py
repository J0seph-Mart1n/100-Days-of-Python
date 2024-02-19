class Animal:
    def __init__(self):
        self.no_of_eyes = 2
        self.legs = 4

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Underwater")

    def swim(self):
        print("Swimming in water")

sardine = Fish()
print(sardine.no_of_eyes)
sardine.breathe()

