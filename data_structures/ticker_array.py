from data_structures.order_list import BuyOrderList, SellOrderList

class Ticker:
    def __init__(self, symbol):
        self.symbol = symbol
        self.buy_orders = BuyOrderList()
        self.sell_orders = SellOrderList()

class TickerArray:
    def __init__(self):
        self.tickers = [None] * 1024  # Initialize array for 1024 tickers

    def hash_symbol(self, symbol):
        # Simple hash function to map ticker symbols to array indices
        return sum(ord(c) for c in symbol) % 1024

    def get_or_create_ticker(self, symbol):
        index = self.hash_symbol(symbol)
        if self.tickers[index] is None:
            self.tickers[index] = Ticker(symbol)
        return self.tickers[index]

    def add_order(self, order_type, symbol, quantity, price):
        ticker = self.get_or_create_ticker(symbol)
        if order_type == 'Buy':
            ticker.buy_orders.add(quantity, price)
        else:  # Sell order
            ticker.sell_orders.add(quantity, price)
