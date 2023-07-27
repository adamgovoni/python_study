# practice for interacting, creating, updating csv files via python
# the following is from 'pythonspot.com/files-spreadsheets-csv/'
# IMPORTANT: the articel is from python2 so there has been some modifications to function for python3
import csv

# creates a csv file with the included data in rows
# the original article has 'wb' instead of just 'w'.  This caused a byte string error in python3
with open('persons.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['Name', 'Profession'])
	filewriter.writerow(['Derek', 'Software Developer'])
	filewriter.writerow(['Steve', 'Software Developer'])
	filewriter.writerow(['Paul', 'Manager'])

# to read a csv file into the terminal
# open file
with open('persons.csv', 'r') as f:
	reader = csv.reader(f)

	# read file row by row
	for row in reader:
		print(row)

# instead of printing the information from a csv to terminal you can add it to a list
# in this example each column will be saved in a seperate list
# create list holders for our date
names = []
jobs = []

# open file
with open('persons.csv', 'r') as f:
	reader = csv.reader(f)

	# create a counter to move the reader down the rows
	rowNr = 0
	
	# read file row by row
	for row in reader:
	# we want to skip the header rown hence beginning at rownr >= 1
		if rowNr == 1:
			names.append(row[0])
			jobs.append(row[1])

		else:
			rowNr = 1

# Print data
print(names)
print(jobs)
