#!/usr/bin/env python3
# Line 1 adds shebang to make it work like a shell script 
import argparse
from pathlib import Path # class is pathlib, Path is data type

def main():
    parser = argparse.ArgumentParser(description="This program uses A* to create the optimal path for a car") 
    parser.add_argument('-i', '--input', default = Path("input.yaml"), type = Path) 
    parser.add_argument('-o', '--output', default = Path("output.yaml"), type = Path)
    args = parser.parse_args()
    print(args)

if __name__=="__main__":
    main()