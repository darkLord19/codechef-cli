from requests_oauthlib import OAuth2Session

client_id = '93a047484029aa73fec6084cf50834fc'
client_secret = '252b7906d1b9c574d1f79356450d5aaf'
token_url = 'https://api.codechef.com/oauth/token'
authorization_url = 'https://api.codechef.com/oauth/authorize'

chef = OAuth2Session(client_id)
access_url, state = chef.authorization_url(authorization_url)
print('Please go here and authorize,', authorization_url)
redirect_response = input('Paste the full redirect URL here:')

code = 

chef.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

r = chef.get('https://api.codechef.com/contests')
print(r.content)