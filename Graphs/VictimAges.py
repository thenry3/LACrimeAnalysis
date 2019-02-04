import csv
import matplotlib.pyplot as plt

CrimeVictimAges = []
AgeGroups = {"0-18": 0, "19-30": 0, "31-50": 0, "51+": 0}


with open("C:\\Users\\Administrator\\Downloads\\Crime_Data_from_2010_to_Present.csv", "r") as LAPD_WestLA:
	CrimeData = csv.reader(LAPD_WestLA, delimiter = ",")

	for crime in CrimeData:
		if (crime[5] == "West LA") & (len(crime[10]) > 0):
			CrimeVictimAges.append(int(crime[10]))

for age in CrimeVictimAges:
	if age > 50:
		AgeGroups["51+"] += 1
	elif age > 30:
		AgeGroups["31-50"] += 1
	elif age > 18:
		AgeGroups["19-30"] += 1
	else:
		AgeGroups["0-18"] += 1

fig, ax = plt.subplots()
ax.bar(AgeGroups.keys() , AgeGroups.values())

plt.title("Comparison of Victim Ages Associated with Crime in West LA")
plt.ylabel("Number of Crimes")
plt.xlabel("Age Ranges")

ax.grid(axis = "y", b = True)

plt.show()








