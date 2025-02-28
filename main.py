#!/usr/bin/env python3
# Line 1 adds shebang to make it work like a shell script 
import argparse

def main():
    print("This is my first IGVC assingment regarding argparse.")
    parser = argparse.ArgumentParser(description="This is an argparse")
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    print(args)

if __name__=="__main__":
    main()



