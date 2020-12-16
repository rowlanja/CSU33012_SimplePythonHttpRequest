import requests
import json

def makeRequest() :
	user_request = requests.get('https://api.github.com/users/'+user, auth=(token_AuthUser, api_token)).json()
	print(user_request)
	
#SWAP LAST CHAR 'X' FOR 1
#CHANGED BECAUSE IF I PUSH API TOKEN TO GITHUB IT WILL BREAK THE TOKEN
user = 'rowlanja'
#api_token = '8c339686419cf727c52b263b027c42fd13121e4X'
token_AuthUser = 'rowlanja'
makeRequest()
