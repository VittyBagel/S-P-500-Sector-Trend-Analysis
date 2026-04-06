import pandas as pd
import yfinance as yf
from datetime import datetime
import os

# === 1️⃣ Set your preferred folder path ===
save_folder = r''  # 🔁 change this to your path
os.makedirs(save_folder, exist_ok=True)

# === 2️⃣ Load S&P 500 company list from GitHub ===
url = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv"
sp500_table = pd.read_csv(url)

# Check and normalize column names
if "Symbol" in sp500_table.columns:
    sp500_table.rename(columns={"Symbol": "Ticker"}, inplace=True)
if "Name" in sp500_table.columns:
    sp500_table.rename(columns={"Name": "Company"}, inplace=True)
if "Sector" not in sp500_table.columns:
    sp500_table["Sector"] = None

# Add extra categorical columns
sp500_table["Exchange"] = "NYSE/NASDAQ"
sp500_table["HQ_Location"] = "Unknown"

# === 3️⃣ Select top 100 companies ===
tickers = sp500_table["Ticker"].head(500).tolist()

# === 4️⃣ Download last 10 years of daily stock data ===
data = yf.download(tickers, period="10y", group_by="ticker", progress=True)

# === 5️⃣ Flatten data and prepare for merging ===
frames = []
for ticker in tickers:
    if ticker in data.columns.levels[0]:
        df = data[ticker].copy()
        df["Ticker"] = ticker
        df.reset_index(inplace=True)
        frames.append(df)

# === 6️⃣ Combine all companies' data ===
stock_data = pd.concat(frames)

# === 7️⃣ Merge with metadata ===
merged_df = pd.merge(stock_data, sp500_table, on="Ticker", how="left")

# === 8️⃣ Save to your chosen folder ===
output_file = os.path.join(
    save_folder, f"sp500_100companies_10years_{datetime.now().strftime('%Y%m%d')}.csv"
)
merged_df.to_csv(output_file, index=False)

print(f"\n✅ Dataset successfully saved to:\n{output_file}")
print(f"Total rows: {len(merged_df)}, Columns: {len(merged_df.columns)}")
print("\nSample preview:")
print(merged_df.head())
