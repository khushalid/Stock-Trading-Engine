from data_structures.ticker_array import TickerArray
import threading

class TradingEngine:
    def __init__(self):
        self.ticker_array = TickerArray()
        self.lock = threading.Lock()

    def add_order(self, order_type, ticker_symbol, quantity, price):
        with self.lock:
            self.ticker_array.add_order(order_type, ticker_symbol, quantity, price)
        self.match_order(ticker_symbol)

    def match_order(self, ticker_symbol):
        ticker = self.ticker_array.get_or_create_ticker(ticker_symbol)
        
        while True:
            with self.lock:
                buy_order = ticker.buy_orders.peek()
                sell_order = ticker.sell_orders.peek()

                if not buy_order or not sell_order or buy_order.price < sell_order.price:
                    break

                print(f"Executed trade: {ticker_symbol} | Buy order: {buy_order.quantity} @ ${buy_order.price:.2f} | Sell order: {sell_order.quantity} @ ${sell_order.price:.2f} |", end=" ")
                # Match found, execute trade
                trade_quantity = min(buy_order.quantity, sell_order.quantity)
                
                # Update or remove buy order
                if trade_quantity == buy_order.quantity:
                    ticker.buy_orders.remove_head()
                else:
                    buy_order.quantity -= trade_quantity

                # Update or remove sell order
                if trade_quantity == sell_order.quantity:
                    ticker.sell_orders.remove_head()
                else:
                    sell_order.quantity -= trade_quantity

            # Print trade details (in a real system, you'd record this in a database)
            # print(f"Executed trade: {ticker_symbol}, Quantity: {trade_quantity}, Price: {sell_order.price}")
            print(f"Executed quantity @ price: {trade_quantity} @ ${sell_order.price:.2f} | Total value: ${trade_quantity * sell_order.price:.2f}")


