import requests

url = 'http://127.0.0.1:8000/matches'
headers = {
    'Content-Type':'application/json;charset=utf-8'
}

#r = requests.get(url,headers=headers)
r = requests.get(url)
files = r.json()

print(files)