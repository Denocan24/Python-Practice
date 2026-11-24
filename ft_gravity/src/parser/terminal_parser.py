from argparse import ArgumentParser
from src.core.errors import minimumNumberError

def argumentParser():
    parser = ArgumentParser()
    parser.add_argument("initial_height", type = float)
    parser.add_argument("gravity", type = float)
    parser.add_argument("restitution", type = float)
    parser.add_argument("dt", type = float)
    parser.add_argument("stop_threshold", type = float)
    args = parser.parse_args()
    if args.initial_height <= 0:
        raise(minimumNumberError)
    return args