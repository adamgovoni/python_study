import csv

names = []
jobs = []

counter = 0

with open('persons.csv', 'r') as f:
	reader = csv.reader(f)
	
	# read file row by row
	for row in reader:
		
		if counter == 1:
			names.append(row[0])
			jobs.append(row[1])

		else:
			counter = 1

# Print data
print(names)
print(jobs)