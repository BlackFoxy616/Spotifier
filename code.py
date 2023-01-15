import requests
from urllib.parse import urlencode
import base64,csv

client_id = "157ea601d4e04eb487df842f1fbb3fa3"
client_secret = "7ea9beec487d46d98295a21c96a29dad"

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:7777/callback",
    "scope": "user-library-read"
}

print("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))


code=input("code:")


encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}



token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:7777/callback"
}


r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)
print(r)
token = r.json()["access_token"]
time = r.json()["expires_in"]
refresh_token = r.json()["refresh_token"]




with open('token.csv','w+') as file:
   cwrite = csv.writer(file)
   cwrite.writerow([token,time, refresh_token])
    
print(token,time, refresh_token)