# S-P-500-Sector-Trend-Analysis
 This project explores whether historical stock data from the S&P 500 can be used to model and predict short-term sector-level trends, specifically whether a sector’s average log return (stock growth) will be positive over the next 30 days. Multiple models, including time series methods, Random Forest, and RNNs, are used to evaluate predictive performance on aggregated sector data.

## Dataset Setup

### This project uses:
 - S&P 500 company list: [S&P 500 Information](https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv) from Github 
 - Stock price data: fetched using the yfinance library
 The dataset consists of approximately 10 years of daily stock prices for S&P 500 companies.

### To run this project:
1. Clone the repository: https://github.com/VittyBagel/S-P-500-Sector-Trend-Analysis.git
2. Install required dependicies: pip install pandas numpy scikit-learn matplotlib seaborn statsmodels tensorflow
3. Download and run the main Python script from the repo:SP500_10Years_Data_Mining 
4. The script automatically:
    - Pulls S&P 500 company data from GitHub
    - Downloads historical stock data using yfinance
    - Combines the two datasets and makes it ready for analysis
5. Place the raw dataset in the correct directory: `data/raw/sp500_500companies_10years_20260401.csv`
6. Important note on dates:
    - The data pipeline pulls 10 years of data starting from the date of execution
    - If reproducing results, ensure the start/end dates in the script match the original run (April 1, 2026 in this case)

## Model Overview & Results

### Three main approaches were tested:
   - Time Series Models
   - Random Forest Regression
   - RNN (Recurrent Neural Network)

### Performance Summary (RMSE Comparison)
   - Random Forest showed the lowest RMSE overall
   - RNN performance was competitive but unstable across sectors
   - Time series models generally had higher RMSE values due to difficulty capturing non-stationary behavior
   - However, RMSE alone is not a reliable indicator of true predictive performance in this context, especially given the noise and structural changes in financial data.

## Key Insights
   - Sector-level stock behavior is highly noisy and difficult to generalize using standard predictive models
   - Some weak seasonal patterns were observed (e.g., monthly and weekly effects), but they are not stable enough for reliable forecasting
   - Thursdays tend to show slightly negative average returns, while Fridays show mild recoveries across multiple sectors
   - November appears to be a relatively strong month for positive returns across sectors, though this may reflect aggregation bias

## Limitations
   - High temporal bias due to limited 10-year window
   - Heavy reliance on log return aggregation reduces granularity of stock behavior
   - Potential overfitting in Random Forest and RNN models
   - RMSE may give a misleading sense of predictive strength

## Recommendations
   - Avoid using these models for real trading decisions without further validation
   - Incorporate additional features such as macroeconomic indicators or volatility measures
   - Test directional accuracy (up/down prediction) instead of relying only on RMSE
   - Extend dataset beyond 10 years to reduce regime bias

## Final Note
This project is primarily a modeling exploration of financial time series rather than a deployable prediction system. It highlights the limitations of applying standard machine learning models to highly non-stationary financial data like the S&P 500.