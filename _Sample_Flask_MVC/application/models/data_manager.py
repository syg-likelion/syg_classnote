import json, os

def save_account(accounts) :
	account_file = open('user_account.json', 'w')
	account_file.write(json.dumps(accounts))
	if not account_file.closed :
		account_file.close()

def load_account() :
	#이 함수를 호출하면 파일에서 사용자 목록을 읽어와서, 리스트 형태로 return
	pass