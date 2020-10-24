#################################################
#    A python program to dig into stocks history
#    Based on an amount, stock symbol and date, 
#    you'll get how much money you'd have today
#################################################

# -- TO DO -- 
# Query the stock list based on user input (test exact date first then approximative to avoid weekends)
# Validate user inputs before querying (stock, dates, amount) --> Done
# Build a chart
# empty list: https://sandbox.iexapis.com/stable/stock/appl/chart/date/20190220?chartByDay=true&token=Tsk_b353e1b5a6dc48d18b7d316ece6c8472
# empty result: today's value https://sandbox.iexapis.com/stable/stock/twtr/ohlc?token=Tsk_b353e1b5a6dc48d18b7d316ece6c8472
# empty result when date on weekend. i.e: GOOG - 20150315/14 - 1000 --> list index out of range ()
# Calculate loss

# Profit (P) = ( (SP * NS) - SC ) - ( (BP * NS) + BC )
#NS is the number of shares,
#SP is the selling price per share,
#BP is the buying price per share,
#SC is the selling commission,
#BC is the buying commission.


import sys
import json
import requests
import datetime

token = 'Tpk_50816d3f9c6b4d3fbfb752405608e04d'

# Connect to IEX API and query the URL
def connect_to_iex(url_to_get):
    response = requests.get(url_to_get)
    return response.json()    

# Gain or Loss calculator based on Amount, History and Yesterday price
def stock_gain_loss_calculator(user_shares, amount, history_value, yesterday_value):

    #calculate gain
    if yesterday_value > history_value:
        user_gain = (yesterday_value - history_value) * user_shares
        return user_gain

    #calculate loss
    elif yesterday_value < history_value:
        user_loss = (yesterday_value - history_value) * user_shares
        return user_loss
    
    #NoPainNoGain
    else:
        pass

# Based on a user date return stock history
def query_stock_history(symbol, date):

    # Add a try/catch to deal with weekends returning "list index out of range ()

    if date == 'yesterday':
        yesterday_url = 'https://sandbox.iexapis.com/stable/stock/{}/previous?token={}'.format(symbol, token)        
        stock_open_value = connect_to_iex(yesterday_url)
        return stock_open_value['close']
    else:
        history_url = 'https://sandbox.iexapis.com/stable/stock/{}/chart/date/{}?chartByDay=true&token={}'.format(symbol, date, token)
        stock_open_value = connect_to_iex(history_url)
        return stock_open_value[0]['open']


# Main program to query the stock informations based on user input
def query_stock_info():

    symbol_url = 'https://sandbox.iexapis.com/stable/ref-data/symbols?token={}'.format(token)

    print("\n-------------------------------------------")
    print("-  Welcome to the Stocks Wayback Machine  -")
    print("-------------------------------------------")

    # Get the stock to query from the user
    while True:
        print("\nPlease enter a stock symbol to query.\ni.e: 'TSLA' for 'Tesla' or 'AAPL' for 'Apple' or 'q' to Quit the program")
        user_stock = input()

        if len(user_stock) == 4 and user_stock.isalpha():
            # Look for the stock in the collected data from IEX API
            stock_info = connect_to_iex(symbol_url)
            for i in range(len(stock_info)):
                #print( str(i+1) + ": " + stock_info[i]['symbol'] + " - " + stock_info[i]['name'] )
                if user_stock == stock_info[i]['symbol']:
                    #print(stock_info[i]['symbol'] + " - " + stock_info[i]['name'])
                    #stock_details[user_stock] = stock_info[i]['name']
                    #stock_symbol = stock_info[i]['symbol']
                    print("You selected: " + stock_info[i]['symbol'] + " - " + stock_info[i]['name'])                    

                    while True:
                        # Ask for a date to start from
                        print("Please enter a date from which you want to query (AAAAMMDD). Exemple:20190220")
                        user_date = input()
                        if len(user_date) == 8 and user_date.isnumeric():
                            while True:
                                # Ask for an amount to calculate user gain or loss
                                print("Please enter the amount you'd invested back then")
                                user_amount = int(input())
                                #if user_amount.isnumeric() and user_amount > 0:
                                if user_amount > 0:
                                    stock_open_value = query_stock_history(user_stock, user_date)
                                    #print("The open value for " + stock_info[i]['symbol'] + " at " + user_date + " was: " + str(stock_open_value) )

                                    stock_yesterday_value = query_stock_history(user_stock, 'yesterday')
                                    #print("Yesterday's closing value for " + stock_info[i]['symbol'] + " was " + str(stock_yesterday_value) )

                                    # Calculate gain/loss and print to user
                                    print(" --- STARTING SIMULATION ---\n")
                                    #print("If you invested " + str(user_amount) + " back then, you'd have: ")
                                    user_shares = user_amount/stock_open_value
                                    print(" - Stock symbol and name: " + stock_info[i]['symbol'] + " -- " + stock_info[i]['name'])
                                    print(" - Investment date: " + user_date)
                                    print(" - Amount invested: " + str(user_amount))
                                    print(" - Number of shares: " + str(user_shares))
                                    print(" - Open value when invested: " + str(stock_open_value))
                                    print(" - Closing value yesterday: " + str(stock_yesterday_value))
                                    print(" - Total value yesterday: " + str(user_shares * stock_yesterday_value))
                                    print(" - Total profit/loss: " + str((user_shares * stock_yesterday_value)-(user_shares * stock_open_value)))
                                    print(" \n--- END ---")                            
                                    break
                                    #print("Stock not found. Please try again"
                                else:
                                    pass #return in loop to ask for correct amout
                        else:
                            pass #return in loop to ask for correct date
                elif i == len(stock_info)-1: 
                    print("Sorry. The stock you're looking for do not exist")
                    break
        elif user_stock == 'q': 
            print("Goodbye my friend")
            sys.exit()


# Program execution
query_stock_info()