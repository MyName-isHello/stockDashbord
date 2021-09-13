import yfinance as yf
import gentleRequest as gR

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
		return trade_end


class Trade_RAW:
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
	def getInfo(self):
		return f"""\n|{self.trade_id}\t|{self.symbol}\t|\t{self.quantity}\t|\t{self.buyPrice}\t|{self.buy_day}\t|"""

class Trade_END(Trade_RAW):
	def __init__(self,
		  trade_id,
		  buy_day,
		  end_day,
		  symbol,
		  quantity,
		  buyPrice,
		  sellPrice):
		self.end_day = end_day
		self.sellPrice = sellPrice
		super().__init__(
			trade_id,
			buy_day,
			symbol,
			quantity,
			buyPrice)

	def getInfo(self):
		return f"{super().getInfo()}{self.end_day}\t|  {self.sellPrice}\t|"

class Trade(Trade_RAW):
	def __init__(self,
		  trade_id,
		  buy_day,
		  symbol,
		  quantity,
		  buyPrice):
		super().__init__(
			trade_id,
			buy_day,
			symbol,
			quantity,
		  	buyPrice
		)
	def closs_Trade(self,sellPrice,sellTime,sellQuantity):
			self.quantity = self.quantity - sellQuantity
			item = Trade_END(f"{self.trade_id}_END",
							 self.buy_day,
							 sellTime,
							 self.symbol,
							 sellQuantity,
							 self.buyPrice,
							 sellPrice)
			return item


class Account:
	def __init__(self,cash_start=None):
		self.Postion = []
		self.Histor_Trade = []
		self.PL = 0
		self.agent = Agent()
		self.cash = Cash(cash_start)
		self.gentleRequest = gR.gentleRequest()
	def chkPostion(self):
		""" check the postion if it quantity is 0 then delete it """
		for trade in self.Postion:
			if trade.quantity == 0:
				self.Postion.remove(trade)

	def callAgent_buy(self,symbol, quantity, buyPrice, buy_day):
		item = self.agent.buy(self.cash, symbol, quantity, buyPrice, buy_day)
	
		self.Postion.append(item)
		self.gentleUpdate()

	def callAgent_sell(self,trade,sellPrice,sellTime,sellQuantity):
		item = self.agent.sell(self.cash, trade,sellPrice,sellTime,sellQuantity)
		self.Histor_Trade.append(item)
		self.chkPostion()
		self.gentleUpdate()
		
	def gentleUpdate(self):
		self.gentleRequest.update({"Postion":self.Postion,
								   "Histor_Trade":self.Histor_Trade})

	def showPosition(self):

		tempDic = {}
		for trade in self.Postion:
			try:
				tempDic[trade.symbol].append(trade)
			except KeyError:
				tempDic.update({trade.symbol:[trade]})

		msg = "|symbol\t|quantity\t|avgCost\t|"
		for key, value in tempDic.items():
			# 	     |symbol\t|   quantity\t|   buyPrice\t|

			sumQuantity = sum(map(lambda x : x.quantity,value))
			avgCost = sum(map(lambda x :x.quantity*x.buyPrice,value))/sumQuantity
			
			msg += f"\n|{key}\t|{sumQuantity}\t\t|{avgCost}\t\t|"

		return msg
	def showHistor_Trade(self):
		msg = "|id\t|symbol\t|   quantity\t|   buyPrice\t|buy_day\t| end_day\t|sellPrice|"
		for trade in self.Histor_Trade:
			msg += trade.getInfo()
		return msg