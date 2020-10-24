# A python program to dig into stocks history
# Based on an amount, stock and date, 
# you'll get how much money you'd have today

import json
import curl

token = 'Tpk_50816d3f9c6b4d3fbfb752405608e04d'
url = 'https://sandbox.iexapis.com/stable/ref-data/symbols?token={}'.format(token)

print test

# Get stock list and show to user 
def get_stock_list(url):
    #stocks_list = []
    # connect to api and get stock list
    #response = curl -k url
    print(response.json())

    #return stocks_list

#def get_stock_details(stock_name):

#get_stock_list(url)

curl --version #https://sandbox.iexapis.com/stable/ref-data/symbols?token=Tpk_50816d3f9c6b4d3fbfb752405608e04d
    


# Ask user what stock to query
# Ask user what amount was invested
# Get stock history and show progression: start, actual