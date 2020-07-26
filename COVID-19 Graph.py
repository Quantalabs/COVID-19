file = open("statewide_cases.csv", "r")
data = file.readlines()

cases = []
for line in data:
    cases.append(int(line.split(',')[0]))


from matplotlib import pyplot as plt

plt.plot(cases)
plt.ylabel('Cases')
plt.xlabel('Days')
plt.show()