import requests
r = requests.get('http://127.0.0.1:5000/')
cldr= requests.get('http://127.0.0.1:5000/CLDR')
run= requests.get('http://127.0.0.1:5000/RUN')
# r.status_code
# r.headers['content-type']
# r.encoding
# r.text
# r.json()
print(r.text)
print('-------------------------------------------')
print('-------------------------------------------')
print(cldr.text)
print('-------------------------------------------')
print('-------------------------------------------')
print(run.text)