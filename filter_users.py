import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as file:
        return json.load(file)


def filter_users_by_name(users: list, name):
    """ Filters a list of users by name."""
    return [user for user in users if user.get("name").lower() == name.lower()]


def filter_user_by_age(users: list, min_age):
    """ Filters a list of user, returning only those above a certain age."""
    return [user for user in users if user.get('age', 0) >= min_age]

if __name__ == "__main__":
    # Load the user data once at the start
    users_data = load_data("users.json")

    filter_option = input("What would you like to filter by? ('name' or 'age'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filtered_users = filter_users_by_name(users_data, name_to_search)

        print("Filtered users:")
        for user in filtered_users:
            print(user)

    elif filter_option == "age":
        try:
            min_age = int(input("Enter a minimum age to filter users: ").strip())
            filtered_users = filter_user_by_age(users_data, min_age)

            print("Filtered users:")
            for user in filtered_users:
                print(user)
        except ValueError:
            print("Invalid age entered. Please enter a number.")
    else:
        print("Filtering by that option is not yet supported.")