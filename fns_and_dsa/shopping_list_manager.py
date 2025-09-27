def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Start with an empty shopping list
    shopping_list = []

    # Keep showing the menu until the user exits
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        # Option 1: Add Item
        if choice == "1":
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")

        # Option 2: Remove Item
        elif choice == "2":
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")

        # Option 3: View List
        elif choice == "3":
            if len(shopping_list) == 0:
                print("Your shopping list is currently empty.")
            else:
                print("Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        # Option 4: Exit
        elif choice == "4":
            print("Goodbye! Thanks for using the Shopping List Manager.")
            break

        # Handle Invalid Input
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()

