import random

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.stocks.remove(stock)
                break

    def get_stock_price(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                return stock.price
        return None

class StockTradingAlgorithm:
    def __init__(self):
        self.portfolio = Portfolio()

    def initialize_portfolio(self):
        # Add initial stocks to the portfolio
        self.portfolio.add_stock(Stock("AAPL", 150.0))
        self.portfolio.add_stock(Stock("GOOG", 2500.0))
        self.portfolio.add_stock(Stock("TSLA", 650.0))
        self.portfolio.add_stock(Stock("AMZN", 3500.0))
        self.portfolio.add_stock(Stock("MAS",10.00))

    def buy_stock(self, symbol, quantity):
        price = self.portfolio.get_stock_price(symbol)
        if price is not None:
            total_cost = price * quantity
            # Perform buying logic
            print(f"Bought {quantity} shares of {symbol} at ${price:.2f} each. Total cost: ${total_cost:.2f}")
        else:
            print(f"Failed to buy {symbol}. Stock not found in portfolio.")

    def sell_stock(self, symbol, quantity):
        price = self.portfolio.get_stock_price(symbol)
        if price is not None:
            total_sale = price * quantity
            # Perform selling logic
            print(f"Sold {quantity} shares of {symbol} at ${price:.2f} each. Total sale: ${total_sale:.2f}")
        else:
            print(f"Failed to sell {symbol}. Stock not found in portfolio.")

    def run_algorithm(self):
        self.initialize_portfolio()

        # Simulate trading for 10 iterations
        for i in range(10):
            # Generate random stock symbol
            symbol = random.choice(["AAPL", "GOOG", "TSLA", "AMZN","MAS"])

            # Generate random quantity
            quantity = random.randint(100, 2000)

            # Generate random action (buy or sell)
            action = random.choice(["buy", "sell"])

            if action == "buy":
                self.buy_stock(symbol, quantity)
            else:
                self.sell_stock(symbol, quantity)

if __name__ == "__main__":
    trading_algorithm = StockTradingAlgorithm()
    trading_algorithm.run_algorithm()
