import tkinter as tk
import csv
from tkinter import messagebox

def on_new_data():
	# function to handle the "New data" button click
	
	# add your logic here for what should happen when the button is clicked
	def write_to_csv(filename, data):

		# open the csv file in write mode and append the data to it
		with open(filename, 'a', newline='') as csvfile:
			csv_writer = csv.writer(csvfile)
			csv_writer.writerow(data)

		confirmation = "Data has been written to the CSV file."
		
		# text box cleared for new data
		text_box.delete(1.0, tk.END)
		text_box.insert(tk.END, confirmation)

	file_name = "data.csv"
	
	# ask the user for input
	user_data = input_box.get().split(',')

	# clear the input box
	input_var.set('')
	write_to_csv(file_name, user_data)
	

def on_show_data():
	# function to handle the "Show data" button click

	# add your logic here for what should happen when the button is clicked
	# to read a csv file
	# open file
	with open('data.csv', 'r') as f:
		reader = csv.reader(f)

		# clear text box for new data
		text_box.delete(1.0, tk.END)

		# read file row by row
		for row in reader:
			text_box.insert(tk.END, row)

	# displayed in terminal that the button was clicked
	show_confirmation= "Show data button clicked!"
	text_box.insert(tk.END, show_confirmation)

if __name__ == "__main__":
	# create the main window
	root = tk.Tk()
	root.title("Button CSV Example")
	root.geometry("400x300")
	
	# create an input box
	input_var = tk.StringVar()
	input_box = tk.Entry(root, textvariable=input_var)
	input_box.pack(padx=10, pady=10)
	
	# create the "New Data" button
	new_data_button = tk.Button(root, text="New Data", command=on_new_data)
	new_data_button.pack(pady=10)
	
	# create the "Show Data" button
	show_data_button = tk.Button(root, text="Show Data", command=on_show_data)
	show_data_button.pack(pady=10)

	# create text box
	text_box = tk.Text(root, height=10, width=50)
	text_box.pack(pady=10)

	# start the tkinter main loop
	root.mainloop()
