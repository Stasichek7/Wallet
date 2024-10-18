from eth_account import Account

account = Account.create()
print(f"Private key: {account.key.hex()}")
print(f"Ethereum address: {account.address}")
