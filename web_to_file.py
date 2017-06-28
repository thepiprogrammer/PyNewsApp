import json
from urllib.request import urlopen
url = "https://newsapi.org/v1/articles?source=google-news&sortBy=top&apiKey=631086356f124f4d82bd059ea5fccc88" 
response = urlopen(url)
data = json.loads(response.read())
with open("jsondata.txt", 'w') as outfile:
	outfile.write(json.dumps(data, sort_keys=True, indent=4))
	print(data['articles'][7]['author'])

