import requests
from sys import exit
import json
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/covid19')
	def covid19():
		return main()

def main():
	# https://thevirustracker.com/free-api?countryTotal=ES
	# Simulate that we are making the request from a browser.
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	# Decode to utf-8 because the original object is a byte array.
	# Replace ' with " to correctly form the json object.
	req = requests.get('https://thevirustracker.com/free-api?countryTotal=ES', headers=headers).content.decode('utf-8')
	try:
		print(req)
		json.loads(req)
	except json.JSONDecodeError:
		print('Malformed JSON object.')
		exit(-1)

	# Parse the JSON object
	obj = json.loads(req)
	print(obj)
	obj = obj.get('countrydata')[0]

	# Get the parsed information in variables
	# First, total information
	total_cases = obj.get('total_cases')
	total_recovered = obj.get('total_recovered')
	total_deaths = obj.get('total_deaths')
	total_active_cases = obj.get('total_active_cases')

	# Now, daily information.
	new_cases_today = obj.get('total_new_cases_today')
	new_deaths_today = obj.get('total_new_deaths_today')

	# Not used: total serious cases
	total_serious_cases = obj.get('total_serious_cases')

	# Build our final strings.
	str_cases = 'Total: {} (+{} hoy)'.format(
		total_cases,
		new_cases_today)

	str_deaths = 'Muertos: {} (+{} hoy)'.format(
		total_deaths,
		new_deaths_today)

	str_recovered = 'Recuperados: {}'.format(
		total_recovered)

	# We print our strings in stdout and return them.
	print(str_cases)
	print(str_deaths)
	print(str_recovered)
	return jsonify({
		'cases':str_cases,
		'deaths':str_deaths,
		'recovered':str_recovered,
		'author':'github.com/jasperan'
	})

if __name__ == '__main__':
	main()