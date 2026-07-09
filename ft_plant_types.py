#!usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, bloomed: bool):
        super().__init__(name: str, height: int, age: int)
        self.bloomed = bloomed

    def show(self):
        super().show()
        if (self.bloomed):
            print(f"Your rose is blooming beautifully")
        else:
            print(f"Your rose has not bloomed yet")

class Tree(Plant):
    
    
