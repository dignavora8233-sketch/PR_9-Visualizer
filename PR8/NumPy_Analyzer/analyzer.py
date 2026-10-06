import numpy as np


class NumPyAnalyzer:

    def __init__(self):
        self.array = None

    def create_array(self):
        print("\n1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ")

        if choice == "1":
            values = input("Enter elements: ").split()
            self.array = np.array([int(x) for x in values])

        elif choice == "2":
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            values = input("Enter elements: ").split()
            self.array = np.array([int(x) for x in values])
            self.array = self.array.reshape(rows, cols)

        elif choice == "3":
            layers = int(input("Enter layers: "))
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            values = input("Enter elements: ").split()
            self.array = np.array([int(x) for x in values])

            self.array = self.array.reshape(layers, rows, cols)

        print("\nArray created successfully:")
        print(self.array)

    def mathematical_operations(self):

        if self.array is None:
            print("First create an array.")
            return

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice: ")

        values = input("Enter the same-size array elements: ").split()
        second = np.array([int(x) for x in values])
        second = second.reshape(self.array.shape)

        if choice == "1":
            print("\nResult:")
            print(self.array + second)

        elif choice == "2":
            print("\nResult:")
            print(self.array - second)

        elif choice == "3":
            print("\nResult:")
            print(self.array * second)

        elif choice == "4":
            print("\nResult:")
            print(self.array / second)

    def combine_split(self):

        if self.array is None:
            print("First create an array.")
            return

        print("\n1. Combine Arrays")
        print("2. Split Array")

        choice = input("Enter your choice: ")

        if choice == "1":

            values = input("Enter another array elements: ").split()
            second = np.array([int(x) for x in values])
            second = second.reshape(self.array.shape)

            result = np.vstack((self.array, second))

            print("\nCombined Array:")
            print(result)

        elif choice == "2":

            parts = int(input("Enter number of parts: "))

            result = np.split(self.array, parts)

            print("\nSplit Arrays:")
            for x in result:
                print(x)

    def search_sort_filter(self):

        if self.array is None:
            print("First create an array.")
            return

        print("\n1. Search")
        print("2. Sort")
        print("3. Filter")

        choice = input("Enter your choice: ")

        if choice == "1":

            value = int(input("Enter value: "))

            if value in self.array:
                print("Value found.")
            else:
                print("Value not found.")

        elif choice == "2":

            print("\nSorted Array:")
            print(np.sort(self.array))

        elif choice == "3":

            value = int(input("Enter value: "))

            print("\nFiltered values:")
            print(self.array[self.array > value])

    def statistics(self):

        if self.array is None:
            print("First create an array.")
            return

        print("\n1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Sum:", np.sum(self.array))

        elif choice == "2":
            print("Mean:", np.mean(self.array))

        elif choice == "3":
            print("Median:", np.median(self.array))

        elif choice == "4":
            print("Standard Deviation:", np.std(self.array))

        elif choice == "5":
            print("Variance:", np.var(self.array))