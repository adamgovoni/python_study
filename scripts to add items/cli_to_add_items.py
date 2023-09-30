import argparse
import os

def add_item_to_list(item, my_list):
    my_list.append(item)
    print(f"Added '{item}' to the list.")

def save_list_to_file(filename, my_list):
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(item + '\n')

def load_list_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            my_list = [line.strip() for line in file]
    else:
        my_list = []
    return my_list

def main():
    parser = argparse.ArgumentParser(description="CLI for adding items to a list")
    parser.add_argument("item", type=str, help="Item to add to the list")
    args = parser.parse_args()

    filename = "my_list.txt"  # Change the filename as needed

    my_list = load_list_from_file(filename)
    add_item_to_list(args.item, my_list)
    save_list_to_file(filename, my_list)

if __name__ == "__main__":
    main()
