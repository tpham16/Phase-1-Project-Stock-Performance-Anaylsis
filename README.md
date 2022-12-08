# Phase 1 Stock Performance Anaylsis using Polygon API Project 
A functional project written in Python that pulls data from Polygon.io.

## How It's Made: 

This project is an beginner friendly project that ultiizes Stock API from Polygon.io. For this project, the following stocks will be analyzed from March 2021 to March 2022: AAPL, AMC, COST, MSFT, and TSLA. These five stocks were chosen because they're common stocks and easily identifiable. 

I requested the API data from Polygon Stock API and extracted the 'Closing Prices' and 'Dates' for each stock from March 2021 to March 2022. Using DictWriter, I saved this data by creating 5 CSV files that contained the Dates and Closing Prices for each respective stock. This can be viewed in extract.py and stock folder. In analysis.py, the standard deviations of each week were calculated using the import statistics. Finally I used matplotlib to plot 5 graphs that presented the change of Standard Deviations from March 2021 to March 2022. 

Example: ![AAPL Stock Performance](https://github.com/tpham16/stock-performance-analysis/blob/main/resources/AAPL_stdev.png)

## Lesson Learned: 
I learned that APIs are a great tool to communicate with a service and access functions and data with a simple command. This is one of my first encounters with using API, but it definitely won't be my last. 

There was a learning curve on how to access the data from an API. However, with the help of my instructors and YouTube videos, I learned how to get an API key, test API endpoints and created an application using Python. Without APIs, the functionality of my applications would be limited. APIs allow me to save tiome when developing. I did not have to manually find the historial data of Apple, Costco, etc. Instead, I can use a more efficient and convenient method such as an OPEN API that simply provides me the data. 

As I continue to analyze data, I hope to practice with various OPEN APIs such as Yahoo Finance API and Spotify API to create more practical applications such as this one.


