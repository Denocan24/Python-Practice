class Object:
    def __init__(self, id: int, name: str, location: tuple[int, int], weight: int):
        self.id = id
        self.name = name
        self.location = location
        self.weight = weight

    def grow(self, amount: int):
        self.weight += amount

    def move(self, coordinate: tuple[int, int]):
        x, y = coordinate
        for i in range(x):
            for j in range(y):
                print(j ,"Y")
            print(i, "X")
        self.location = coordinate