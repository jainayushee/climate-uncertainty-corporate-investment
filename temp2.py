import pandas as pd

sp500_data = pd.read_csv("https://datahub.io/core/s-and-p-500-companies/r/constituents.csv")
sp500_dict = {}

for index, row in sp500_data.iterrows():
    company_name = row['Name']
    ticker_symbol = row['Symbol']
    sp500_dict[company_name] = ticker_symbol

print(sp500_dict)
