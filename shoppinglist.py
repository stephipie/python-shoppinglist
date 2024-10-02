# Create a shoppinglist with Python
# First we set a variable with the name shoppinglist
shoppinglist = []

# Define  the add_item function
def add_item():
# Ask user for input    
    item = input("Please insert the article you want to add to your shoppinglist: ")
    print(item)
# Check if the shopping list is empty    
    if item == '':
        None
    else:
        shoppinglist.append(item)   #.append is a function to add e.g. items
print(shoppinglist)
# Define a function to show shoppinglist
def show_shoppinglist():
    if shoppinglist:
        print("Your shoppinglist")
        for item in shoppinglist:                   # For-Loop to print every item of my shoppinglist
            print(item) 
    else:
        print("Your shoppinglist is empty")
# While-Loop to keep the programm running 
def main():
    while True:
        print("-----Shoppinglist-----")
        print("1. Add article to your shoppinglist")
        print("2. Show shoppinglist")
        print("3. End the programm")
        choice = int(input("Please choose 1, 2 or 3: "))
        if choice == 1:
            add_item()
        elif choice == 2:
            show_shoppinglist()
        elif choice == 3:
            print("Program is ended! Goodbye, see you soon.")
            break                                                           #while/break loop
        else:
            print("Invalid selection. Please choose 1, 2 or 3.")   
if __name__ == "__main__":
    main()

