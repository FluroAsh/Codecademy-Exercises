# Our OutOfStock exception:
class OutOfStock(Exception):
  pass

# Class to raise our OutOfStock exception:
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
  
  # Function to buy specific color of stock, adjust our dictionary if we are able to succesfully purchase
  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1
  
candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# Uncomment to raise OutOfStock:
#candle_shop.buy('green')
