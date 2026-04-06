# S-P-500-Sector-Trend-Analysis
 Predict whether each sector’s average return will be positive over the next 30 days from historical data

## Dataset Setup

This project uses the [S&P 500 Information](https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv) from Github and yfinance library for the stock data.

Repo Link (for PY File): 
https://github.com/VittyBagel/S-P-500-Sector-Trend-Analysis.git

To run this project:
1. Download the PY file (SP500_10Years_Data_Mining) from the repo (above link) and run it
2. The PY file automatically compiles S&P 500 information from Github with the stock market data from yfinance
3. Place `sp500_500companies_10years_20260401.csv` in the `data/raw/` folder
4. The file structure should be: `data/raw/sp500_500companies_10years_20260401.csv`
5. Somewhere in the Time Series Forcasting, you need to add the start and end dates manually because the data mining python will mine the 10 year data from the day you run the code. Above file structure reflects it as I ran my py code on April, 1st. 