# Create a shoppinglist with Python
# First we set a variable with the name shoppinglist
shoppinglist = []

# Define  the add_item function
def add_item():
# Ask user for input    
    item = input("Please insert the article you want to add to your shoppinglist: ")
    print(f"You want to buy {item}") 
    shoppinglist.append(item)

add_item()