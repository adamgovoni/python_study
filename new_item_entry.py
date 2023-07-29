import csv
import tkinter as tk

def new_item():
	# function to handle the "New data" button click
	
	# add your logic here for what should happen when the button is clicked
	def write_to_csv(filename, name, price, stock):

		# open the csv file in write mode and append the data to it
		with open(filename, 'a', newline='') as csvfile:
			csv_writer = csv.writer(csvfile)
			csv_writer.writerow([name, price, stock])

		confirmation = "Data has been written to the CSV file."
		
		# text box cleared for new data
		text_box.delete(1.0, tk.END)
		text_box.insert(tk.END, confirmation)

	file_name = "items.csv"
	
	# ask the user for input
	name = input_box_name.get()
	price = input_box_price.get()
	stock = input_box_stock.get()

	# clear the input boxes
	input_var_name.set('')
	input_var_price.set('')
	input_var_stock.set('')
	write_to_csv(file_name, name, price, stock)

def show_items():
	# function to handle the "Show data" button click

	# add your logic here for what should happen when the button is clicked
	# to read a csv file
	# open file
	with open('items.csv', 'r',newline='') as f:
		reader = csv.reader(f)

		# clear text box for new data
		text_box.delete(1.0, tk.END)

		# read file row by row
		for row in reader:
			name, price, stock = row
            
			# Append each row as a new line to the textbox
			text_box.insert(tk.END, f"Name: {name}\nPrice: {price}\nStock: {stock}\n\n")
		

if __name__ == "__main__":
	# create the main window
	root = tk.Tk()
	root.title("Item Creation")
	root.geometry("400x550")
	root.resizable(0, 0)
	
	# set the size of the columns
	root.columnconfigure(0, weight=0)
	root.columnconfigure(1, weight=3)

	# create input boxes with labels using 'grid' for alignment
	label_name = tk.Label(root, text = "Name")
	label_name.grid(row=0, column=0, sticky=tk.E)
	input_var_name = tk.StringVar()
	input_box_name = tk.Entry(root, textvariable=input_var_name)
	input_box_name.grid(row=0, column=1, sticky=tk.W)
	
	label_price = tk.Label(root, text = "Price")
	label_price.grid(row=1, column=0, sticky=tk.E)
	input_var_price = tk.StringVar()
	input_box_price = tk.Entry(root, textvariable=input_var_price)
	input_box_price.grid(row=1, column=1, sticky=tk.W)

	label_stock = tk.Label(root, text = "Stock")
	label_stock.grid(row=2, column=0, sticky=tk.E)
	input_var_stock = tk.StringVar()
	input_box_stock = tk.Entry(root, textvariable=input_var_stock)
	input_box_stock.grid(row=2, column=1, sticky=tk.W)

	# create the "Submit" button
	new_item_button = tk.Button(root, text="New Items", command=new_item)
	new_item_button.grid(row=4, columnspan=2, sticky=tk.EW)
	
	# create the "Show Items" button
	show_items_button = tk.Button(root, text="Show Items", command=show_items)
	show_items_button.grid(row=5, columnspan=2, sticky=tk.EW)

	# create text boxes
	text_box = tk.Text(root, height=10, width=40)
	text_box.grid(row=6, columnspan=2, sticky=tk.EW)

	# start the tkinter main loop
	root.mainloop()