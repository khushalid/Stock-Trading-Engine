import random
import threading
import time
from trading_engine import TradingEngine

def generate_random_order():
    order_type = random.choice(['Buy', 'Sell'])
    ticker_symbol = f"STOCK{random.randint(1, 1024):04d}"
    quantity = random.randint(1, 100)
    price = round(random.uniform(1.0, 1000.0), 2)
    return order_type, ticker_symbol, quantity, price

def simulate_trading(engine, num_orders, delay):
    for _ in range(num_orders):
        order = generate_random_order()
        engine.add_order(*order)
        time.sleep(delay)

def main():
    engine = TradingEngine()
    
    num_threads = 5
    # Number of orders per thread
    orders_per_thread = 1000
    delay = 0.01

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=simulate_trading, args=(engine, orders_per_thread, delay))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Simulation complete.")

if __name__ == "__main__":
    main()
