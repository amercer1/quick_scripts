import csv

def process(data, symbol, closing_price):
    print(data, symbol, closing_price)

# Notes: When actually opening a real csv file, you may have to use 'rb'
# for reading bytes instead of 'r'
with open('colon_delimited_stock_prices.txt', 'r') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        data = row["date"]
        symbol = row["symbol"]
        closing_price = row["closing_price"]
        process(data,symbol, closing_price)
