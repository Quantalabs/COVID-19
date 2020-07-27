file = open("Climate/SF-Cases.csv", "r")
data = file.readlines()

cases = []
for line in data:
    cases.append(float(line.split(',')[0]))

new_cases = []
for line in data:
    new_cases.append(float(line.split(',')[2]))

deaths = []
for line in data:
    deaths.append(float(line.split(',')[1]))

new_deaths = []
for line in data:
    new_deaths.append(float(line.split(',')[3]))

from matplotlib import pyplot as plt

plt.plot(cases,label="SF Total Confirmed Cases")
plt.plot(new_cases,label="SF New Confirmed Cases")
plt.plot(deaths, label="SF Total Deaths")
plt.plot(new_deaths,label="SF New Deaths")
plt.ylabel('Cases')
plt.xlabel('Days')
plt.legend()
plt.show()