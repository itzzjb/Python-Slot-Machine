# We can import modules for python files
# We need to import the random module to generate random slot machine values
import random

# We can use constants to store the values that we will use in the program that will not be changed
# Constants are written in all capital letters
# This will also give the ability for us to change the values in the machines...
# ...and the program will adapt to them automatically
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Defining the number of rows and columns in the slot machine
ROWS = 3
COLS = 3

# Python dictionaries are used to store data values in key:value pairs
# We can use a dictionary to store the symbols and the number of each symbols in the slot machine
# We use curly braces to define a dictionary
symbol_count = {
    # symbol: count
    "A": 2,  # Every single reel we have 2 A's
    "B": 4,  # Every single reel we have 4 B's
    "C": 6,  # Every single reel we have 6 C's
    "D": 8  # Every single reel we have 8 D's
}

# We can create another dictionary to store the multiplier values for the symbols
symbol_value = {
    # symbol: value
    "A": 5,  # A is worth 5 multiplier points
    "B": 4,  # B is worth 4 multiplier points
    "C": 3,  # C is worth 3 multiplier points
    "D": 2  # D is worth 2 multiplier points
}


# Now we need a function to check the winning
def check_winning(columns, lines, bet, values):
    # We use this variable to store the total winnings
    winnings = 0
    # We use this list to get the values of winning lines
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        # We can have an else statement for a for loop as well
        # It will only run if the for loop completes without a break
        else:
            winnings += values[symbol] * bet
            # We need to add a 1 because line is an index
            winning_lines.append(line + 1)

    # We can return two values like this
    return winnings, winning_lines


# Now we need to generate outcome of the slot machine using the symbols and the number of each symbols
def get_slot_machine_spin(rows, cols, symbols):
    # Getting all the values in the dictionary to a list
    all_symbols = []

    for symbol, count in symbols.items():
        # We can use an anonymous variable "_" here
        # We use it when we don't need the value of the variable
        # Used when you want to loop through something, but you don't care about the interation value
        for _ in range(count):
            all_symbols.append(symbol)

    # This is a nested list
    # Normally in nested list the inner list is the row and the outer list is the column
    # But in this case, the inner list is the column and the outer list is the columns

    columns = []

    # Generating columns for every single column we have ...
    for _ in range(cols):
        column = []

        # We need to add : inbetween the square brackets.
        # This is called the slicing operator
        # This will create a new list with the same values as the original list
        # This is done to avoid changing the original list
        # Without the slicing operator, the original list will be changed when we change the new list
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # We can use random.choice() to get a random value from a list
            value = random.choice(current_symbols)
            # We need to remove the value we chose from the current_symbols list
            # Finds the first instance of the value same as the value in the list and removes it
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


# We need to define a function to print the slot machine values in the console
# columns = [ [A, B, C], [D, A, B], [C, D, A] ]
# [ A, B, C ]
# [ D, A, B ]
# [ C, D, A ]

# There are the 3 different columns in the slot machine
# The actual rows will be like
# A D C
# B A D
# C B A

# This operation is called transposing a matrix
def print_slot_machine(columns):
    # len(columns) will give the number of symbols per column in the slot machine
    for row in range(len(columns[0])):
        # This way you can iterate through the values in a list and get the values
        # for column in columns:
        # We can add enumerate() function to get the index and the value of the list
        for i, column in enumerate(columns):
            # We need to check if we are at the last column
            # So we can avoid adding the "|" at the end of the row
            # end -> Tells the print() function what to print at the end of the string
            # by default it is "\n" which is a new line
            # because of this when we use print() it will print the next print() in the next line
            # We can chane the end value to "" of other value to print in same line.
            if i == len(columns) - 1:
                print(column[row], end="")
            else:
                print(column[row], end=" | ")
        # We can have a empty print() to add a new line
        # This is same as print(end="\n")
        print()


# We can start from getting the data from the user
# This function collects user input and get the deposit from the user
def deposit():
    # True and False should start with capital letter
    while True:
        # By adding a string inside input() function, we can show the message to the user
        amount = input("What would you like to deposit? $ ")
        # We need to check whether the user entered a number or not
        # Python String isdigit() method returns “True” if all characters in the string are digits
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                # break the while loop if the user entered a valid number
                # brings down to return amount
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount


# We normally use snake_case for function names
# This function will get the number of lines the user wants to bet on
def get_number_of_lines():
    while True:
        # We converted the MAX_LINES to string, so we can concatenate it with the string
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) + ") ? ")
        if lines.isdigit():
            lines = int(lines)
            # We can combine the two conditions into one without using "and" keyword
            # Used to check if a number is between two numbers
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 and", MAX_LINES)
        else:
            print("Please enter a number")
    return lines


def get_bet():
    while True:
        bet = input("Enter the amount to bet on each line (" + str(MIN_BET) + " - " + str(MAX_BET) + ") ? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                # We can use f front of a string to add the variables inside the string
                # This is called f-string
                # The values inside the curly races will be converted to string if it can be converted
                # $ -> is here to indicate currency dollar
                print(f"Please enter a number between ${MIN_BET} = ${MAX_BET}")
        else:
            print("Please enter a number")
    return bet


# We can have a function to represent the game as a whole because game must be playable multiple times
# We can call it a spin
# balance is not included here
def spin(balance):
    # This will get the deposit from the user
    lines = get_number_of_lines()  # This will get the deposit from the user

    # This will get the bet per line from the user
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print("You don't have enough balance to bet on", lines, "lines with", bet, "on each line")
            print("Your balance is", balance)
            print("Total bet is", total_bet)
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${bet * lines}")

    # We can use the get_slot_machine_spin() function to get the slot machine values
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    # We can use the check_winning() function to check the winnings and winning lines
    # We can retrieve multiple values from a function by using multiple variables like this
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won $ {winnings}")
    # We can use * to unpack the list and print the values in the list
    # This is call the spat/unpack operator
    print("You won on lines: ", *winning_lines)

    # We need to get a return value to identify how much they win or lose per game
    return winnings - total_bet


# We can put the program in a main function so if we end our program, we can call this again to rerun the program
# Then when the user wants to play again, we can call this function again
def main():
    # This will get the deposit from the user
    balance = deposit()

    # We can write a while loop to keep the game running
    while True:
        print()
        print(f"Your current balance is ${balance}")
        # We don't need to assign a variable to get the input because we don't care about the input
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break

        # We are passing the previous balance and calling the spin function...
        # ...while getting the new balance from adding the win of loss from this spin
        # This happens after the execution of the current spin
        balance += spin(balance)

    print(f"Your final balance is ${balance}")


# Calling the main function to run the program
main()
