#!/usr/bin/env python3
__author__ = 'cap10'

## called as $ ./input_cl2.py -v 1 --somearg "five"

import argparse

parser = argparse.ArgumentParser(description='demonstration.')
parser.add_argument('-v', type=int, dest='theint',
                   help='an integer')
parser.add_argument('--somearg', dest='thestring', type=str,
                   help='a string')
parser.add_argument('-u', dest='uncalled', type=float, default=42.0,
                   help='an optional arg')

args = parser.parse_args()
print("\n", args, args.thestring, args.theint)
