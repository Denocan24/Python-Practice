from src.parser import terminal_parser
from src.core.errors import minimumNumberError

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
        
if __name__ == "__main__":
    # player = Object(1, "Player", (0, terminal_parser.argumentParser()), 50)
    # player.grow(10)
    # player.move((0,0))
    # print(player.location)
    try:
        print("Başlangıç Değerleri: ", terminal_parser.argumentParser())
        k = terminal_parser.argumentParser().initial_height
        while k > 1:
            k -= 1
            print(k)
    except minimumNumberError as e:
        print(e)