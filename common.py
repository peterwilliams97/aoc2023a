"""
    Functions used by multiple solutions.
"""
import re
import argparse

RE_NUMBERS = re.compile(r"\d+")
def numbers_(text):
    return [int(s) for s in RE_NUMBERS.findall(text)]

def parse_args(description, default_input):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-i', '--input', default=default_input, help="Input file path")
    return parser.parse_args()

def read_text(filename):
    return open(filename).read()

def read_lines(filename):
    return read_text(filename).splitlines()

def read_rows(filename):
    lines = read_lines(filename)
    return [list(line) for line in lines]

def char_positions(rows, char):
    "Returns `positions` where positions((y,x)) exists if rows[y][x] == `char`."
    positions = set()
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c == char:
                positions.add((y, x))
    return positions