# Create a shoppinglist with Python
# First we set a variable with the name shoppinglist
shoppinglist = []

# Define  the add_item function
def add_item():
# Ask user for input    
    item = input("Please insert the article you want to add to your shoppinglist: ")
    print(f"You want to buy {item}") 
    if item == '':
        None
    else:
        shoppinglist.append(item)
add_item()
print(shoppinglist)
def show_shoppinglist():
    if shoppinglist: 
        print("Your Shoppinglist")
    else:
        print("Your Shoppinglist is empty")
show_shoppinglist()
for item in shoppinglist:
    print(item)
show_shoppinglist()    
