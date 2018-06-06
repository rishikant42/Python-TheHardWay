import optparse
import argparse

def main():
    p = optparse.OptionParser()
    p.add_option('--person', '-p', default="world")
    p.add_option('--abc', '-a', default="apple")
    options, arguments = p.parse_args()
    print 'Hello %s' % options.person
    print 'Hello %s' % options.abc

def otr():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--echo", help="h", action="store_true")
    parser.add_argument("apple")
    args = parser.parse_args()
    print(args.echo)

otr()
