class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toString(self):
        return f"Hello {self.name}, {self.age}"

