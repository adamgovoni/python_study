import csv

def write_to_csv(filename, data):

	# open the csv file in write mode and append the data to it
	with open(filename, 'a', newline='') as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow(data)

	print("Data has been written to the CSV file.")


file_name = "data.csv"
# ask the user for input
user_data = input("Enter your data (comma-separated): ").split(',')
write_to_csv(file_name, user_data)

# to read a csv file into the terminal
# open file
with open('data.csv', 'r') as f:
	reader = csv.reader(f)

	# read file row by row
	for row in reader:
		print(row)

# instead of printing the information from a csv to terminal you can add it to a list
# in this example each column will be saved in a seperate list
# create list holders for our date
items = []

# open file
with open('data.csv', 'r') as f:
	reader = csv.reader(f)

	# create a counter to move the reader down the rows
	rowNr = 0
	
	# read file row by row
	for row in reader:
	# we want to skip the header rown hence beginning at rownr >= 1
		if rowNr == 1:
			items.append(row[0])

		else:
			rowNr = 1

# Print data
print(items)