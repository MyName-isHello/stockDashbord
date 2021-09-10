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

	def sell(self, cash, trade,sellPrice,sellTime,sellQuantity):
		trade_end = trade.closs_Trade(sellPrice,sellTime,sellQuantity)
		cash.update(cash.getValue()+sellPrice*sellQuantity)
		return Trade_END

class Trade:
	def __init__(self,
		  trade_id,
		  buy_day,
		  symbol,
		  quantity,
		  buyPrice):
		
		self.trade_id = trade_id
		self.buy_day  = buy_day # YYYY-MM-DD 
		self.symbol   = symbol
		self.quantity = quantity
		self.buyPrice = buyPrice

	def getValue(self, daynow):
		ticker = yf.download(self.symbol,daynow,daynow)
		return ticker["Adj Close"]*self.quantity

	def closs_Trade(self,sellPrice,sellTime,sellQuantity):
			self.quantity = self.quantity - sellQuantity
			return Trade_END(self.trade_id+"_END",
							 self.buy_day,
							 sellTime,
							 self.symbol,
							 sellQuantity,
							 self.buyPrice,
							 sellPrice)
	def getInfo(self):
		return f"""|id\t|symbol\t|quantity\t|buyPrice\t|buy_day\t|\n|{self.trade_id}\t|{self.symbol}\t|{self.quantity}\t\t|{self.buyPrice}\t\t|{self.buy_day}\t|
		"""

class Trade_END(Trade):
	def __init__(self,
		  trade_id,
		  buy_day,
		  end_day,
		  symbol,
		  quantity,
		  buyPrice,
		  sellPrice):
		super().__init__(
			trade_id,
			buy_day,
			symbol,
			quantity,
			buyPrice)
		self.end_day = end_day

class Account:
	def __init__(self,cash_start=None):
		self.Postion = []
		self.Histor_Trade = []
		self.PL = 0
		self.agent = Agent()
		self.cash = Cash(cash_start)

	def callAgent_buy(self,symbol, quantity, buyPrice, buy_day):
		self.Postion.append(self.agent.buy(self.cash, symbol, quantity, buyPrice, buy_day))


