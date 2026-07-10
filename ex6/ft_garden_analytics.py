class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age_days = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")


@staticmethod
def older_than_year(age: int):
    print(f"Is {age} days more than a year? -> {age > 365}")

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

    class 

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self):
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

if __name__ == "__main__":

    older_than_year(1000)
