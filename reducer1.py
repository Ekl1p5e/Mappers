#!/usr/bin/env python
# Be sure the indentation is correct and also be sure the line above this is on the first line
# Reduces from [month, country, customerID, spent] to [Month,Country:CustomerID]
import sys
 
def main(argv):
  # Initialize variables
  current_month = None
  current_country = None
  current_customerID = None
  current_spent = 0.0
  
  month = None
  country = None
  customerID = None
  
  # Loop through lines of the standard input
  for line in sys.stdin:
    # Trim line
    line = line.strip()
	
	# Split line by comma
	kv = line.split('\t', 1)
    month, country = kv[0].split('-')
	customerID, spent = kv[1].split('-')
	
	# Make spent a float
    spent = float(spent)
	
	# If current word is the same as word of current line, increment, else reprint and change current word
    if current_month == month & current_country == country:
	  if current_spent < spent:
	    current_spent = spent
		current_month = month
		current_customerID = customerID
		current_country = country
	  else if current_spent == spent:
	    current_customerID = current_customerID + " " + customerID  
    else:
	  # If current word is not none, reprint
      if current_month & current_country:
        print([current_month, current_country].join("-") + '\t' + [current_customerID, current_spent].join("-"))

      current_spent = spent
      current_month = month
	  current_customerID = customerID
      current_country = country

  # Print out all ids
  if current_month == month & current_country == country:
    customerIDs = current_customerID.split()
	for id in customerIDs:
	  print('%s,%s:%s' % (current_month, current_country, id))

# Note there are two underscores around name and main
if __name__ == "__main__":
  main(sys.argv)