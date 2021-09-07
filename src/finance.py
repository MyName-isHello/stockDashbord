import yfinance as yf

class Cash:
	def __init__(self, number=None):
		self.value = 0
		if number:
			self.value = number
	def getValue(self):
		return self.value

	def update(self,number):
		self.value = number

class Histor_Trade:
	def __init__(self):
		self.TradeList = []

	def update(Trade):
		self.TradeList.append(Trade)


class Agent:
	def __init__(self):
		self.idCount = 0

	def idGaveter(self):
		self.idCount+=1
		return self.idCount

	def buy(self,cash, symbol, quantity, buyPrice, dayTime):
		trade = Trade(self.idGaveter(),dayTime,symbol,quantity,buyPrice)
		cash.update(cash.getValue()-buyPrice*quantity)
		return trade

	def sell(self, cash, Trade):
		pass

class Trade:
	def __init__(self,
		  trade_id,
		  dayTime,
		  symbol,
		  quantity,
		  buyPrice):
		
		self.trade_id = trade_id
		self.dayTime  = dayTime # YYYY-MM-DD 
		self.symbol   = symbol
		self.quantity = quantity
		self.buyPrice = buyPrice

	def getValue(self, daynow):
		ticker = yf.download(self.symbol,daynow,daynow)
		return ticker["Adj Close"]*self.quantity
