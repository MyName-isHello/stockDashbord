import finance as fe
import kivy
from kivy.app import App
def main():
	myac = fe.Account(5000)

	myac.callAgent_buy("tsla", 10, 99, "2021-3-20")
	myac.callAgent_buy("amd", 13, 9, "2021-3-20")
	myac.callAgent_buy("sq", 1, 984, "2021-3-20")
	myac.callAgent_buy("tsla", 10, 929, "2021-3-20")

	myac.callAgent_sell(myac.Postion[1],9,"2021-4-20",3)


#	print(myac.showPosition())

#	print(myac.gentleRequest.gentle_get("fff"))
	print("T$"*50)

if __name__ == '__main__':
	main()
"""
	

	print("#"*20)
	#print(myac.showHistor_Trade())
	#print(myac.cash.getValue())
	#print(myac.Histor_Trade)
"""
