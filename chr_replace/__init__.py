#!/usr/bin/env python3
import argparse
import pandas as pd
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Adds or removes "chr" prefixes from a column of a CSV')
    parser.add_argument('csv', type=Path)
    parser.add_argument('-m', '--mode', choices=['add', 'remove'], help='Whether to add or remove the chr prefix', required=True)
    parser.add_argument('-c', '--column', type=int, help='The column number to modify', required=True)
    parser.add_argument('-d', '--delimiter', help='The delimiter for the input and output CSV file', required=True)
    parser.add_argument('-o', '--output', help='The output CSV', type=Path, required=True)
    parser.add_argument('-t', '--comment', help='Comment format in the input CSV', default='#')

    # Parse args
    args = parser.parse_args()

    # Read CSV
    df = pd.read_csv(args.csv, sep=args.delimiter, comment=args.comment)

    # Decide paramters
    if args.mode == 'add':
        frm = r'(.+)'
        to = r'chr\1'
    elif args.mode == 'remove':
        frm = 'chr'
        to = ''

    # Do the translation
    df.iloc[:, args.column] = df.iloc[:, args.column].astype(str).str.replace(frm, to)

    # Save it
    df.to_csv(args.output, sep=args.delimiter, index=False)

if __name__ == '__main__':
    main()
