import random

def generate_random_order():
    order_type = random.choice(['Buy', 'Sell'])
    ticker_symbol = f"STOCK{random.randint(1, 1024):04d}"
    quantity = random.randint(1, 100)
    price = random.uniform(1.0, 1000.0)
    return order_type, ticker_symbol, quantity, price
