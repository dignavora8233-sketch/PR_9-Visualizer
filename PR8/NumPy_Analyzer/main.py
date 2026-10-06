from analyzer import NumPyAnalyzer


obj = NumPyAnalyzer()

while True:

    print("\nWelcome to the NumPy Analyzer!")
    print("=" * 40)

    print("1. Create a NumPy Array")
    print("2. Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter")
    print("5. Aggregates and Statistics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        obj.create_array()

    elif choice == "2":
        obj.mathematical_operations()

    elif choice == "3":
        obj.combine_split()

    elif choice == "4":
        obj.search_sort_filter()

    elif choice == "5":
        obj.statistics()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")