import requests

x = requests.get('https://google.com')

if x.status_code == 200:
  print("hello docker jenkins web hook!")
  print("test new branch")
  print("test2")
else:
  print("bad requests")
