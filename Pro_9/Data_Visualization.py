import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesAnalyzer:

    def __init__(self):
        self.data = None

    # Destructor
    def __del__(self):
        print("SalesAnalyzer object deleted.")

    # --------------------------------------------------
    # Load CSV
    # --------------------------------------------------

    def load_data(self, file_path):

        try:
            self.data = pd.read_csv(file_path)

            print("\nDataset loaded successfully!")
            print("Rows:", len(self.data))
            print("Columns:", len(self.data.columns))

        except FileNotFoundError:
            print("\nFile not found.")

        except Exception as e:
            print("\nError:", e)

    # --------------------------------------------------
    # Check Dataset
    # --------------------------------------------------

    def check_data(self):

        if self.data is None:
            print("\nPlease load dataset first.")
            return False

        return True

    # --------------------------------------------------
    # Explore Data
    # --------------------------------------------------

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
                self.data.info()

            elif choice == "6":
                break

            else:
                print("Invalid choice.")

    # --------------------------------------------------
    # Clean Data
    # --------------------------------------------------

    def clean_data(self):

        if not self.check_data():
            return

        while True:

            print("\n===== CLEAN DATA =====")
            print("1. Show Missing Values")
            print("2. Fill Numeric Missing Values")
            print("3. Drop Missing Rows")
            print("4. Remove Duplicate Rows")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "1":

                print("\nMissing Values:")
                print(self.data.isnull().sum())

            elif choice == "2":

                numeric = self.data.select_dtypes(include=np.number)

                self.data[numeric.columns] = numeric.fillna(
                    numeric.mean()
                )

                print("Numeric missing values filled.")

            elif choice == "3":

                self.data.dropna(inplace=True)

                print("Missing rows removed.")

            elif choice == "4":

                self.data.drop_duplicates(inplace=True)

                print("Duplicate rows removed.")

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

    # --------------------------------------------------
    # Mathematical Operations
    # --------------------------------------------------

    def mathematical_operations(self):

        if not self.check_data():
            return

        if "Sales" not in self.data.columns:
            print("Sales column not found.")
            return

        numbers = self.data["Sales"].to_numpy()

        print("\n===== MATHEMATICAL OPERATIONS =====")

        print("Total Sales:", np.sum(numbers))
        print("Average Sales:", np.mean(numbers))
        print("Maximum Sales:", np.max(numbers))
        print("Minimum Sales:", np.min(numbers))
        print("Standard Deviation:", np.std(numbers))
        print("Variance:", np.var(numbers))

    # --------------------------------------------------
    # NumPy Operations
    # --------------------------------------------------

    def numpy_operations(self):

        if not self.check_data():
            return

        numbers = self.data["Sales"].to_numpy()

        print("\n===== NUMPY OPERATIONS =====")

        print("\nSales Array:")
        print(numbers)

        print("\nFirst 5 Values:")
        print(numbers[:5])

        print("\nFirst Value:")
        print(numbers[0])

        print("\nFirst 5 Values using Slicing:")
        print(numbers[0:5])

        print("\nTotal:")
        print(np.sum(numbers))

        print("\nMean:")
        print(np.mean(numbers))

        print("\nMaximum:")
        print(np.max(numbers))

        print("\nMinimum:")
        print(np.min(numbers))

    # --------------------------------------------------
    # Search, Sort and Filter
    # --------------------------------------------------

    def search_sort_filter(self):

        if not self.check_data():
            return

        while True:

            print("\n===== SEARCH / SORT / FILTER =====")
            print("1. Search Product")
            print("2. Sort by Sales")
            print("3. Filter Sales")
            print("4. Back")

            choice = input("Enter your choice: ")

            if choice == "1":

                if "Product" not in self.data.columns:
                    print("Product column not found.")
                    continue

                name = input("Enter product name: ")

                result = self.data[
                    self.data["Product"].astype(str).str.contains(
                        name,
                        case=False,
                        na=False
                    )
                ]

                print(result)

            elif choice == "2":

                result = self.data.sort_values(
                    "Sales",
                    ascending=False
                )

                print(result)

            elif choice == "3":

                value = float(input("Enter minimum sales: "))

                result = self.data[
                    self.data["Sales"] >= value
                ]

                print(result)

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

    # --------------------------------------------------
    # DataFrame Operations
    # --------------------------------------------------

    def dataframe_operations(self):

        if not self.check_data():
            return

        while True:

            print("\n===== DATAFRAME OPERATIONS =====")
            print("1. Show Data")
            print("2. Show Shape")
            print("3. Show Columns")
            print("4. Select Sales Column")
            print("5. Split Data")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(self.data)

            elif choice == "2":
                print("Shape:", self.data.shape)

            elif choice == "3":
                print(self.data.columns.tolist())

            elif choice == "4":
                print(self.data["Sales"])

            elif choice == "5":
                self.split_data()

            elif choice == "6":
                break

            else:
                print("Invalid choice.")

    # --------------------------------------------------
    # Split Data
    # --------------------------------------------------

    def split_data(self):

        if not self.check_data():
            return

        middle = len(self.data) // 2

        first_part = self.data.iloc[:middle]
        second_part = self.data.iloc[middle:]

        print("\n===== FIRST PART =====")
        print(first_part)

        print("\n===== SECOND PART =====")
        print(second_part)

    # --------------------------------------------------
    # Aggregate Functions
    # --------------------------------------------------

    def aggregate_functions(self):

        if not self.check_data():
            return

        if "Sales" not in self.data.columns:
            print("Sales column not found.")
            return

        print("\n===== AGGREGATE FUNCTIONS =====")

        print("Sum:", self.data["Sales"].sum())
        print("Mean:", self.data["Sales"].mean())
        print("Maximum:", self.data["Sales"].max())
        print("Minimum:", self.data["Sales"].min())
        print("Count:", self.data["Sales"].count())

        if "Region" in self.data.columns:

            print("\nSales by Region:")
            print(
                self.data.groupby("Region")["Sales"].sum()
            )

    # --------------------------------------------------
    # Statistical Analysis
    # --------------------------------------------------

    def statistical_analysis(self):

        if not self.check_data():
            return

        print("\n===== STATISTICAL ANALYSIS =====")

        print("\nDescriptive Statistics:")
        print(self.data.describe())

        if "Sales" in self.data.columns:

            print("\nSales Statistics:")

            print("Mean:",
                  self.data["Sales"].mean())

            print("Median:",
                  self.data["Sales"].median())

            print("Standard Deviation:",
                  self.data["Sales"].std())

            print("Variance:",
                  self.data["Sales"].var())

            print("25% Quantile:",
                  self.data["Sales"].quantile(0.25))

            print("50% Quantile:",
                  self.data["Sales"].quantile(0.50))

            print("75% Quantile:",
                  self.data["Sales"].quantile(0.75))

    # --------------------------------------------------
    # Pivot Table
    # --------------------------------------------------

    def create_pivot_table(self):

        if not self.check_data():
            return

        if "Sales" not in self.data.columns:
            print("Sales column not found.")
            return

        if "Region" not in self.data.columns:
            print("Region column not found.")
            return

        table = pd.pivot_table(
            self.data,
            values="Sales",
            index="Region",
            aggfunc="sum"
        )

        print("\n===== PIVOT TABLE =====")
        print(table)

    # --------------------------------------------------
    # Combine Data
    # --------------------------------------------------

    def combine_data(self):

        if not self.check_data():
            return

        file_path = input(
            "Enter second CSV file path: "
        )

        try:

            second_data = pd.read_csv(file_path)

            print("\n===== CONCAT =====")

            combined = pd.concat(
                [self.data, second_data],
                ignore_index=True
            )

            print(combined)

            common_columns = list(
                set(self.data.columns)
                & set(second_data.columns)
            )

            if len(common_columns) > 0:

                common_column = common_columns[0]

                print("\n===== MERGE =====")

                merged = pd.merge(
                    self.data,
                    second_data,
                    on=common_column
                )

                print(merged)

                print("\n===== JOIN =====")

                left = self.data.set_index(common_column)
                right = second_data.set_index(common_column)

                joined = left.join(
                    right,
                    lsuffix="_left",
                    rsuffix="_right"
                )

                print(joined)

            else:

                print(
                    "\nNo common column found for merge/join."
                )

        except FileNotFoundError:

            print("Second file not found.")

        except Exception as e:

            print("Error:", e)

    # --------------------------------------------------
    # Visualization
    # --------------------------------------------------

    def visualize_data(self):

        if not self.check_data():
            return

        if "Sales" not in self.data.columns:
            print("Sales column not found.")
            return

        while True:

            print("\n===== VISUALIZATION =====")
            print("1. Bar Chart")
            print("2. Line Chart")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Subplots")
            print("8. Seaborn Heatmap")
            print("9. Seaborn Boxplot")
            print("10. Back")

            choice = input("Enter your choice: ")

            # Bar Chart
            if choice == "1":

                data = self.data.head(10)

                plt.figure()

                plt.bar(
                    range(len(data)),
                    data["Sales"]
                )

                plt.title("Sales Bar Chart")
                plt.xlabel("Records")
                plt.ylabel("Sales")

                plt.savefig("sales_bar.png")
                plt.show()

            # Line Chart
            elif choice == "2":

                data = self.data.head(20)

                plt.figure()

                plt.plot(
                    data["Sales"],
                    marker="o"
                )

                plt.title("Sales Line Chart")
                plt.xlabel("Records")
                plt.ylabel("Sales")

                plt.savefig("sales_line.png")
                plt.show()

            # Scatter Plot
            elif choice == "3":

                if "Quantity" in self.data.columns:

                    plt.figure()

                    plt.scatter(
                        self.data["Quantity"],
                        self.data["Sales"]
                    )

                    plt.title("Quantity vs Sales")
                    plt.xlabel("Quantity")
                    plt.ylabel("Sales")

                    plt.savefig("sales_scatter.png")
                    plt.show()

                else:

                    print("Quantity column not found.")

            # Pie Chart
            elif choice == "4":

                if "Region" in self.data.columns:

                    region_sales = self.data.groupby(
                        "Region"
                    )["Sales"].sum()

                    plt.figure()

                    plt.pie(
                        region_sales,
                        labels=region_sales.index,
                        autopct="%1.1f%%"
                    )

                    plt.title("Sales by Region")

                    plt.savefig("sales_pie.png")
                    plt.show()

                else:

                    print("Region column not found.")

            # Histogram
            elif choice == "5":

                plt.figure()

                plt.hist(
                    self.data["Sales"],
                    bins=10
                )

                plt.title("Sales Histogram")
                plt.xlabel("Sales")
                plt.ylabel("Frequency")

                plt.savefig("sales_histogram.png")
                plt.show()

            # Stack Plot
            elif choice == "6":

                data = self.data.head(10)

                plt.figure()

                x = range(len(data))

                plt.stackplot(
                    x,
                    data["Sales"],
                    labels=["Sales"]
                )

                plt.title("Sales Stack Plot")
                plt.xlabel("Records")
                plt.ylabel("Sales")

                plt.legend()

                plt.savefig("sales_stack.png")
                plt.show()

            # Subplots
            elif choice == "7":

                data = self.data.head(10)

                fig, axes = plt.subplots(
                    2, 2,
                    figsize=(10, 8)
                )

                axes[0, 0].bar(
                    range(len(data)),
                    data["Sales"]
                )

                axes[0, 0].set_title("Bar")

                axes[0, 1].plot(
                    data["Sales"]
                )

                axes[0, 1].set_title("Line")

                axes[1, 0].hist(
                    self.data["Sales"],
                    bins=10
                )

                axes[1, 0].set_title("Histogram")

                axes[1, 1].plot(
                    data["Sales"],
                    marker="o"
                )

                axes[1, 1].set_title("Sales Trend")

                plt.tight_layout()

                plt.savefig("sales_subplots.png")
                plt.show()

            # Seaborn Heatmap
            elif choice == "8":

                numeric_data = self.data.select_dtypes(
                    include=np.number
                )

                plt.figure(
                    figsize=(10, 6)
                )

                sns.heatmap(
                    numeric_data.corr(),
                    annot=True
                )

                plt.title("Correlation Heatmap")

                plt.savefig("sales_heatmap.png")
                plt.show()

            # Seaborn Boxplot
            elif choice == "9":

                plt.figure()

                sns.boxplot(
                    y=self.data["Sales"]
                )

                plt.title("Sales Boxplot")

                plt.savefig("sales_boxplot.png")
                plt.show()

            elif choice == "10":
                break

            else:
                print("Invalid choice.")

    # --------------------------------------------------
    # Statistics Summary
    # --------------------------------------------------

    def statistics(self):

        if not self.check_data():
            return

        print("\n===== DESCRIPTIVE STATISTICS =====")

        print(self.data.describe())

        if "Sales" in self.data.columns:

            print(
                "\nTotal Sales:",
                self.data["Sales"].sum()
            )

            print(
                "Average Sales:",
                self.data["Sales"].mean()
            )

            print("Highest Sales:",self.data["Sales"].max())

            print("Lowest Sales:",self.data["Sales"].min())



