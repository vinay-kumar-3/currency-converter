import requests


def main():
    print("\n✨ Simple Currency Converter ✨")
    print("🔄 Getting exchange rates...")

    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        rates = response.json()["rates"]
        print("✅ Got rates successfully!")
    except:
        print("❌ Error: Unable to get exchange rates.")

    print("\n💼 Popular: USD EUR GBP JPY CAD AUD CNY INR")

    while True:
        print("\n💸 Enter details:")
        from_currency = input("From currency code (e.g. USD): ").upper()
        if from_currency not in rates:
            print(f"❌ Invalid code: {from_currency}")
            continue

        to_currency = input("To Currency code: ").upper()
        if to_currency not in rates:
            print(f"❌ Invalid code: {to_currency}")
            continue

        try:
            amount = float(input(f"enter amount in {from_currency}: "))
        except:
            print("Please enter a number.")

        amount_in_from = amount / rates[from_currency]
        amount_in_to = amount_in_from * rates[to_currency]

        print(
            f"\n💰 Result: {amount} {from_currency} = {amount_in_to:.2f} {to_currency}")
        print(
            f"Rate: 1 {from_currency} = {rates[to_currency]/rates[from_currency]:.4f} {to_currency}")

        if not input("\n Convert again? (y/n): ").lower().startswith("y"):
            print("👋 Thanks GoodBye!")
            break


if __name__ == "__main__":
    main()
