import finance as fe
def main():
	myac = fe.Account(5000)

	myac.callAgent_buy("tsla", 10, 20, "2021-3-20")
	myac.callAgent_buy("amd", 13, 9, "2021-3-20")
	myac.callAgent_buy("sq", 1, 984, "2021-3-20")
	#myac.callAgent_buy("tsla", 10, 20, "2021-3-20")
	myac.callAgent_buy("tsla", 10, 10, "2021-3-20")
	myac.callAgent_sell(myac.Postion[1],9,"2021-4-20",3)
	print(myac.showPosition())

	print("#-"*30)
	#myac.callAgent_sell(trade,sellPrice,sellTime,sellQuantity)
	myac.callAgent_sell(myac.Postion[1],9,"2021-5-1",1)
	print(myac.showPosition())
	print("#-"*30)
	print(myac.Postion)
if __name__ == '__main__':
	main()
"""
	

	print("#"*20)
	#print(myac.showHistor_Trade())
	#print(myac.cash.getValue())
	#print(myac.Histor_Trade)
"""
