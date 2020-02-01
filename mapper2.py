#!/usr/bin/env python
# Be sure the indentation is identical and also be sure the line above this is on the first line
 
import sys
import re
 
def main(argv):
  # Read first line
  line = sys.stdin.readline()
  input = ['a', 'e', 'i', 'o', 'u', 'y']
  
  # Loop through lines until end
  while line:
    # Loop through WORDS of line
    for word in line.split():
	  if length(word) > 0:
	    # Filter vowels
		vowelless = ''.join(sorted([c for c in input]))
	  
	    # Print the WORD with an initial count of 1
        print(vowelless+"\t"+"1")
	  
	# Read line
    line = sys.stdin.readline()

# Note there are two underscores around name and main
if __name__ == "__main__":
  main(sys.argv)