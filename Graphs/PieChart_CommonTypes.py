import csv
import matplotlib.pyplot as plt
import math

CrimeTracker = {}
CrimeTypes = []
CrimeOccurences = []
cleanCrimeTracker = {}


CrimeCount = 0
OtherTypesofCrimeCount = 0 

with open("C:\\Users\\Administrator\\Downloads\\Crime_Data_from_2010_to_Present.csv", "r") as LAPD_WestLA:
	CrimeData = csv.reader(LAPD_WestLA, delimiter = ",")

	for crime in CrimeData:
		if crime[5] == "West LA":
			if crime[8] not in CrimeTracker:
				CrimeTracker[crime[8]] = 0
				CrimeCount += 1
			else:
				CrimeTracker[crime[8]] += 1
				CrimeCount += 1

	
	CrimeTracker["Other"] = 0
	cleanCrimeTracker["Other"] = 0

	for crime in CrimeTracker:
		if (CrimeTracker[crime] / CrimeCount) < 0.01:
			CrimeTracker["Other"] += CrimeTracker[crime]
			OtherTypesofCrimeCount += 1
		else:
			cleanCrimeTracker[crime] = 0
			cleanCrimeTracker[crime] = CrimeTracker[crime]


	cleanCrimeTracker[str(OtherTypesofCrimeCount) + " OTHER TYPES OF CRIME"] = CrimeTracker["Other"]
	cleanCrimeTracker.pop("Other")
	print(cleanCrimeTracker)


	for crime in cleanCrimeTracker:
		CrimeTypes.append(crime)
		CrimeOccurences.append(cleanCrimeTracker[crime])


plt.pie(CrimeOccurences, labels = CrimeTypes, startangle = 0, autopct = "%.2f%%")
plt.title("Most Common Types of Crime in West LA")
plt.show()













