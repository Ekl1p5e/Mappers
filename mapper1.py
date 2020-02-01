#!/usr/bin/env python
# Be sure the indentation is identical and also be sure the line above this is on the first line
# Maps file to the format [month, country, customerID, spent]

import sys
import csv
 
def main(argv):
  # Read first line
  line = sys.stdin.readline()
  
  # Loop over csv
  for row in csv.reader(iter(sys.stdin.readline, '')):
    invoiceNo = str(row[0])
    customerID = str(row[6])
	
	# Check that invoice number does not begin with C and there is a customer id value
    if!invoiceNo.startswith('C') & not customerID):
	  # CSV Columns [0:InvoiceNo, 1:StockCode, 2:Description, 3:Quantity, 4:InvoiceDate, 5:UnitPrice, 6:CustomerID, 7:Country]
	  country = str(row[7])
	  spent = int(row[3]) * float(row[5])
	  
	  # Split by forward slash and get first entry
	  month = str(row[4]).split('/')[0]
	  
	  # Print comma-separated values
	  print([month, country].join("-") + '\t' + [customerID, spent].join("-"))

# Note there are two underscores around name and main
if __name__ == "__main__":
  main(sys.argv)