import csv
from datetime import datetime
import matplotlib.pyplot as plt

def get_weather_data(filename,datas,highs):
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
    
        for row in reader:
            try:
                current_date = datetime.strptime(row[0],'%Y-%m-%d')
                high = int(row[1])
            except ValueError:
                print(current_date,('miss data'))
            else:
                dates.append(current_date)
                highs.append(high)

fig = plt.figure(figsize=(10,6))
plt.title('highest temperatures compare',fontsize=24)

dates,highs = [],[]
get_weather_data('sitka_weather_2014.csv',dates,highs)
plt.plot(dates,highs,linewidth=1,c='red')


dates,highs = [],[]
get_weather_data('death_valley_2014.csv',dates,highs)
plt.plot(dates,highs,linewidth=1,c='yellow')

plt.ylabel('highest temperatures',fontsize=14)
plt.xlabel('Date',fontsize=14)
fig.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()

