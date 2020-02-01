#!/usr/bin/env python
# Be sure the indentation is correct and also be sure the line above this is on the first line
 
import sys
 
def main(argv):
  # Initialize variables
  current_word = None
  current_count = 0
  word = None
  
  # Loop through lines of the standard input
  for line in sys.stdin:
    # Trim line
    line = line.strip()
	
	# Split line by tab
    word, count = line.split('\t', 1)
	
	# Make the count an integer
    count = int(count)
	
	# If current word is the same as word of current line, increment, else reprint and change current word
    if current_word == word:
      current_count += count
    else:
	  # If current word is not none, reprint
      if current_word:
        print('%s\t%s' % (current_word, current_count))
      current_count = count
      current_word = word

  # 
  if current_word == word:
    print('%s\t%s' % (current_word, current_count))

# Note there are two underscores around name and main
if __name__ == "__main__":
  main(sys.argv)