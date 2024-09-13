import database

MENU_PROMPT = """
 --- Welcome to Coffee Bean App! ---
Please choose one of the following options:
1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Updae a bean's rating or preparation method
6) Delete a bean
7) Exit
Your selection:
"""

def menu():
    # Connect with the database
    connection = database.connect()
    database.create_tables(connection)

    while (user_input :=input(MENU_PROMPT)) != 5:
        if user_input == "1":
            prompt_add_new_bean(connection)
        elif user_input == "2":
            prompt_see_all_beans(connection)
        elif user_input == "3":
            prompt_find_bean(connection)
        elif user_input == "4":
            prompt_find_best_bean(connection)
        elif user_input == "5":
            prompt_update_bean(connection)
        elif user_input == "6":
            prompt_delete_bean(connection)
        elif user_input == "7":
            return
        else:
            print("Invalid input, please try again!")

def prompt_add_new_bean(connection):
    name = input("Enter bean name: ")
    method = input("Enter how you have prepared it: ")
    rating = int(input("Enter your rating score (0-5): "))
    database.add_bean(connection, name, method, rating)

def prompt_see_all_beans(connection):
    beans = database.get_all_beans(connection)
    for bean in beans:
        print(f"{bean[0]}. {bean[1]}, {bean[2]}, {bean[3]}")

def prompt_find_bean(connection):
    name = input("Enter bean name to find: ")
    beans = database.get_beans_by_name(connection, name)
    for bean in beans:
        print(f"{bean[0]}. {bean[1]} {bean[2]} {bean[3]}")

def prompt_find_best_bean(connection):
    name = input("Enter bean name to find best preparation method: ")
    best_method = database.get_best_preparation_for_bean(connection, name)
    print(f"The best preparation method for {name} is: {best_method}")

def prompt_update_bean(connection):
    name = input("Enter the name of the bean you'd like to update: ")
    bean_id = int(input("Enter the ID of the bean you'd like to update: "))
    new_name = input("Enter bean name: ")
    new_method = input("Enter how you have prepared it: ")
    new_rating = int(input("Enter your rating score (0-5): "))
    database.update_bean(connection, bean_id, new_name, new_method, new_rating)
    print("Bean updated successfully.")

def prompt_delete_bean(connection):
    name = input("Enter the name of the bean to delete: ")
    bean_id = int(input("Enter the id of the bean you'd like to delete: "))
    database.delete_bean(connection, bean_id)
    print("Bean deleted successfully.")


if __name__=="__main__":
    menu()