# Download stock quotes in CSV


import requests
import time

i = 0

# defint the stocks to download
stock_list = ['GOOG', 'YHOO', 'MSF']

while (i < 1):

    # define the base url
    base_url = 'http://download.finance.yahoo.com/d/quotes.csv'

    # retrieve data from web server
    for stock in stock_list:
        data = requests.get(
            base_url,
            params={'s': stock, 'f': 'sl1d1t1c1ohgv', 'e': '.csv'}
        )

        # output the data to the screen
        print(data.content)

    i += 1

    # pause for 3 seconds
    time.sleep(3)