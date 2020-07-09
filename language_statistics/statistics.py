#!/usr/bin/env python3

import argparse
from language_statistics import colorbar
import os

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-o",
        "--other",
        nargs="?",
        type=float,
        default=1,
        help="Files below this percentage of the directory as a whole will be labeled as other.",
    )

    parser.add_argument(
        "-m",
        "--maximum",
        nargs="?",
        type=int,
        default=8,
        help="Number of different languages to display before setting the rest to 'Other'",
    )

    args = parser.parse_args()

    print("Creating file with language bar for current directory...")

    colorbar.draw_statistics(args.other, args.maximum)
    print(f"Completed process, image can be found at {os.getcwd()}/output.svg!")