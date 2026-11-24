from src.parser import terminal_parser
from src.core.errors import minimumNumberError, invailedNumberError
from src.core.physics import Ball, physicsRules
        
if __name__ == "__main__":
    try:
        args = terminal_parser.argumentParser()
        ball = Ball(args.initial_height, args.stop_threshold, 0.0)
        physics =  physicsRules(args.initial_height, args.gravity, args.restitution, args.dt, args.stop_threshold, ball)
        print(physics.simulate())
    except(invailedNumberError, minimumNumberError)as e:
        print(e)