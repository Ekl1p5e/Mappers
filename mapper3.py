#!/usr/bin/env python
# Be sure the indentation is identical and also be sure the line above this is on the first line
 
import sys
import re
 
def main(argv):
  # Read first line
  line = sys.stdin.readline()
  
  # Create a regex pattern for WORDS
  pattern = re.compile("[a-zA-Z0-9]+")
  
  # Loop through lines until end
  while line:
    # Loop through WORDS of line
    for word in pattern.findall(line):
	  # Print the WORD with an initial count of 1
      print(word+"\t"+"1")
	  
	# Read line
    line = sys.stdin.readline()

# Note there are two underscores around name and main
if __name__ == "__main__":
  main(sys.argv)