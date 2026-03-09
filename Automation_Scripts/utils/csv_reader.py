
import csv
def read_stocks_from_csv(file_path: str) -> list:
    stocks = []
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            stocks.append(row[0])
    return stocks