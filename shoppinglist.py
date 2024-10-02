# Create a shoppinglist with Python
# First we set a variable with the name shoppinglist
shoppinglist = []

# Add_item
# First we ask the user for input

def add_item():
    item = input("Please insert the article you want to add to your shoppinglist: ")
    print(f"You want to buy {item}") 
    shoppinglist.append(item)

add_item()