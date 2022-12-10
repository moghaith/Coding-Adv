import requests
res = requests.get('https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean')
q_data = res.json()["results"]