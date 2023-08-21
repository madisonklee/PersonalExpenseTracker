import sqlite3
import datetime

conn=sqlite3.connect("expenses.db")
cur=conn.cursor()       # be our basis for ind actions

while True:
    print("Select an option:")
    print("1. Enter a new expense")
    print("2. View expenses summary")

    choice=int(input())

    if choice==1:
        # need info from user
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        description = input("Enter the description of the expense: ")

        # add a category or give existing category
        # use cursor to execute the following statement
        cur.execute("SELECT DISTINCT category FROM expenses")

        # get results
        categories = cur.fetchall()

        # iterate over categories that we have and enumerate them
        print("Select a category by number: ")
        for idx, category in enumerate(categories):
            print(f"{idx + 1}. {category[0]}")  # creates memu
        print(f"{len(categories) + 1}. Create a new category")      # add an additional object that adds new category

        # what the user wants to do
        category_choice = input()
        if category_choice == len(categories) + 1:   # create new category
            category = input("Enter the new category name: ")
        else:
            category = categories[category_choice-1][0]

        price = input("Enter the price of the expense: ")
        cur.execute("INSERT INTO expenses(Date, description, category, price) VALUES (?, ?, ?, ?)", (date, description, category, price))

        conn.commit()

    elif choice==2:
        print("Select an option:")
        print("1. View all expenses")
        print("2. View monthly expenses by category")

        view_choice =int(input())

        if view_choice==1:
            cur.execute("SELECT * FROM expenses")
            expenses = cur.fetchall()
            for exp in expenses:
                print(exp)

        elif view_choice==2:
            month = input("Enter the month (MM): ")
            year = input("Enter the year (YYYY): ")
            cur.execute("SELECT category, SUM(price) FROM expenses WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ? GROUP BY category", (month, year))
            expenses = cur.fetchall()
            for exp in expenses:
                print(f"Category: {exp[0]}, Total: {exp[1]}")
        else:
            exit()

    else:
        exit()

    repeat = input("Would you like to do something else (y/n)? \n")
    if repeat.lower() != "y":
        break

conn.close()