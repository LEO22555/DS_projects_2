import pandas as pd
data = pd.read_csv(r"DS Time Series\fremont-bridge.csv", index_col= 'Date', parse_dates=True)
data.head()

# shortening the column names and adding a “Total” column
data.columns = ["West", "East"]
data["Total"] = data["West"] + data["East"] 
data.head()

# summary statistics for this data:
data.dropna().describe()

#  plotting the raw data
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
data.plot()
plt.ylabel("Hourly Bicycle count")
plt.show()

# resampling the data to a coarser grid; Resampling by week

weekly = data.resample("W").sum()
weekly.plot(style=[':', '--', '-'])
plt.ylabel('Weekly bicycle count')
plt.show()

# mean hourly coun
daily = data.resample('D').sum()
daily.rolling(30, center=True).sum().plot(style=[':', '--', '-'])
plt.ylabel('mean hourly count')
plt.show()

#  Applying a Gaussian window
daily.rolling(50, center=True,
              win_type='gaussian').sum(std=10).plot(style=[':','--', '-'])
plt.show()

import numpy as np
by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
by_time.plot(xticks= hourly_ticks, style=[':', '--', '-'])
plt.ylabel("Traffic according to time")
plt.show()

# GroupBy functionality

import numpy as np
by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
by_time.plot(xticks= hourly_ticks, style=[':', '--', '-'])
plt.ylabel("Traffic according to time")
plt.show()