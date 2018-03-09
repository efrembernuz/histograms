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

fig1, axs = plt.subplots(2, 3, sharey=True)

molecule = 'p4'
kind = ['cartesian'] #, 'modes']
temperature = [400] # [100, 200, 300, 400]
files = []
steps = [10000, 15000, 20000, 25000, 30000, 35000]

for step in steps:
    for i in kind:
        files.append(molecule+'_400_'+str(step)+'_'+i)
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

means = []
for n in range(len(energy)):
    minimum = min(energy[n])
    modified_array = [E - minimum for E in energy[n][-5000:]]
    w, bins, patches = axs[x, z].hist(modified_array, 25, normed=True, label='cartesian', fc=(0, 0, 1, 0.5))

    s, loc, scale = stats.lognorm.fit(modified_array, floc=0)
    # print("scatter for data is %s" % s)
    # print("mean of data is %s" % scale)
    mean, var, skew, kurt = stats.lognorm.stats(s, moments='mvsk')
    print("recalculated parameters, steps {}".format(steps[n]))
    print("mean: {}, var: {}, skew: {}, kurt: {} ".format(mean, var, skew, kurt))
    means.append(mean)

    num = np.linspace(min(modified_array), max(modified_array), 100)
    pdf = stats.lognorm.pdf(num, s, scale=scale)
    axs[x, z].plot(num, pdf, 'k', label=str(modified_array), linewidth=2.0)

    z += 1
    if z == 3:
        x += 1
        z = 0

# plt.show()

fig2 = plt.figure()
plt.plot(steps, means)
plt.show()
quit()

for n in list(range(0, 8, 2)):
    minimum = min(energy[n]+energy[n+1])
    modified_array1 = [E - minimum for E in energy[n][-5000:]]
    modified_array2 = [E - minimum for E in energy[n+1][-5000:]]
    w1, bins1, patches2 = axs[x, z].hist(modified_array1, 25, normed=True, label='cartesian', fc=(0, 0, 1, 0.5))
    w2, bins2, patchse2 = axs[x, z].hist(modified_array2, 25, normed=True, label='modes', fc=(1, 0, 0, 0.5))
    # w1, bins1, patches2 = axs[x, z].hist(energy[n][-5000:], 25, normed=True, label='cartesian',fc=(0, 0, 1, 0.5))
    # w2, bins2, patchse2 = axs[x, z].hist(energy[n+1][-5000:], 25, normed=True, label='modes', fc=(1, 0, 0, 0.5))

    for fitting_list in [modified_array1, modified_array2]:

        s, loc, scale = stats.lognorm.fit(fitting_list, floc=0)
        # print("scatter for data is %s" % s)
        print("mean of data is %s" % scale)

        num = np.linspace(min(fitting_list), max(fitting_list), 100)
        pdf = stats.lognorm.pdf(num, s, scale=scale)
        axs[x, z].plot(num, pdf, label=str(fitting_list))

    # axs[x, z].set_title('Temperature: {} K'.format(temperature[int(n / 2)]), fontsize=10,
    #                     transform=axs[x, z].transAxes, horizontalalignment='center')

    if z == 1:
        x = 1
        z = 0
    else:
        z = 1

# ax.set_xlabel('Energy')
# ax.set_ylabel('Probability')
# plt.title('Histogram of :')

# plt.legend()
# plt.show()
plt.savefig(molecule+'.png', dpi=300)
# plt.show()
