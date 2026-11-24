class Object:
    def __init__(self,
                 inital_height = float,
                 gravity = float,
                 restitution = float,
                 dt = float,
                 stop_threshold = float):
        self.inital_height = inital_height
        self.gravity = gravity
        self.restitution = restitution
        self.dt = dt
        self.stop_threshold = stop_threshold

    def grow(self, amount: int):
        self.weight += amount

    def move(self, coordinate: tuple[int, int]):
        x, y = coordinate
        for i in range(x):
            for j in range(y):
                print(j ,"Y")
            print(i, "X")
        self.location = coordinate

class physicsRules(Object):
    def __init__(self, 
                 inital_height = float, 
                 gravity = float, 
                 restitution = float,
                 dt = float, 
                 stop_threshold = float):
        super().__init__(dt=dt,
                         gravity=gravity,
                         inital_height=inital_height,
                         restitution=restitution,
                         stop_threshold=stop_threshold)