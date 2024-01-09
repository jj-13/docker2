import requests

x = requests.get('https://google.com')

if x.status_code == 200:
  print("hello docker jenkins!")
else:
  print("bad requests")
