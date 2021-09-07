import finance as fe
def main():
	cash = fe.Cash(5000)
	print(f"{cash.getValue()}\t| cash work.")

	agent = fe.Agent()
	amd = agent.buy(cash,"AMD",10,20,"2021-01-08")
	print(f"{cash.getValue()}\t| cash after agent.buy action")
	print(f"{amd.getValue('2021-01-08')}\t| amd object")
if __name__ == '__main__':
	main()