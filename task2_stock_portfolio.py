stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420
}

total = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name or 'done' to finish: ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock is not available.")
        continue

    quantity = int(input("Enter quantity: "))
    investment = stock_prices[stock] * quantity
    total += investment

    print("Stock:", stock)
    print("Price:", stock_prices[stock])
    print("Quantity:", quantity)
    print("Investment:", investment)

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment:", total)

save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_result.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        file.write("Total Investment: " + str(total))
    print("Result saved successfully.")
