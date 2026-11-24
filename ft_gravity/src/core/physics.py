class Ball:
    def __init__(self,
                 inital_height: float,
                 stop_threshold: float,
                 velocity: float):
        self.inital_height = inital_height
        self.stop_threshold = stop_threshold
        self.velocity = velocity

    def grow(self, amount: int):
        self.weight += amount

    def move(self, coordinate: tuple[int, int]):
        x, y = coordinate
        for i in range(x):
            for j in range(y):
                print(j ,"Y")
            print(i, "X")
        self.location = coordinate

class physicsRules:
    def __init__(self, 
                 inital_height: float, 
                 gravity: float, 
                 restitution: float,
                 dt: float, 
                 stop_threshold: float,
                 ball: Ball):
        self.initial_height = inital_height
        self.gravity = gravity
        self.restitution = restitution
        self.dt = dt
        self.stop_threshold = stop_threshold
        self.ball = ball

    def movePhysics(self) -> bool:
        self.ball.velocity = self.ball.velocity - (self.gravity * self.dt)
        self.ball.inital_height = self.ball.inital_height + (self.ball.velocity * self.dt)
        if self.ball.inital_height <= 0.0:
            self.ball.inital_height = 0.0
            self.ball.velocity = -self.ball.velocity * self.restitution
            max_bounce_height = (self.ball.velocity ** 2) / (2 * self.gravity)
            if max_bounce_height < self.stop_threshold:
                return False
        return True

    def simulate(self, max_steps: int = 10000) -> list[float]:
        heights = [self.ball.inital_height]
        steps = 0
        while steps < max_steps:
            is_active = self.movePhysics()
            heights.append(self.ball.inital_height)
            steps += 1
            if not is_active:
                break

        return heights