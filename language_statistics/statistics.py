#!/usr/bin/env python3

import argparse
import os

from language_statistics import colorbar


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d",
        "--depth",
        nargs="?",
        default=3,
        type=int,
        help="The depth from the current directory at which files should be read (default 3). A depth of one will only read files in the current directory, a depth of two files in the current directory and those one level below (in subdirs), etc. Slightly affects execution time."
    )

    parser.add_argument(
        "-t",
        "--type",
        nargs="?",
        default='svg',
        help="Choose whether to export your image as a png or a svg (example: statistics -t svg). Default is svg."
    )

    parser.add_argument(
        "-l",
        "--limit",
        nargs="?",
        type=float,
        default=1,
        help="Files below this percentage of the directory as a whole will be labeled as other. Default is 1.",
    )

    parser.add_argument(
        "-m",
        "--maximum",
        nargs="?",
        type=int,
        default=8,
        help="Number of different languages to display before setting the rest to 'Other'. Default is 8.",
    )

    parser.add_argument(
        '-e',
        '--exclude',
        nargs='*',
        default='',
        help='Which extensions to exclude, can select multiple (e.g. statistics -e .py .java .php). Default is none.',
        required=False
    )

    parser.add_argument(
        '-c',
        '--colors',
        nargs='*',
        default='',
        help='List of hex colors to use. Default is none, indicating to use the YAML colors.',
        required=False
    )

    parser.add_argument(
        "-n",
        "--names",
        nargs="*",
        default='',
        help="Which filenames to exclude, can select multiple (e.g. statistics -n Dockerfile Cakefile). Default is "
             "none.",
        required=False
    )

    parser.add_argument(
        "-s",
        "--skip-dirs",
        nargs='*',
        default='',
        help='List of relative directory paths to exclude when generating the color bar.',
        required=False
    )

    args = parser.parse_args()

    print("Creating file with language bar for current directory...")
    colorbar.draw_statistics(args.type, args.limit, args.maximum, args.depth - 1, args.exclude, args.skip_dirs,
                             args.names, args.colors)
    print(f"Completed process, image can be found at {os.getcwd()}/output.{args.type}!")
