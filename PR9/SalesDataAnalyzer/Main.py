from file_operations import create_csv
from analyzer import SalesAnalyzer
from visualization import DataVisualizer


# Create CSV automatically
file_path = create_csv()

# Create analyzer object
analyzer = SalesAnalyzer()

while True:

    print("\n================================")
    print("       SALES DATA ANALYZER")
    print("================================")

    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    # Load Dataset
    if choice == "1":

        analyzer.load_data(file_path)

    # Explore Data
    elif choice == "2":

        analyzer.explore_data()

    # DataFrame Operations
    elif choice == "3":

        analyzer.dataframe_operations()

    # Missing Data
    elif choice == "4":

        analyzer.missing_data()

    # Statistics
    elif choice == "5":

        analyzer.statistics()

    # Visualization
    elif choice == "6":

        if analyzer.check_data():

            visualizer = DataVisualizer(
                analyzer.data
            )

            visualizer.menu()

            # Keep visualizer for saving
            analyzer.visualizer = visualizer

    # Save Visualization
    elif choice == "7":

        if hasattr(analyzer, "visualizer"):

            analyzer.visualizer.save_current_plot()

        else:

            print("\nPlease create a visualization first.")

    # Exit
    elif choice == "8":

        print("\nThank you for using Sales Data Analyzer!")

        break

    else:

        print("\nInvalid choice. Please try again.")