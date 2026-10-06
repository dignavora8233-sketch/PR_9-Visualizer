import pandas as pd
import numpy as np


class SalesAnalyzer:

    def __init__(self):
        self.data = None

    # Load CSV
    def load_data(self, file_path):

        self.data = pd.read_csv(file_path)

        print("\nDataset loaded successfully!")
        print("Rows:", len(self.data))
        print("Columns:", len(self.data.columns))

    # Check dataset
    def check_data(self):

        if self.data is None:
            print("\nPlease load dataset first.")
            return False

        return True

    # Explore Data
    def explore_data(self):

        if not self.check_data():
            return

        while True:

            print("\n===== EXPLORE DATA =====")
            print("1. First 5 Rows")
            print("2. Last 5 Rows")
            print("3. Column Names")
            print("4. Data Types")
            print("5. Basic Information")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(self.data.head())

            elif choice == "2":
                print(self.data.tail())

            elif choice == "3":
                print(self.data.columns.tolist())

            elif choice == "4":
                print(self.data.dtypes)

            elif choice == "5":
                print(self.data.info())

            elif choice == "6":
                break

            else:
                print("Invalid choice.")

    # DataFrame Operations
    def dataframe_operations(self):

        if not self.check_data():
            return

        while True:

            print("\n===== DATAFRAME OPERATIONS =====")
            print("1. Show Data")
            print("2. Search Product")
            print("3. Sort by Sales")
            print("4. Filter Sales")
            print("5. NumPy Operations")
            print("6. Pivot Table")
            print("7. Split Data")
            print("8. Back")

            choice = input("Enter your choice: ")

            if choice == "1":

                print(self.data)

            elif choice == "2":

                name = input("Enter product name: ")

                result = self.data[
                    self.data["Product"].str.contains(name, case=False)
                ]

                print(result)

            elif choice == "3":

                result = self.data.sort_values("Sales", ascending=False)

                print(result)

            elif choice == "4":

                value = float(input("Enter minimum sales: "))

                result = self.data[self.data["Sales"] >= value]

                print(result)

            elif choice == "5":

                numbers = self.data["Sales"].to_numpy()

                print("\nSales Array:")
                print(numbers)

                print("Total:", np.sum(numbers))
                print("Average:", np.mean(numbers))
                print("Maximum:", np.max(numbers))
                print("Minimum:", np.min(numbers))

            elif choice == "6":

                table = pd.pivot_table(
                    self.data,
                    values="Sales",
                    index="Region",
                    aggfunc="sum"
                )

                print(table)

            elif choice == "7":

                print("\n--- First Part ---")
                print(self.data.iloc[:4])

                print("\n--- Second Part ---")
                print(self.data.iloc[4:])

            elif choice == "8":
                break

            else:
                print("Invalid choice.")

    # Missing Data
    def missing_data(self):

        if not self.check_data():
            return

        while True:

            print("\n===== HANDLE MISSING DATA =====")
            print("1. Show Missing Rows")
            print("2. Fill Numeric Missing Values")
            print("3. Drop Missing Rows")
            print("4. Replace Missing Values")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "1":

                missing = self.data[self.data.isnull().any(axis=1)]

                print(missing)

            elif choice == "2":

                numeric = self.data.select_dtypes(include=np.number)

                self.data[numeric.columns] = numeric.fillna(
                    numeric.mean()
                )

                print("Missing numeric values filled.")

            elif choice == "3":

                self.data.dropna(inplace=True)

                print("Missing rows removed.")

            elif choice == "4":

                value = input("Enter replacement value: ")

                self.data.fillna(value, inplace=True)

                print("Missing values replaced.")

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

    # Statistics
    def statistics(self):

        if not self.check_data():
            return

        print("\n===== DESCRIPTIVE STATISTICS =====")

        print(self.data.describe())

        print("\nTotal Sales:",
              self.data["Sales"].sum())

        print("Average Sales:",
              self.data["Sales"].mean())

        print("Highest Sales:",
              self.data["Sales"].max())

        print("Lowest Sales:",
              self.data["Sales"].min())