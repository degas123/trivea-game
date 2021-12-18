import requests

perma = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
response = requests.get(url="https://opentdb.com/api.php",params=perma)
response.raise_for_status()
data = response.json()
Question = data['results']
question_data = Question
