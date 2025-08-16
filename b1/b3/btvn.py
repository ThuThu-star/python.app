class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def __str__(self):
        return f"{self.name}"
    
    def make_sound(self):
        print(f"{self.name} kêu {self.sound}")

animals = [
    Animal("Sư tử", "Có vú", "gầm gừ"),
    Animal("Hổ mang", "Bò sát", "rít")
]

for animal in animals:
    animal.make_sound()


    def list(self):

