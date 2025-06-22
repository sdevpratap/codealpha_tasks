stock_prices = {
    "APPLE": 2000,
    "TESLA": 1500,
    "GOOGLE": 13500,
    "AMAZON": 1250,
    "MICROSOFT": 3200
}

def stock_tracker():
    print("Welcome to Stock Tracker!")
    print("Available stocks:", ', '.join(stock_prices.keys()))

    total_investment = 0
    investments = []

    while True:
        stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        price = stock_prices[stock]
        value = price * quantity
        total_investment += value
        investments.append((stock, quantity, price, value))
        print(f"Added: {quantity} x {stock} at ${price} = ${value}")

    print("\n--- Investment Summary ---")
    for stock, qty, price, value in investments:
        print(f"{stock}: {qty} x ${price} = ${value}")
    print(f"\nTotal Investment: ${total_investment}")

    save = input("\nDo you want to save this summary? (yes/no): ").lower()

    if save == "yes":
        filename = input("Enter filename (e.g., result.txt or result.csv): ")

        with open(filename, "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty, price, value in investments:
                f.write(f"{stock},{qty},{price},{value}\n")
            f.write(f"\nTotal Investment: ${total_investment}")

        print(f"Summary saved to {filename} ✅")
        
stock_tracker()
