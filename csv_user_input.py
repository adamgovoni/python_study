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