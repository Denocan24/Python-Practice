from argparse import ArgumentParser
from src.core.errors import minimumNumberError, invailedNumberError

def argumentParser():
    parser = ArgumentParser()
    parser.add_argument("initial_height", type = float, default=100.0, nargs = "?")
    parser.add_argument("gravity", type = float, default=9.8, nargs = "?")
    parser.add_argument("restitution", type = float, default=0.7, nargs = "?")
    parser.add_argument("dt", type = float, default=0.1, nargs = "?")
    parser.add_argument("stop_threshold", type = float, default=0.1, nargs = "?")
    args = parser.parse_args()
    if args.initial_height <= 0:
        raise(minimumNumberError)
    if args.gravity <= 0:
            raise(minimumNumberError)
    if args.restitution <= 0 or args.restitution > 1:
            raise(invailedNumberError)
    if args.dt <= 0:
            raise(minimumNumberError)
    if args.stop_threshold <= 0:
            raise(minimumNumberError)
    return args