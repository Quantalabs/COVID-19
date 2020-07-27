file = open("NYS-Cases.csv", "r")
data = file.readlines()

ny_cases = []
for line in data:
    ny_cases.append(float(line.split(',')[3]))

ny_deaths = []
for line in data:
    numlist = line.split(',')[4].split()
    num = float(''.join(numlist))
    ny_deaths.append(num)

ca_file = open("CA-Cases.csv", "r")
ca_data = ca_file.readlines()

ca_cases = []
for line in ca_data:
    ca_cases.append(int(line.split(',')[3]))

ca_deaths = []
for line in ca_data:
    numlist = line.split(',')[4].split()
    num = float(''.join(numlist))
    ca_deaths.append(num)

date = []
for line in data:
    date.append(line.split(',')[0])

from matplotlib import pyplot as plt

plt.plot(ny_cases, color="turquoise", label="New York Cases")
plt.plot(ca_cases, color="violet", label="California Cases")
plt.plot(ca_deaths, color="red", label="California Deaths")
plt.plot(ny_deaths, color="pink", label="New York Deaths")
plt.ylabel('Cases')
plt.xlabel('Days')
plt.legend()
plt.show()
