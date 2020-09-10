expense_list = []
split_expenses = 0

#First user value is name, second value is current money paid in
user_dictionary = {
    1: ["Kain", 0],
    2: ["Nick", 0]
}



number_of_users = len(user_dictionary)

expense_category_dict = {
    1: "Food",
    2: "Utilities",
    3: "Household goods",
    4: "Luxuries"

}
def user_select():
    print("""\nWelcome to the 32 Rose Street budget app!
    Select a user:
        1. Kain
        2. Nick\n"""   )

    user_selection = int(input("Input: "))
    
    if  user_selection == 1 or user_selection == 2:
        
        global user
        user = user_dictionary[user_selection][0]
        main_menu(user)
    else:
        print("Invalid selection")
        user_select()




def print_expense_list():
    for i in range(len(expense_list)):
        print(expense_list[i])


def print_total_cost():
    sum = 0.0
    for i in range(len(expense_list)):
        sum += expense_list[i][2]
    print("Total cost of expenses: $", sum)
    return sum

def print_paid_in_by_user():
    print("Paid in of total expenses:")
    for user in user_dictionary:
        paid = 0.0
        for i in range(len(expense_list)):
            if expense_list[i][0] == user_dictionary[user][0]:
                paid += expense_list[i][2]
        print(user_dictionary[user][0] + ": $", paid)

def print_debt_owed():
    for user in user_dictionary:
        paid = 0.0
        for i in range(len(expense_list)):
            if expense_list[i][0] == user_dictionary[user][0]:
                paid += expense_list[i][2]
        user_dictionary[user][1] = paid
        if paid < split_expenses:
            print(user_dictionary[user][0] + " owes", (split_expenses - user_dictionary[user][1]))






def print_financial_overview():
    sum = print_total_cost()
    global split_expenses
    split_expenses = sum / number_of_users
    print("Total expenses divided by", number_of_users, "users =", split_expenses)

    print_paid_in_by_user()

    print_debt_owed()



def enter_household_expense(user):
    new_expense = []
    print("\nSelect expense category:")
    for i in range(len(expense_category_dict)):
        print(i+1, ": ", expense_category_dict[i+1])

    try:
        selection = int(input("\nInput: "))
        category = expense_category_dict[selection]

    except:
        print("Bad selection.")
        enter_household_expense()

    print(category + " selected. ")
    cost = float(input("Cost of expense: $"))

    date = input("Date of expense: ")

    memo = input("Memo(optional): ")

    new_expense = [user, category, cost, date, memo]

    print("Review entry: \n", new_expense)

    submit = input("Submit? Y/N: ")
    if submit.lower() == "y":
        add_expense(user, category, cost, date, memo)
        print("Expense submitted, returning to main menu\n")
        main_menu(user)
    else:
        print("Operation canceled, returning to main menu\n")
        main_menu(user)






def add_expense(user, category, cost, date, memo, ):
    expense_list.append([user, category, cost, date, memo])

def total_cost():
    sum = 0
    for i in range(len(expense_list)):
        sum += expense_list[i][2]
    return sum

def print_command_list():
    print("""
    1. Enter a household expense
    2. View all expenses
    3. View cost total
    4. Financial overview
    5. Pay personal balance
    6. Change user\n""")






def main_menu(user):


    print("\nHello, " + user + ". Please select a command:")
    print_command_list()

    #try:
    command = int(input("Input: "))
    if command == 1:
            print("This is running")
            enter_household_expense(user)
    elif command == 2:
        print_expense_list()
    elif command == 3:
        print_total_cost()
    elif command == 4:
        print_financial_overview()
    elif command == 6:
        user_select()
    else:
        print("Invalid command")

    input("Press Enter to return to main menu")
    main_menu(user)




add_expense("Kain", "Food", 10.00, "10/10/2020", "memo")
add_expense("Nick", "Utilities", 20.00, "10/08/2020", "electricity")
user_select()

