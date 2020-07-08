import argparse
import colorbar
import os

parser = argparse.ArgumentParser()

parser.add_argument('-o', '--other', nargs = '?', type = int, default = 99)

parser.add_argument('-m', '--maximum', nargs = '?', type = int, default = 8)

args = parser.parse_args()

print('Creating file with language bar for current directory...')

colorbar.draw_statistics(args.other, args.maximum)
print(f'Completed process, image can be found at {os.getcwd()}/output.svg!')