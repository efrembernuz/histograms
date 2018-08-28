import matplotlib.pyplot as plt


Ha2Kcal = 630
energy = []
acceptation = []
cv = []

file = 'eta_1000_15000_cartesian'
with open('results/' + file + '.out') as in_file:
    for line in in_file:
        if '#' in line:
            pass
        else:
            energy.append(float(line.split()[0]))
            acceptation.append(float(line.split()[1]))
            cv.append(float(line.split()[2]))

minimum = min(energy)
# modified_array = [(E - minimum)*Ha2Kcal for E in energy]
modified_array = [(E - minimum) for E in energy]
plt.plot(modified_array)
plt.figure()
plt.plot(acceptation)
plt.show()
