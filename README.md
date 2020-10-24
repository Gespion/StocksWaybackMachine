# StocksWaybackMachine
A program to dig into stocks history to find out how much money you'd have today if you invested some money

**Tools used**
* API: IEX Cloud for stocks data https://iexcloud.io/docs/api/
* Json to manage API data 
* Requests to call API

**TO DO** 
1. Query the stock list based on user input (test exact date first then approximative to avoid weekends)
2. Validate user inputs before querying (stock, dates, amount) --> Done
3. Build a chart
4. empty list: https://sandbox.iexapis.com/stable/stock/appl/chart/date/20190220?chartByDay=true&token=Tsk_b353e1b5a6dc48d18b7d316ece6c8472
5. Deals with some empty results:
- empty result: today's value https://sandbox.iexapis.com/stable/stock/twtr/ohlc?token=Tsk_b353e1b5a6dc48d18b7d316ece6c8472
- empty result when date on weekend. i.e: GOOG - 20150315/14 - 1000 --> list index out of range ()
6. Calculate losses
