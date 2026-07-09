#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name

        self._height = 0.0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height: float):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, age: int):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age = age

    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


def main():
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)

    print("Plant created:", end=" ")
    rose.show()

    rose.set_height(25)
    print("Height updated:", rose.get_height(), "cm")

    rose.set_age(30)
    print("Age updated:", rose.get_age(), "days")

    if rose.get_height() == 25:
        rose.set_height(-10)
        print("Height update rejected")

    if rose.get_age() == 30:
        rose.set_age(-5)
        print("Age update rejected")

    print("Current state:", end=" ")
    rose.show()


if __name__ == "__main__":
    main()