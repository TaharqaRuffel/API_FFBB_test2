import requests

url = 'http://127.0.0.1:8000/'
headers = {
    'Content-Type':'application/json;charset=utf-8'
}

#r = requests.get(url,headers=headers)
r = requests.get(url,headers=headers)
print(r.status_code)
print(r.headers['content-type'])

if r.headers['content-type'] == "application/json":
    files = r.json()
    print(files)
else :
    print('no JSON')