#!/usr/bin/python3

from flask import Flask, request
import argparse
import requests

app = Flask(__name__)
API_KEY=None
API_ENDPOINT='https://www.alphavantage.co/query?function={}&apikey={}'

@app.route('/btc_weekly')
def btc_weekly():
    try:
        req = requests.get( API_ENDPOINT.format('DIGITAL_CURRENCY_WEEKLY&symbol=BTC&market=USD', API_KEY))
        data = req.json()['Time Series (Digital Currency Weekly)']
    except Exception as e:
        return {'status': f'Failed - {str(e)}'}
    else:
        #for key in data.keys():
        #    del data[key]['1a. open (CNY)']
        #    del data[key]['2a. high (CNY)']
        #    del data[key]['3a. low (CNY)']
        #    del data[key]['4a. close (CNY)']
        return data

@app.route('/btc_current')
def btc_current():
    try:
        req = requests.get(API_ENDPOINT.format('CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD',API_KEY))
        data = req.json()['Realtime Currency Exchange Rate']
    except Exception as e:
        return {'status': f'Failed - {str(e)}'}
    else:
        return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str, help='Alpha Vantage API Key')
    args = parser.parse_args();
    API_KEY = args.key
    print(f'Using key {API_KEY}')

    app.run(port=5006, debug=True)
