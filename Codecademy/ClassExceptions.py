# Define your exception up here:
class OutOfStock(Exception):
  """ 
  Exception that gets thrown whe item is out 
  of stock
  """
# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] <= 0:
      raise OutOfStock("The {color} candles are out of stock. {name}".format(color=color, name=self.name))
    else:
      self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')
print(candle_shop)
# This should raise OutOfStock:
try:
  candle_shop.buy('green')
except OutOfStock as a:  # Print the custom message (a)
  print(a)
# print("This item is out of stock.")