import json, os

def save_account(accounts) :
	account_file = None
	try :
		account_file = open('user_account.json', 'r+')
	except IOError :
		account_file = open('user_account.json', 'w')
	account_file.write(json.dumps(accounts))
	if not account_file.closed :
		account_file.close()

def load_account() :
	account_file = None
	try :
		account_file = open('user_account.json', 'r')
	except IOError :
		raise
	_json = account_file.read()
	account_file.close()
	if _json == '' :
		accounts = []
	else :
		accounts = json.loads(_json)
	return accounts