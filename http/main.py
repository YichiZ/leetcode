import requests

r = requests.get('https://api.spacetraders.io/game/status')

data = r.json()

print(data)
