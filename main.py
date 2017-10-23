import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.optimize import curve_fit


def func(x, a):
    return 2*np.sqrt(1/np.pi)*np.sqrt(x)*np.exp(-x/a**2)/a**3
    # return np.log(a*np.sqrt(x)) - b*x


gamma = stats.gamma
chi2 = stats.chi2
maxwell = stats.maxwell

fig1, axs = plt.subplots(2, 2, sharey=True)

molecule = 'c4h4'
kind = ['cartesian', 'modes']
temperature = [100, 200, 300, 400]
files = []

for temp in temperature:
    for i in kind:
        files.append(molecule+'_'+str(temp)+'_'+i)
energy = [[] for i in range(len(files))]
acceptation = [[] for j in range(len(files))]
cv = [[] for l in range(len(files))]

for n, file in enumerate(files):
    with open('results/'+file+'.out') as in_file:
        for line in in_file:
            if '#' in line:
                pass
            else:
                energy[n].append(float(line.split()[0]))
                acceptation[n].append(float(line.split()[1]))
                cv[n].append(float(line.split()[2]))

k = 0.0019872041
Na = 6.0221409e+23
T = temperature[int(1/2)]

# the histogram of the data
n_half = int(len(energy[1])/2)
n_half_pere = int(len(energy[0])/2)
x, z = 0, 0

for n in list(range(0, 8, 2)):
    minimum = min(energy[n]+energy[n+1])
    modified_array1 = [E - minimum for E in energy[n][-5000:]]
    modified_array2 = [E - minimum for E in energy[n+1][-5000:]]
    w1, bins1, patches2 = axs[x, z].hist(modified_array1, 25, normed=True, label='cartesian', fc=(0, 0, 1, 0.5))
    w2, bins2, patchse2 = axs[x, z].hist(modified_array2, 25, normed=True, label='modes', fc=(1, 0, 0, 0.5))
    # w1, bins1, patches2 = axs[x, z].hist(energy[n][-5000:], 25, normed=True, label='cartesian',fc=(0, 0, 1, 0.5))
    # w2, bins2, patchse2 = axs[x, z].hist(energy[n+1][-5000:], 25, normed=True, label='modes', fc=(1, 0, 0, 0.5))

    bins = bins2
    size = len(bins)

    params = maxwell.fit(bins, floc=0)
    axs[x, z].plot(bins, maxwell.pdf(bins, *params), label='maxwell')

    params = chi2.fit(bins, floc=0)
    axs[x, z].plot(bins, chi2.pdf(bins, *params), label='chi2')

    params = gamma.fit(bins, floc=0)
    axs[x, z].plot(bins, gamma.pdf(bins, *params), label='gamma')

    axs[x, z].set_title('Temperature: {} K'.format(temperature[int(n / 2)]), fontsize=10,
                        transform=axs[x, z].transAxes, horizontalalignment='center')

    if z == 1:
        x = 1
        z = 0
    else:
        z = 1
# axs[0, 0].set_title()

# print('Average: {} Standar Deviation: {}'.format(average, deviation))

# ax.set_xlabel('Energy')
# ax.set_ylabel('Probability')
# plt.title('Histogram of :')

plt.legend()
plt.show()
# plt.savefig(molecule+'.png', dpi=300)
quit()
# plt.show()
