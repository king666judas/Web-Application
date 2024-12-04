
class car:
    def __init__(self, a, b, c):
        self.color = a
        self.color = b
        self.mod = c
        print(self.color, self.model, self.mod)
    def __str__(self) -> str:
        return f"{self.color}-{self.model}-{self.mod}"
    
car1 = car("white", "Toyota", "2008")