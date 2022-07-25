# =============== Imports ===============
from tabulate import tabulate

# =============== Class & Methods ===============

# Create a Shoe Class 
class Shoe:

    # Initialises the shoe class with the following attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Returns a string representation of a class 
    def __repr__(self):
        return f"{self.country} {self.code} {self.product} {self.cost} {self.quantity}"

    # Returns the country of the shoe
    def get_country(self):
        return self.country
    
    # Returns the shoe code
    def get_code(self): 
        return self.code
    
    # Returns the name of the shoe
    def get_product(self):
        return self.product
    
    # Returns the cost of the shoe
    def get_cost(self):
        return self.cost

    # Return the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # Sets the quantity of the shoe
    def set_quantity(self, restock_qty):
        self.quantity = restock_qty

    def set_cost(self, sale_cost):
        self.cost = sale_cost     

# =============== Functions ===============

# Function for reading data from the text file
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as inventory_file:
            shoe_list.clear
            for line in inventory_file:
                line_list = line.split(",")
                split_quantity = line_list[4].split("\n")
                object_content = Shoe(line_list[0], line_list[1], line_list[2], line_list[3], split_quantity[0])
                shoe_list.append(object_content)
            del shoe_list[0]
    except FileNotFoundError:
        print("Inventory file couldn't be found")

# Create a object with the shoe data and append to the obj list
def capture_shoes():
    new_country = input("Country: ")
    new_code = input("Shoe Code: ")
    new_product = input("Shoe Name: ")
    new_cost = input("Shoe Cost: ")
    new_quantity = input("Shoe Quantity: ")
    new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
    shoe_list.append(new_shoe)

# Iterate over Shoe List and print details from return of __str__
def view_all(shoe_list):
    table = [["Country", "Code", "Product", "Cost", "Quantity", "Value"]]
    
    for shoe in shoe_list:
        country = shoe.get_country()
        code = shoe.get_code()
        product = shoe.get_product()
        cost = shoe.get_cost()
        quantity =  shoe.get_quantity()
        value = get_value(shoe)
    
        temp = [country, code, product, f"R{cost}" , quantity, f"R{value}"]
        table.append(temp)
    
    print(tabulate(table, headers='firstrow', tablefmt='github'))

# Find Shoe with lowest quantity, Request user to add to quantity if he wants
def re_stock(quantity_list):
    min_quantity = min(quantity_list)
    for shoe in shoe_list:
        if int(shoe.quantity) == min_quantity:
            try:
                with open('inventory.txt', 'r+') as inventory_file:
                    for count, line in enumerate(inventory_file):
                        if shoe.code in line:
                            print(f"\nProduct:\t{shoe.product}\nCountry:\t{shoe.country}\nCode:\t\t{shoe.code}\nCost:\t\tR{shoe.cost}\nQuantity:\t{shoe.quantity}")
                            restock_input = input("Restock Amount: ")
                            restock_qty = str(int(restock_input) + int(shoe.quantity))
                            shoe.set_quantity(restock_qty)
                            print(f"{shoe.product} has been restocked.")
            except FileNotFoundError:
                print("Could not locate the file.")

# Search for a shoe from list with shoe code and print it
def search_shoe(code_input):
    for shoe in shoe_list:
        if shoe.code == code_input:
            print(f"\nProduct:\t{shoe.product}\nCountry:\t{shoe.country}\nCode:\t\t{shoe.code}\nCost:\t\tR{shoe.cost}\nQuantity:\t{shoe.quantity}")

# Determine shoe with highest quantity and put up as for sale
def highest_qty(quantity_list):
    max_quantity = max(quantity_list)
    for shoe in shoe_list:
        if int(shoe.quantity) == max_quantity:
            print(f"\nProduct:\t{shoe.product}\nCountry:\t{shoe.country}\nCode:\t\t{shoe.code}\nCost:\t\tR{shoe.cost}\nQuantity:\t{shoe.quantity}")
            sale_cost = input("What is your sales price: ")
            shoe.set_cost(sale_cost)
            print(f"\n{shoe.product} price has been changed to {shoe.cost})")

# Return the value of shoe object
def get_value(shoe):
    return int(shoe.quantity) * int(shoe.cost)

# Function to get the quantity of each item and put them in a list
def quantity():
    quantity_list = []
    for shoe in shoe_list:
        quantity_list.append(int(shoe.get_quantity()))
    return quantity_list

# =============== Main Menu ===============

# List for Shoe Objects
shoe_list = []
user_choice = 0
read_shoes_data()

while user_choice != 6:
    user_choice = int(input("\n1.Search\n2.Capture Shoe\n3.Restock\n4.Highest Stocks\n5.View All\n6.Quit\nSelect: "))
    if user_choice == 1:
        code_input = input("Enter the shoe code: ")
        search_shoe(code_input)
    if user_choice == 2:
        capture_shoes()
    if user_choice == 3:
        re_stock(quantity())
    if user_choice == 4:
        highest_qty(quantity())
    if user_choice == 5:
        view_all(shoe_list)
    if user_choice == 6:
        print("Goodbye")
