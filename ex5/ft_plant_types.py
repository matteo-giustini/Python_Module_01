class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age_days = age

    def grow(self, cm):
        self.height += cm

    def age(self, days):
        self.age_days += days

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")


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

def main():
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    Tree.produce_shade

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    tomato.grow(42)
    tomato.age(20)
    tomato.show()
    
if __name__ == "__main__":

    main()

