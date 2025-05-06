# 💱 Simple Currency Converter

A lightweight command-line currency converter written in Python that fetches real-time exchange rates from the API.

## ✨ Features

- Fetches latest exchange rates and converts between global currencies.
- Simple interactive CLI interface.
- Converts any amount from one currency to another.
- Displays conversion rate used.
- Graceful error handling for invalid inputs.

## 📦 Requirements

- Python 3.x
- `requests` library

Install dependencies using:

```bash
pip install requests
```
## 🚀 How to Run

```bash
python currency_converter.py
```

You will see a output like:

```bash

✨ Simple Currency Converter ✨
🔄 Getting exchange rates...
✅ Got rates successfully!

💼 Popular: USD EUR GBP JPY CAD AUD CNY INR

💸 Enter details:
From currency code (e.g. USD): USD
To Currency code: INR
enter amount in USD: 100

💰 Result: 100 USD = 8313.20 INR
Rate: 1 USD = 83.1320 INR

```

## 🌍 Supported Currencies
This currency converter supports 236 currencies worldwide. Some of the most popular ones include:

- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- JPY (Japanese Yen)
- CAD (Canadian Dollar)
- AUD (Australian Dollar)
- CNY (Chinese Yuan)
- INR (Indian Rupee)

## ⚠️ Note

- Internet connection is required to fetch live exchange rates.
