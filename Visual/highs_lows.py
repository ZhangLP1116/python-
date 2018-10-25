import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            high = int(row[1])
            low = int(row[3])
            current_date = datetime.strptime(row[0],'%Y-%m-%d')
        except ValueError:
            print(current_date,'miss data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

fig = plt.figure(figsize=(10,6))
plt.plot(dates,highs,linewidth=1,c='red',alpha=0.5)
plt.plot(dates,lows,linewidth=1,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title('Daily high and low temperayures-2014',fontsize=24)
plt.xlabel('sitka_weather_2014',fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()


    
