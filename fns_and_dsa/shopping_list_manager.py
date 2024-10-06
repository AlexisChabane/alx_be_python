def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the name of the item to add")
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

def remove_item(shopping_list):
    item = input("Enter the name of ther item to remove: ")
    if item in shopping_list.remove(item):
        print(f"{item} has been removed from the list")
    else:
        print(f"{item} is not in the shopping list")

def view_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty")
    else:
        print("\n Shopping List")
        for index, item in enumerate(shopping_list, starts=1):
            print(f"{index}. {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Exiting the Shopping List Manager")
            break
        else:
            print("Invalid choice. Please select a vaild option (1-4). ")