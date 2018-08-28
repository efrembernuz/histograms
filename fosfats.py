import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from matplotlib.ticker import FormatStrFormatter
import scipy.stats as stats


dir = 'results/phosphate/'
molecule = 'phosphate'
temperature = [10, 50, 100, 150, 200, 250, 300, 350, 400]
files = []

for temp in temperature:
    files.append(molecule+'_'+str(temp)+'_30500_cartesian')
energy = [[] for i in range(len(files))]

n_eclipsed = [0 for i in range(len(files))]
n_staggered = [0 for i in range(len(files))]
Emin = -397040.5560
# Emin = 0

for n, file in enumerate(files):
    with open(dir+file+'.out') as in_file:
        for idx, line in enumerate(in_file):
            if idx >= 1:
                energy[n].append(float(line.split()[0]))
                # energy[n].append(float(line.split()[0]))

# the histogram of the data
fig1, axs = plt.subplots(3, 3, sharex=True)
x, z = 0, 0
means = []
means_asac = []
calaixos = 100
for n in range(len(energy)):
    minimum = min(energy[n])
    modified_array = [(E - minimum) for E in energy[n]]
    w, bins, patches = axs[x, z].hist(modified_array, calaixos, normed=True, label=str(temperature[n]) + 'º', fc=(0, 0, 1, 0.5))

    shape, loc, scale = stats.lognorm.fit(modified_array, floc=0)
    pdf = stats.lognorm.pdf(bins, shape, loc=loc, scale=scale)
    axs[x, z].plot(bins, pdf, 'k', linewidth=3.0, alpha=1)

    if max(pdf) > max(w):
        ymax = max(pdf)
    else:
        ymax = max(w)
    axs[x, z].title.set_text(str(temperature[n]) + 'K')
    # axs[x, z].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    mean, var, skew, kurt = stats.lognorm.stats(shape, loc=loc, scale=scale, moments='mvsk')
    means.append(np.average(modified_array))
    axs[x, z].set_xticks(np.arange(min(modified_array), max(modified_array) + 1, 5))
    loc = plticker.MultipleLocator(base=4.0)
    axs[x, z].xaxis.set_major_locator(loc)
    # axs[x, z].set_xlim((5669, 5674))

    # axs[x, z].ticklabel_format(style='sci', axis='x', scilimits=(0, 0))

    z += 1
    if z == 3:
        x += 1
        z = 0
print('Temperature mean_Ci')
for n in range(len(temperature)):
    print('{} {:.2f}'.format(temperature[n], float(means[n])))


plt.show()
quit()

files = []
for temp in temperature:
    files.append(molecule+'_'+str(temp)+'_30500_cartesian_shape')
shape_Td = [[] for i in range(len(files))]
shape_D4h = [[] for i in range(len(files))]

for n, file in enumerate(files):
    with open(dir+file+'.txt') as in_file:
        for idx, line in enumerate(in_file):
            if idx >= 501:
                shape_Td[n].append(float(line.split()[1]))
                shape_D4h[n].append(float(line.split()[2]))

fig2, axs = plt.subplots(3, 3, sharex=True)
x, z = 0, 0
means = []
means_asac = []
calaixos = 100
shape_n = shape_D4h
for n in range(len(shape_n)):
    weights = np.ones_like(shape_n[n]) / float(len(shape_n[n]))
    w, bins, patches = axs[x, z].hist(shape_n[n], calaixos, normed=True, label=str(temperature[n]) + 'º', fc=(0, 0, 1, 0.5))
    # w, bins, patches = plt.hist(ci[n], 100, normed=True, label=str(temperature[n]) + 'º', fc=(0, 0, 1, 0.5))
    # print('mean1 {} = {}'.format(temperature[n], np.average(energy[n])))

    shape, loc, scale = stats.lognorm.fit(shape_n[n], floc=0)
    pdf = stats.lognorm.pdf(bins, shape, loc=loc, scale=scale)
    axs[x, z].plot(bins, pdf, 'k', linewidth=3.0, alpha=1)

    if max(pdf) > max(w):
        ymax = max(pdf)
    else:
        ymax = max(w)
    # axs[x, z].text(max(bins)*0.9, ymax*0.9, 'T = ' + str(temperature[n]) + 'º')
    axs[x, z].title.set_text(str(temperature[n]) + 'K')
    axs[x, z].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    mean, var, skew, kurt = stats.lognorm.stats(shape, loc=loc, scale=scale, moments='mvsk')
    means.append(np.average(shape_n[n]))

    z += 1
    if z == 3:
        x += 1
        z = 0

print('Temperature mean')
for n in range(len(temperature)):
    print('{} {:.2f}'.format(temperature[n], float(means[n])))
plt.show()
