import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='acc', action='store_const',
                    const=min, default=max,
                    help='sum the integers (default: find the max)')

parser.add_argument('-a', action="store_true", default=False)
args = parser.parse_args()
print args.acc(args.integers)
