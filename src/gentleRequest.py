import yfinance as yf
import datetime
class gentleRequest():
	def __init__(self):
		self.Postion = []
		self.Histor_Trade = []
	def update(self,requirement):
		self.Postion = requirement["Postion"]
		self.Histor_Trade = requirement["Histor_Trade"]
	def  gentle_get(self,day_now):
		data_queue = {}
		temp_queue_Postion = {}
		temp_queue_histor = {}
		for trade in self.Postion:
			try:
				temp_queue_Postion[trade.symbol].append(trade)
			except KeyError:
				temp_queue_Postion.update({trade.symbol:[trade]})
		for trade in self.Histor_Trade:
			try:
				temp_queue_histor[trade.symbol].append(trade)
			except KeyError:
				temp_queue_histor.update({trade.symbol:[trade]})

		print(temp_queue_histor)