analyzer = SalesAnalyzer()

while True:

    print("\n===================================")
    print("       SALES DATA ANALYZER")
    print("===================================")

    print("1. Load CSV")
    print("2. Explore Data")
    print("3. Clean Data")
    print("4. DataFrame Operations")
    print("5. Search / Sort / Filter")
    print("6. NumPy Operations")
    print("7. Mathematical Operations")
    print("8. Aggregate Functions")
    print("9. Statistical Analysis")
    print("10. Pivot Table")
    print("11. Combine Data")
    print("12. Visualization")
    print("13. Statistics")
    print("14. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        file_path = input(
            "Enter CSV file path: "
        )

        analyzer.load_data(file_path)

    elif choice == "2":

        analyzer.explore_data()

    elif choice == "3":

        analyzer.clean_data()

    elif choice == "4":

        analyzer.dataframe_operations()

    elif choice == "5":

        analyzer.search_sort_filter()

    elif choice == "6":

        analyzer.numpy_operations()

    elif choice == "7":

        analyzer.mathematical_operations()

    elif choice == "8":

        analyzer.aggregate_functions()

    elif choice == "9":

        analyzer.statistical_analysis()

    elif choice == "10":

        analyzer.create_pivot_table()

    elif choice == "11":

        analyzer.combine_data()

    elif choice == "12":

        analyzer.visualize_data()

    elif choice == "13":

        analyzer.statistics()

    elif choice == "14":

        print("Thank you!")

        break

    else:

        print("Invalid choice.")

