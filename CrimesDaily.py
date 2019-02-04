import csv
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

RawCrimeDates = []
GraphCrimeDates = {}
CrimeDates = []
DailyCrimeCount = []


with open("C:\\Users\\Administrator\\Downloads\\Crime_Data_from_2010_to_Present.csv", "r") as LAPD_WestLA:
	CrimeData = csv.reader(LAPD_WestLA, delimiter = ",")

	for crime in CrimeData:
		if crime[5] == "West LA":
			RawCrimeDates.append(crime[2].split()[0])


dates = [datetime.datetime.strptime(date, "%m/%d/%Y") for date in RawCrimeDates]
dates.sort()
sortedRawCrimeDates = [datetime.datetime.strftime(date, "%m/%d/%Y") for date in dates]

for date in sortedRawCrimeDates:
	if date not in GraphCrimeDates:
		GraphCrimeDates[date] = 0
	else:
		GraphCrimeDates[date] += 1

for date in GraphCrimeDates:
	CrimeDates.append(date)
	DailyCrimeCount.append(GraphCrimeDates[date])

x = [datetime.datetime.strptime(date, "%m/%d/%Y") for date in CrimeDates]

fig, ax = plt.subplots()
ax.plot(x, DailyCrimeCount)

ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.xaxis.set_minor_locator(mdates.MonthLocator())

ax.format_xdata = mdates.DateFormatter("%m/%d/%Y")
ax.grid(True)

plt.title("Daily Occurences of Crime since 2010 in West LA")
plt.ylabel("Number of Crimes per Day")

plt.show()


