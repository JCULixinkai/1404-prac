# electricity_bill.py
"""Function estimate_electricity_bill:
Print "Electricity bill estimator"
    Input cents_per_kwh as float from user
    Input daily_use_kwh as float from user
    Input billing_days as integer from user
    Set estimated_bill to (cents_per_kwh / 100) * daily_use_kwh * billing_days
    Print "Estimated bill: $" followed by estimated_bill formatted to 2 decimal places
    If this script is being run directly:
    Call estimate_electricity_bill function"""


def estimate_electricity_bill():
    print("Electricity bill estimator")
    cents_per_kwh = float(input("Enter cents per kWh: "))
    daily_use_kwh = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))

    estimated_bill = (cents_per_kwh / 100) * daily_use_kwh * billing_days
    print(f"Estimated bill: ${estimated_bill:.2f}")


if __name__ == "__main__":
    estimate_electricity_bill()

# electricity_bill.py

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def estimate_electricity_bill_with_tariff():
    print("Electricity bill estimator 2.0")
    tariff = input("Which tariff? 11 or 31: ")

    if tariff == "11":
        cents_per_kwh = TARIFF_11 * 100
    elif tariff == "31":
        cents_per_kwh = TARIFF_31 * 100
    else:
        print("Invalid tariff choice.")
        return

    daily_use_kwh = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))

    estimated_bill = (cents_per_kwh / 100) * daily_use_kwh * billing_days
    print(f"Estimated bill: ${estimated_bill:.2f}")


if __name__ == "__main__":
    estimate_electricity_bill_with_tariff()

# sequences.py
"""# sequences.py

Function show_even_numbers(x, y):
    Print "Even numbers from", x, "to", y
    For each i from x to y:
        If i is even:
            Print i, separated by a space
    Print a new line

Function show_odd_numbers(x, y):
    Print "Odd numbers from", x, "to", y
    For each i from x to y:
        If i is odd:
            Print i, separated by a space
    Print a new line

Function show_squares(x, y):
    Print "Squares of numbers from", x, "to", y
    For each i from x to y:
        Print i squared, separated by a space
    Print a new line

Function main:
    Print "Number sequence generator"
    Input x as integer from user
    Input y as integer from user

    While True:
        Print a new line
        Print "Menu:"
        Print "1. Show the even numbers from x to y"
        Print "2. Show the odd numbers from x to y"
        Print "3. Show the squares of the numbers from x to y"
        Print "4. Exit the program"

        Input choice from user

        If choice is "1":
            Call show_even_numbers(x, y)
        Else If choice is "2":
            Call show_odd_numbers(x, y)
        Else If choice is "3":
            Call show_squares(x, y)
        Else If choice is "4":
            Print "Exiting the program."
            Break the loop
        Else:
            Print "Invalid choice. Please try again."

If this script is being run directly:
    Call main function
"""


def show_even_numbers(x, y):
    print("Even numbers from", x, "to", y)
    for i in range(x, y + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()


def show_odd_numbers(x, y):
    print("Odd numbers from", x, "to", y)
    for i in range(x, y + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()


def show_squares(x, y):
    print("Squares of numbers from", x, "to", y)
    for i in range(x, y + 1):
        print(i * i, end=" ")
    print()


def main():
    print("Number sequence generator")
    x = int(input("Enter the start number (x): "))
    y = int(input("Enter the end number (y): "))

    while True:
        print("\nMenu:")
        print("1. Show the even numbers from x to y")
        print("2. Show the odd numbers from x to y")
        print("3. Show the squares of the numbers from x to y")
        print("4. Exit the program")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_even_numbers(x, y)
        elif choice == "2":
            show_odd_numbers(x, y)
        elif choice == "3":
            show_squares(x, y)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    while True:
        sales = float(input("Enter sales: $"))
        if sales < 0:
            break
        if sales < 1000:
            bonus = sales * 0.10
        else:
            bonus = sales * 0.15
        print(f"Sales: ${sales:.2f}, Bonus: ${bonus:.2f}")

    print("Negative sales entered, program terminated.")


if __name__ == "__main__":
    main()

# loops.py

# Odd numbers between 1 and 20
print("Odd numbers between 1 and 20:")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Count in 10s from 0 to 100
print("Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. Count down from 20 to 1
print("Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Print n stars on one line
n = int(input("Number of stars: "))
print("Print n stars:")
for i in range(n):
    print('*', end='')
print()

# d. Print n lines of increasing stars
print("Print n lines of increasing stars:")
for i in range(1, n + 1):
    print('*' * i)

# broken_score.py

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")


# menu_program.py

def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


def main():
    name = input("Enter name: ")
    choice = ''

    while choice != 'Q':
        display_menu()
        choice = input(">>> ").upper()

        if choice == 'H':
            print(f"Hello {name}")
        elif choice == 'G':
            print(f"Goodbye {name}")
        elif choice != 'Q':
            print("Invalid choice")

    print("Finished.")


if __name__ == "__main__":
    main()


# shop_calculator.py

def main():
    total_price = 0
    num_items = int(input("Number of items: "))

    while num_items < 0:
        print("Invalid number of items!")
        num_items = int(input("Number of items: "))

    for _ in range(num_items):
        price = float(input("Price of item: "))
        total_price += price

    if total_price > 100:
        total_price *= 0.90

    print(f"Total price for {num_items} items is ${total_price:.2f}")


if __name__ == "__main__":
    main()
