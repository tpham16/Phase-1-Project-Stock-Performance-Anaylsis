from config import key
import requests
import time
import csv

stocks = ["AAPL","COST","TSLA","MSFT","AMC"] 

for stock in stocks: 
    api_url  = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=299&apiKey={key}"
    data = requests.get(api_url)
    json_data = data.json()
    results = json_data['results']
    list_data = []
    for closing in results: 
        closing_price = closing['c']
        time_price = closing['t']
        date = time.strftime('%Y-%m-%d', time.localtime(closing['t']/1000))
        dict = {
            'Date':date,
            'Closing_Price':closing_price
        }
        list_data.append(dict)
                
    with open(f"{stock}.csv", "w", newline='') as outfile:
        fieldnames = ['Date','Closing_Price']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_data)

