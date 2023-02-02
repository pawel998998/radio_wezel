import json

def read_data(filename):
	with open(filename, encoding="utf-8") as f:
		data = f.read()
	js = json.loads(data)
	return js

