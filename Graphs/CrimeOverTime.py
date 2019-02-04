import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import datetime


RawCrimeDates = []
CrimeDatesforGraph = {}

CleanCrimeDates = []
CleanCrimeCount = []


years = mdates.YearLocator()
months = mdates.MonthLocator()
yearsFmt = mdates.DateFormatter('%Y')

with open("C:\\Users\\Administrator\\Downloads\\Crime_Data_from_2010_to_Present.csv", "r") as LAPD_WestLA:
	CrimeData = csv.reader(LAPD_WestLA, delimiter = ",")

	for crime in CrimeData:
		if crime[5] == "West LA":
			RawCrimeDates.append(crime[2].split()[0]) 

	# Put dates in order
	dates = [datetime.datetime.strptime(date, "%m/%d/%Y") for date in RawCrimeDates]
	dates.sort()
	sortedRawCrimeDates = [datetime.datetime.strftime(date, "%m/%d/%Y") for date in dates]

	for date in sortedRawCrimeDates:
		if date not in CrimeDatesforGraph:
			CrimeDatesforGraph[date] = 0
		else:
			CrimeDatesforGraph[date] += 1

	for date in CrimeDatesforGraph:
		CleanCrimeDates.append(date)
		CleanCrimeCount.append(CrimeDatesforGraph[date])

	# Makes crime counts increase cumulatively to show growth of crime over the years.
	for counter in range(1, len(CleanCrimeCount)):
		CleanCrimeCount[counter] += CleanCrimeCount[counter - 1]

x = [datetime.datetime.strptime(d,'%m/%d/%Y').date() for d in CleanCrimeDates]

fig, ax = plt.subplots()
ax.plot(x, CleanCrimeCount)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

ax.format_xdata = mdates.DateFormatter('%m/%d/%Y')
ax.grid(True)
plt.ylabel("Crimes Occured")
plt.title("Total Crime Since 2010 in West LA")

plt.show()


