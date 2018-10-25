import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.josn'
r = requests.get(url)
response = r.json()
print(r.status_code)
