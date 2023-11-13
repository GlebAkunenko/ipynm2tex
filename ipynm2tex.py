import argparse
import inspect, os
import sys
from main import run

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

args = argparse.ArgumentParser()
args.add_argument("path", type=str, help="The path to current folder")
args.add_argument("input", type=str, help="The path to the .ipynm file")
args.add_argument("-o", "--output", type=str, default='output', help="The output folder path")

args = args.parse_args()

if args.output == "output":
	args.output = args.path + "/output"

if not os.path.exists(args.path + args.output):
	os.mkdir(args.output)

run(args.input, args.output)