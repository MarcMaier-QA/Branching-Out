import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as file:
        return json.load(file)


def filter_users_by_name(users: list, name):
    """ Filters a list of users by name."""
    return [user for user in users if user.get("name").lower() == name.lower()]


def filter_users_by_age(users: list, min_age):
    """ Filters a list of user, returning only those above a certain age."""
    return [user for user in users if user.get('age', 0) >= min_age]


def filter_users_by_email(users: list, email):
    """Filters a list of users by email address."""
    return [user for user in users if user.get("email").lower() == email.lower()]


def main():
    """Main function to run the user filtering address"""
    users_data = load_data("users.json")

    filter_option = input("What would you like to filter by? ('name', 'age', or 'email'): ").strip().lower()

    filtered_users = []
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filtered_users = filter_users_by_name(users_data, name_to_search)

    elif filter_option == "age":
        try:
            min_age = int(input("Enter a minimum age to filter users: ").strip())
            filtered_users = filter_users_by_age(users_data, min_age)
        except ValueError:
            print("Invalid age entered. Please enter a number.")
            filtered_users = []  # Set to empty list to avoid errors

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filtered_users = filter_users_by_email(users_data, email_to_search)

    else:
        print("Filtering by that option is not yet supported.")

    print("\nFiltered users:")
    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("No users found matching your criteria.")


if __name__ == "__main__":
    main()
