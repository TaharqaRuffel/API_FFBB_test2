import requests

id = str(38)
iduser = str(1)
idMatch = str(1)

urlbase = 'http://127.0.0.1:8000/snippets/'
urluser = 'http://127.0.0.1:8000/users/'
urlmatch = 'http://127.0.0.1:8000/matches/'

# url = urlbase + id + "/"
# url = urlbase + "highlight/"
#url = urlmatch + idMatch + "/"

url = urlmatch

data = {"championship": "b5e6211f1955b5e6212059fa2263", "day": 2, "match_date": "2020-10-04 09:45:00",
        "home": "ATLANTIQUE BC NAZAIRIEN", "visitor": "AS BRAINS BASKET", "score_home": 43, "score_visitor": 45,
        "plan": "'533001012747'"}
# data = {"championship": "b5e6211f1955b5e6212059fa2278","day":5, "match_date": "2020-10-11 10:30:00",
#         "home": "testHome", "visitor": "AS BRAINS BASKET"}
# data = {'username': 'testUser2', 'email': 'test2@test.com', 'password': 'test'}
headers = {
    'Content-Type': 'application/html;charset=utf-8'
}

# r = requests.get(url,headers=headers)
# r = requests.get(url, auth=('admin', 'admin'))
# r = requests.get(url)
# r = requests.delete(url, auth=('admin', 'admin'))
# r = requests.post(urlbase, data={'code': 'testnew2'}, auth=('admin', 'admin'))
r = requests.post(url, data, auth=('admin', 'admin'))
# r = requests.patch(url, data={'day': 2}, auth=('admin', 'admin'))

#r = requests.put(url, data=data, auth=('admin', 'admin'))

print(url)

# r = requests.get(url2, auth=('admin', 'admin'))
# r = requests.get(urluser, auth=('admin', 'admin'))

print(r.status_code)
print(r.headers['content-type'])

if r.headers['content-type'] == "application/json":
    files = r.json()
    print(files)
else:
    print('no JSON')

# print(r.json().get('id'))
#
# url = urlbase + str(r.json().get('id'))
# print(url)
