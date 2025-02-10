from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('data/xrp-usd-max.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Print headers to check
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates, prices, and market-caps
dates, prices, market_caps = [], [], []
for row in reader:
    try:
        # Adjust the date format to match your CSV
        current_date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S UTC')
        price = float(row[1])
        market_cap = float(row[2])
    except ValueError:
        continue  # Skip rows with invalid data
    else:
        dates.append(current_date)
        prices.append(price)
        market_caps.append(market_cap)

# Create a figure and axis
plt.style.use('fivethirtyeight')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the market cap on the primary y-axis (left side)
ax1.plot(dates, market_caps, color='#5B9F6B',
          label='Market-Cap (USD)', alpha=0.5)
ax1.set_xlabel('', fontsize=14)
ax1.set_ylabel('Market-Cap (USD)', fontsize=14, color='#5B9F6B')
ax1.tick_params(axis='y', labelcolor='#5B9F6B')

# Create a second y-axis (right side) for the price
ax2 = ax1.twinx()  # Share the same x-axis
ax2.plot(dates, prices, color='#D9534F', label='Price (USD)', alpha=0.5)
ax2.set_ylabel('Price (USD)', fontsize=14, color='#D9534F')
ax2.tick_params(axis='y', labelcolor='#D9534F')

# Format the plot
title = 'Daily XRP Prices and Market-Cap\n 2024-2025'
ax1.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax1.tick_params(labelsize=12)
ax2.tick_params(labelsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Add legends
ax1.legend(loc='upper left', fontsize=12, bbox_to_anchor=(0, 0.9)) 
ax2.legend(loc='upper left', fontsize=12)

# Show plot
plt.tight_layout()
plt.show()