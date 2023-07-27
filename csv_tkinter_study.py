import tkinter as tk
import csv

def on_new_data():
	# function to handle the "New data" button click
	
	# add your logic here for what should happen when the button is clicked
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
	# displayed in terminal that the button was clicked
	print("New data button clicked!")

def on_show_data():
	# function to handle the "Show data" button click

	# add your logic here for what should happen when the button is clicked

	# displayed in terminal that the button was clicked
	print("Show data button clicked!")

if __name__ == "__main__":
	# create the main window
	root = tk.Tk()
	root.title("Button CSV Example")

	# create the "New Data" button
	new_data_button = tk.Button(root, text="New Data", command=on_new_data)
	new_data_button.pack(pady=10)

	# create the "Show Data" button
	show_data_button = tk.Button(root, text="Show Data", command=on_show_data)
	show_data_button.pack(pady=10)

	# start the tkinter main loop
	root.mainloop()
