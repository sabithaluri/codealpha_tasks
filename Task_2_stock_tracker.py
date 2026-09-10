# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")

# Get number of different stocks
number_of_stocks = int(input("How many different stocks do you have? "))

for i in range(number_of_stocks):

    stock_name = input("Enter stock name (AAPL/TSLA/GOOGL/AMZN/MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity

        print("Stock price:", price)
        print("Investment:", investment)

        total_investment += investment

    else:
        print("Stock not found!")

print("\nTotal Investment Value:", total_investment)
    