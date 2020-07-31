#!/usr/bin/python3
from sys import argv
from sys import stderr
from os import path

def markDown():

 if __name__ == "__main__":
    if len(argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',file=stderr)
        exit(1)

    if not path.exists(argv[1]):
        print('Missing {}'.format(argv[1]), file=stderr)
        exit(1)
    exit(0)      
        
       
 
markDown()
