from web3 import Web3, HTTPProvider

"""
print(Web3.toWei(1, 'ether'))
print(Web3.toWei(1, 'finney'))
print(Web3.toWei(1, 'szabo'))
print(Web3.toWei(1, 'gwei'))
"""

# print(W.fromWei(10**13, 'ether'))
wal = "0x000D636E559FC89fA5D16792bFF594b1E29cdCc7"

w3 = Web3(HTTPProvider("https://kovan.infura.io"))
#print(w3.eth.blockNumber)
print(w3.eth.getBalance(wal))

tx = "0x2df062b7d992cf1419eb833d1f4709f9daea2549482dfc66961628aee8b8390e"
print(w3.eth.getTransaction(tx).to)

receipt = w3.eth.getTransaction(tx)
print(receipt)