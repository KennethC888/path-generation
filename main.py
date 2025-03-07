#!/usr/bin/env python3
# Line 1 adds shebang to make it work like a shell script 
import argparse

def main():
    parser = argparse.ArgumentParser(description="Argparse input and output flags") #This program uses A* to create the optimal path for a car
    parser.add_argument('-i', '--input', required = True)
    parser.add_argument('-o', '--output', required = True)
    args = parser.parse_args()
    print(args)

if __name__=="__main__":
    main()