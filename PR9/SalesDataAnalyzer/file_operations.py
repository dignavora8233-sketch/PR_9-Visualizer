import os
import pandas as pd


def create_folders():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists("visualizations"):
        os.makedirs("visualizations")


def create_csv():
    create_folders()

    file_path = "data/sales_data.csv"

    if not os.path.exists(file_path):

        data = {
            "SalesID": [101, 102, 103, 104, 105, 106, 107, 108],
            "Product": [
                "Product A", "Product B", "Product C", "Product D",
                "Product E", "Product F", "Product G", "Product H"
            ],
            "Region": [
                "North", "East", "West", "South",
                "Central", "North", "East", "West"
            ],
            "Sales": [500, 600, 700, 800, 550, 900, 650, 750],
            "Quantity": [5, 6, 7, 8, 5, 9, 6, 7],
            "Year": [2022, 2022, 2022, 2022, 2022, 2023, 2023, 2023]
        }

        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)

        print("\nCSV file created successfully!")

    return file_path


def save_plot(figure, name):
    create_folders()

    path = "visualizations/" + name + ".png"
    figure.savefig(path)

    print("\nVisualization saved:", path)