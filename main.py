# We can use constants to store the values that we will use in the program that will not be changed
# Constants are written in all capital letters
# This will also give the ability for us to change the values in the machines...
# ...and the program will adapt to them automatically
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


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


# We can put the program in a main function so if we end our program, we can call this again to rerun the program
# Then when the user wants to play again, we can call this function again
def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${bet * lines}")


main()
