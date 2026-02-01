stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", stocks)

while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break

    if stock_name not in stocks:
        print("❌ Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))
    investment = stocks[stock_name] * quantity
    total_investment += investment

print("\n💰 Total Investment Value:", total_investment)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: {total_investment}")

print("📁 Result saved in portfolio.txt")
