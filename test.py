from urllib import request, parse
import json

fixer = 'http://data.fixer.io/api/latest?access_key=dbf220bdadf57b8ba97750df20e4d07b&format=1'

response = request.urlopen(fixer)
result = json.loads(response.read().decode('utf-8'))

usd_cny = result['rates']['CNY']/result['rates']['USD']
print(usd_cny)