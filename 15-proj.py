#!/usr/bin/python3

from flask import Flask, request
import crayons
import requests

app = Flask(__name__)
API_KEY='RYSS5B71Y18GH26A'
API_ENDPOINT='https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol=BTC&market=CNY&apikey={}'

@app.route('/btc_weekly')
def btc_weekly():
    print(API_ENDPOINT.format(API_KEY))
    try:
        req = requests.get(API_ENDPOINT.format(API_KEY))
        data = req.json()['Time Series (Digital Currency Weekly)']
    except Exception as e:
        return {'status': f'Failed - {str(e)}'}
    else:
        for key in data.keys():
            del data[key]['1a. open (CNY)']
            del data[key]['2a. high (CNY)']
            del data[key]['3a. low (CNY)']
            del data[key]['4a. close (CNY)']
        return data

if __name__ == '__main__':
    app.run(port=5006, debug=True)
