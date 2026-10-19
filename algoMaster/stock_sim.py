
import random
import time


def display_market(market, cash, portfolio):
    print("\n" + "=" * 55)
    print("             VIRTUAL STOCK MARKET")
    print("=" * 55)
    print(f"Available cash: Rs. {cash:.2f}")
    print("-" * 55)
    print(f"{'STOCK':<15}{'PRICE':>15}{'CHANGE':>15}")
    print("-" * 55)

    for name, data in market.items():
        change = data["change"]
        sign = "+" if change >= 0 else ""
        print(
            f"{name:<15}"
            f"Rs. {data['price']:>10.2f}"
            f"{sign}{change:>13.2f}"
        )

    print("-" * 55)
    print("Your portfolio:")

    if not portfolio:
        print("You do not own any stocks yet.")
    else:
        for name, quantity in portfolio.items():
            print(f"{name}: {quantity} shares")

    print("=" * 55)


def update_market(market):
    for data in market.values():
        old_price = data["price"]
        percentage = random.uniform(-0.08, 0.08)
        new_price = max(1.0, old_price * (1 + percentage))

        data["price"] = round(new_price, 2)
        data["change"] = round(data["price"] - old_price, 2)

    print("\nMarket prices have been updated!")


def trade_stock(market, portfolio, cash):
    action = input("\nBuy or sell? (B/S): ").strip().upper()
    name = input("Enter stock name: ").strip().upper()

    if name not in market:
        print("Stock not found.")
        return cash

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return cash
    except ValueError:
        print("Please enter a valid whole number.")
        return cash

    price = market[name]["price"]
    total = price * quantity

    if action == "B":
        if total > cash:
            print("Not enough cash to complete this purchase.")
        else:
            cash -= total
            portfolio[name] = portfolio.get(name, 0) + quantity
            print(f"Purchased {quantity} shares of {name}.")

    elif action == "S":
        if portfolio.get(name, 0) < quantity:
            print("You do not own enough shares.")
        else:
            cash += total
            portfolio[name] -= quantity

            if portfolio[name] == 0:
                del portfolio[name]

            print(f"Sold {quantity} shares of {name}.")

    else:
        print("Invalid action. Choose B or S.")

    return cash


def main():
    market = {
        "TECH": {"price": 150.0, "change": 0.0},
        "GREEN": {"price": 85.0, "change": 0.0},
        "SPACE": {"price": 220.0, "change": 0.0},
        "ROBOT": {"price": 120.0, "change": 0.0},
        "HEALTH": {"price": 95.0, "change": 0.0}
    }

    cash = 10000.0
    portfolio = {}

    print("Welcome to the Virtual Stock Market!")
    print("You have Rs. 10,000 in virtual cash.")

    while True:
        display_market(market, cash, portfolio)

        print("\n1. Buy or sell stocks")
        print("2. Advance market by one round")
        print("3. Check portfolio value")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            cash = trade_stock(market, portfolio, cash)

        elif choice == "2":
            update_market(market)
            time.sleep(0.5)

        elif choice == "3":
            portfolio_value = sum(
                market[name]["price"] * quantity
                for name, quantity in portfolio.items()
            )
            total_wealth = cash + portfolio_value

            print(f"\nCash: Rs. {cash:.2f}")
            print(f"Stock value: Rs. {portfolio_value:.2f}")
            print(f"Total wealth: Rs. {total_wealth:.2f}")

        elif choice == "4":
            print("Thanks for playing the stock market simulator!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
