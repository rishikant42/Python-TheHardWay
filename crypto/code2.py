import argparse

parser = argparse.ArgumentParser(prog='my_program')

parser.add_argument('--version', action='version', version='1.1')

subparsers = parser.add_subparsers()

parser_tcp = subparsers.add_parser('tcp')
parser_tcp.add_argument("<host>")
parser_tcp.add_argument("<port>")
parser_tcp.add_argument("--timeout", nargs="?")

parser_serial = subparsers.add_parser('serial')
parser_serial.add_argument("<host>")
parser_serial.add_argument("--baud", nargs=1)
parser_serial.add_argument("--timeout", nargs="?")
parser_serial.add_argument("--add", nargs="+", default=[1,2,3])
parser_serial.add_argument("--spam", type=int, default=11)

print (parser.parse_args())
args = parser.parse_args()

print args.timeout
