import finance as fe
def main():
	amd =fe.Trade("amd_123","2021-4-24","AMD",40,10)

	print(f"{amd.quantity}\t| amd_1")

	amdEND = amd.closs_Trade(99,"2021-4-26",2)
	print(f"{amd.quantity}\t| amd_2")
	print(f"{amdEND.quantity}\t| amd_3")


	myac = fe.Account()

	print(myac.cash.getValue())
if __name__ == '__main__':
	main()
