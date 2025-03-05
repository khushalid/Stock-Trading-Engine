# Real-time Stock Trading Engine

## Project Overview

This project implements a real-time stock trading engine that matches buy and sell orders for multiple stock tickers. It's designed to handle concurrent transactions efficiently, simulating a real-world stock exchange environment.

## Key Features

- Supports 1,024 unique stock tickers
- Concurrent order processing using multi-threading
- Custom implementation of lock-free data structures
- Efficient order matching algorithm with O(n) time complexity
- Simulation of active stock transactions

## Technical Stack

- Language: Python 3.x
- Concurrency: Threading
- Data Structures: Custom implementations (no use of built-in dictionaries or maps)


## Core Components

1. **TradingEngine**: Main class that handles order addition and matching.
2. **TickerArray**: Custom array implementation to store and manage 1,024 stock tickers.
3. **OrderList**: Lock-free linked list implementation for storing buy and sell orders.

## Key Functions

- `add_order(order_type, ticker_symbol, quantity, price)`: Adds a new order to the system.
- `match_order(ticker_symbol)`: Matches buy and sell orders for a given ticker.

## Running the Simulation

To run the trading engine simulation:

1. Ensure you have Python 3.x installed.
2. Navigate to the project directory.
3. Run the following command:
python main.py



