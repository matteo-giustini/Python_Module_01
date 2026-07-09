#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self):
        self.height += 0.8

    def age_plant(self):
        self.age += 1

def main():
    rose = Plant("Rose", 25.0, 30)
    initial_height = rose.height
    sunflower = Plant("Sunflower", 80.0, 45)
    cactus = Plant("Cactus", 15.0, 120)

    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_plant()
        rose.show()

    growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {growth}cm")

if __name__ == "__main__":
    main()