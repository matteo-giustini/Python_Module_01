class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age_days = age
        self.stats = self.Stats()

    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(f"{self.grow_calls} grow, {self.age_calls} age, {self.show_calls} show")

    def show(self):
        self.stats.show_calls += 1
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")
    
    def grow(self, cm):
        self.stats.grow_calls += 1
        self.height += cm

    def age(self, days):
        self.stats.age_calls += 1
        self.age_days += days

    @staticmethod
    def older_than_year(age: int):
        print(f"Is {age} days more than a year? -> {age > 365}")

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self, seeds):
        super().bloom()
        self.seeds = seeds
        

    def show(self):
        super().show()
        print(f"Seeds:{self.seeds}")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self.stats = self.Stats()

    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0
        
        def display(self):
            super().display()
            print(f"{self.shade_calls} shade")

    def produce_shade(self):
        self.stats.shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, cm):
        super().grow(cm)
        self.nutritional_value += cm

    def age(self, days):
        super().age(days)
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

def main():

    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.older_than_year(30)
    Plant.older_than_year(400)
    print("\n===Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.stats.display()
    print("[asking the rose to grow and bloom]")
    rose.grow(2.3)
    rose.bloom()
    rose.show()
    rose.stats.display()

    print("\n===Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.stats.display()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.stats.display()

    print("\n===Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(67)
    sunflower.bloom(42)
    sunflower.show()
    sunflower.stats.display()

    print("\n===Anonymus")
    anonymous_plant = Plant.anonymous()
    anonymous_plant.show()
    anonymous_plant.stats.display()

if __name__ == "__main__":
    main()
