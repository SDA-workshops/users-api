from prettytable import PrettyTable

from containers import users, UsersIterator
from db.session import db_session


def main():
    print("Available users:")
    for user in users(db_session):
        print(user)

    users_table = PrettyTable(
        ["id", "first_name", "last_name", "email", "registration_date"]
    )
    users_iterator = iter(UsersIterator(db_session))
    users_table.add_rows(users_iterator)

    print("Available users:")
    print(users_table)


if __name__ == "__main__":
    main()
