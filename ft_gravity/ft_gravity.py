from src.parser import terminal_parser
from src.core.errors import minimumNumberError, invailedNumberError
from src.core.physics import Object
        
if __name__ == "__main__":
    try:
        print("Başlangıç Değerleri: ", terminal_parser.argumentParser())
        k = terminal_parser.argumentParser().initial_height
        while k > 1:
            k -= 1
            print(k)
    except(invailedNumberError, minimumNumberError)as e:
        print(e)