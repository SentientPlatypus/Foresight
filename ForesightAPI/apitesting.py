import requests
import constants

data = requests.get("https://ForesightAPI.sentientplatypu.repl.co").json()
print(data)
print(data["maidens"])