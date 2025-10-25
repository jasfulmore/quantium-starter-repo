import pandas as pd

pink_morsel_data = 'pink morsel'


df1 = pd.read_csv('quantium-starter-repo/data/daily_sales_data_0.csv')
df2 = pd.read_csv('quantium-starter-repo/data/daily_sales_data_1.csv')
df3 = pd.read_csv('quantium-starter-repo/data/daily_sales_data_2.csv')

combined = pd.concat([df1, df2, df3], ignore_index=True)

# make explicit copy to avoid SettingWithCopyWarning
filtered = combined[combined['product'] == 'pink morsel'].copy()

# Ensure numeric types (strip non-numeric chars from price if needed) and compute sales
filtered['price'] = pd.to_numeric(filtered['price'].astype(str).str.replace(r"[^\d\.-]", "", regex=True), errors='coerce')
filtered['quantity'] = pd.to_numeric(filtered['quantity'], errors='coerce')
filtered['sales'] = filtered['price'] * filtered['quantity']

df_clean = filtered.groupby(['date','region'])['sales'].sum().reset_index()

df = filtered[['sales', 'date', 'region']]




print(df.head())