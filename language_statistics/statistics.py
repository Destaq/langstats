#!/usr/bin/env python3

import argparse
from language_statistics import colorbar
import os

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t",
        "--type",
        nargs="?",
        default='svg',
        help="Choose whether to export your image as a png or a svg (example: statistics -t svg). Default is png."
    )

    parser.add_argument(
        "-l",
        "--limit",
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

    try:
        print("Creating file with language bar for current directory...")

        colorbar.draw_statistics(args.type, args.limit, args.maximum)
        print(f"Completed process, image can be found at {os.getcwd()}/output.{args.type}!")
    except:
        print("[ERROR] You have entered one or more of your arguments incorrectly!")