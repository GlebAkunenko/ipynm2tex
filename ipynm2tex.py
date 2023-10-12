import argparse
import inspect, os
import sys
from main import run

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

args = argparse.ArgumentParser()
args.add_argument("path", type=str, help="Path to current folder")
args.add_argument("input", type=str, help="Path to the .ipynm file")
args.add_argument("-o", "--output", type=str, default='output.tex', help="Path to the result .tex file")

args = args.parse_args()

if args.output == "output.tex":
	args.output = args.path + "/output.tex"

run(args.input, args.output)