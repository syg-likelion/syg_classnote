import json, os

def save_account(accounts) :
	account_file = open('user_account.json', 'w')
	account_file.write(json.dumps(accounts))
	if not account_file.closed :
		account_file.close()

def load_account() :
	account_file = open('user_account.json', 'r')
	if account_file.read() == '' :
		accounts = []
	else : 
		accounts = json.loads(account_file.read())
	account_file.close()