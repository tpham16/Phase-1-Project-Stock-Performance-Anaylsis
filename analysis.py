import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import statistics

AAPL_data = []
AMC_data = []
COST_data = []
MSFT_data = []
TSLA_data = []

empty_list = [AAPL_data,AMC_data,COST_data,MSFT_data,TSLA_data]
files = ["AAPL.csv","AMC.csv","COST.csv","MSFT.csv","TSLA.csv"]
stock_dict = dict(zip(files,empty_list))

for stock in files:
    with open(stock, "r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            stock_dict[stock].append(row)

i = 0 
AAPL_stdev = []
while i < len(AAPL_data):
    if i + 1 >= len(AAPL_data) or i + 2 >= len(AAPL_data) or i + 3 >= len(AAPL_data) or i + 4 >= len(AAPL_data):
        break
    day1 = float(AAPL_data[i]['Closing_Price'])
    day2 = float(AAPL_data[i + 1]['Closing_Price'])
    day3 = float(AAPL_data[i + 2]['Closing_Price'])
    day4 = float(AAPL_data[i + 3]['Closing_Price'])
    day5 = float(AAPL_data[i + 4]['Closing_Price'])
    x = statistics.pstdev([day1,day2,day3,day4,day5]) 
    AAPL_stdev.append(x)
    i += 5 

i = 0 
AMC_stdev = []
while i < len(AMC_data):
    if i + 1 >= len(AMC_data) or i + 2 >= len(AMC_data) or i + 3 >= len(AMC_data) or i + 4 >= len(AMC_data):
        break
    day1 = float(AMC_data[i]['Closing_Price'])
    day2 = float(AMC_data[i + 1]['Closing_Price'])
    day3 = float(AMC_data[i + 2]['Closing_Price'])
    day4 = float(AMC_data[i + 3]['Closing_Price'])
    day5 = float(AMC_data[i + 4]['Closing_Price'])
    x = statistics.pstdev([day1,day2,day3,day4,day5]) 
    AMC_stdev.append(x)
    i += 5 
    
i = 0 
COST_stdev = []
while i < len(AAPL_data):
    if i + 1 >= len(COST_data) or i + 2 >= len(COST_data) or i + 3 >= len(COST_data) or i + 4 >= len(COST_data):
        break
    day1 = float(COST_data[i]['Closing_Price'])
    day2 = float(COST_data[i + 1]['Closing_Price'])
    day3 = float(COST_data[i + 2]['Closing_Price'])
    day4 = float(COST_data[i + 3]['Closing_Price'])
    day5 = float(COST_data[i + 4]['Closing_Price'])
    x = statistics.pstdev([day1,day2,day3,day4,day5]) 
    COST_stdev.append(x)
    i += 5 
    
i = 0 
MSFT_stdev = []
while i < len(AAPL_data):
    if i + 1 >= len(MSFT_data) or i + 2 >= len(MSFT_data) or i + 3 >= len(MSFT_data) or i + 4 >= len(MSFT_data):
        break
    day1 = float(MSFT_data[i]['Closing_Price'])
    day2 = float(MSFT_data[i + 1]['Closing_Price'])
    day3 = float(MSFT_data[i + 2]['Closing_Price'])
    day4 = float(MSFT_data[i + 3]['Closing_Price'])
    day5 = float(MSFT_data[i + 4]['Closing_Price'])
    x = statistics.pstdev([day1,day2,day3,day4,day5]) 
    MSFT_stdev.append(x)
    i += 5 
    
i = 0 
TSLA_stdev = []
while i < len(AAPL_data):
    if i + 1 >= len(TSLA_data) or i + 2 >= len(TSLA_data) or i + 3 >= len(TSLA_data) or i + 4 >= len(TSLA_data):
        break
    day1 = float(TSLA_data[i]['Closing_Price'])
    day2 = float(TSLA_data[i + 1]['Closing_Price'])
    day3 = float(TSLA_data[i + 2]['Closing_Price'])
    day4 = float(TSLA_data[i + 3]['Closing_Price'])
    day5 = float(TSLA_data[i + 4]['Closing_Price'])
    x = statistics.pstdev([day1,day2,day3,day4,day5]) 
    TSLA_stdev.append(x)
    i += 5 

# AAPL 
plt.plot(AAPL_stdev)
plt.xlabel('Weeks') 
plt.ylabel('Standard Deviation of Closing Price')  
plt.title("Weekly Standard Deviations of Apple (2021-2022)")

plt.savefig("AAPL_stdev.png")
plt.show()

# AMC
plt.plot(AMC_stdev)
plt.xlabel('Weeks') 
plt.ylabel('Standard Deviation of Closing Price')  
plt.title("Weekly Standard Deviations of AMC (2021-2022)") 

plt.savefig("AMC_stdev.png")
plt.show()

# MSFT 
plt.plot(MSFT_stdev)
plt.xlabel('Weeks') 
plt.ylabel('Closing Price')  
plt.title("Weekly Standard Deviations of Microsoft (2021-2022)")

plt.savefig("MSFT_stdev.png")
plt.show()

# COST
plt.plot(COST_stdev)
plt.xlabel('Weeks') 
plt.ylabel('Standard Deviation of Closing Price')  
plt.title("Weekly Standard Deviations of Costco (2021-2022)") 

plt.savefig("COST_stdev.png")
plt.show()

# TSLA 
plt.plot(TSLA_stdev)
plt.xlabel('Weeks') 
plt.ylabel('Standard Deviation of Closing Price')  
plt.title("Weekly Standard Deviations of Tesla (2021-2022)") 

plt.savefig("TSLA_stdev.png")
plt.show()
