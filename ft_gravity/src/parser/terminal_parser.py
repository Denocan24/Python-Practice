from argparse import ArgumentParser

def argumentParser():
    parser = ArgumentParser()
    parser.add_argument("initial_height", type = float)
    parser.add_argument("gravity", type = float)
    parser.add_argument("restitution", type = float)
    parser.add_argument("dt", type = float)
    parser.add_argument("stop_threshold", type = float)
    args = parser.parse_args()
    return args