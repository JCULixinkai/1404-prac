from guitar import Guitar

def main():
    print("My guitars!")
    name = input("Name: ")
    guitars = []
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
        guitars.append(guitar)
        print(guitar, " added.")
        name = input("\nName: ")

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} (vintage)")
            else:
                print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")
    else:
        print("\nNo guitars :( Quick, go and buy one!")


main()
