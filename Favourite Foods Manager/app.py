# Favourite Food Item Manager
def food_item_manager():
    # List to store favorite food items
    favorite_food_items = []

    while True:
        # Display menu
        print("\n--- Favourite Food Item Manager ---")
        print("1. Add a food item")
        print("2. Remove a food item")
        print("3. Check if a food item is in the list")
        print("4. Show all food items")
        print("5. Exit")

        # Get user choice
        choice = input("Enter your choice (1/2/3/4/5): ")

        # Add a food item
        if choice == '1':
            item = input("Enter the name of the food item to add: ")
            if item not in favorite_food_items:
                favorite_food_items.append(item)
                print(f"'{item}' has been added to your favorite food list.")
            else:
                print(f"'{item}' is already in your favorite food list.")

        # Remove a food item
        elif choice == '2':
            item = input("Enter the name of the food item to remove: ")
            if item in favorite_food_items:
                favorite_food_items.remove(item)
                print(f"'{item}' has been removed from your favorite food list.")
            else:
                print(f"Error: '{item}' is not in your favorite food list.")

        # Check if a food item is in the list
        elif choice == '3':
            item = input("Enter the name of the food item to check: ")
            if item in favorite_food_items:
                print(f"Yes, '{item}' is in your favorite food list.")
            else:
                print(f"No, '{item}' is not in your favorite food list.")

        # Show all food items
        elif choice == '4':
            if favorite_food_items:
                print("Your favorite food items are:")
                for index, food in enumerate(favorite_food_items, 1):
                    print(f"{index}. {food}")
            else:
                print("Your favorite food list is empty.")

        # Exit the program
        elif choice == '5':
            print("Exiting the Favourite Food Item Manager. Goodbye!")
            break

        # Handle invalid input
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")

# Run the food item manager
food_item_manager()