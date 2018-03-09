import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import scipy.stats as stats
from scipy.optimize import curve_fit


def func(x, a):
    return 2*np.sqrt(1/np.pi)*np.sqrt(x)*np.exp(-x/a**2)/a**3
    # return np.log(a*np.sqrt(x)) - b*x


gamma = stats.gamma
chi2 = stats.chi2
maxwell = stats.maxwell

fig1, axs = plt.subplots(3, 3) #, sharey=True)

molecule = 'eta'
temperature = [10, 50, 100, 150, 200, 250, 300, 350, 400]
files = []
# steps = [10000, 15000, 20000, 25000, 30000, 35000]

for temp in temperature:
    files.append(molecule+'_'+str(temp)+'_30500_cartesian')
ci = [[] for i in range(len(files))]

for n, file in enumerate(files):
    with open('results/'+file+'.out') as in_file:
        for line in in_file:
            if '#' in line:
                pass
            else:
                ci[n].append(float(line.split()[0]))

# the histogram of the data
x, z = 0, 0

means = []
means_asac = []
for n in range(len(ci)):
    minimum = min(ci[n])
    modified_array = [E - minimum for E in ci[n][500:]]
    # modified_array = ci[n]
    means_asac.append(np.mean(ci[n]))
    w, bins, patches = axs[x, z].hist(modified_array, 25, normed=True, label=str(temperature[n])+'º', fc=(0, 0, 1, 0.5))

    s, loc, scale = stats.lognorm.fit(modified_array, floc=0)
    mean, var, skew, kurt = stats.lognorm.stats(s, moments='mvsk')
    print("recalculated parameters, temps {}".format(temperature[n]))
    print("mean: {}, var: {}, skew: {}, kurt: {} ".format(mean, var, skew, kurt))
    means.append(mean)

    num = np.linspace(min(modified_array), max(modified_array), 100)
    pdf = stats.lognorm.pdf(num, s, scale=scale)
    axs[x, z].plot(num, pdf, 'k', linewidth=2.0)
    axs[x, z].legend()
    axs[x, z].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

    z += 1
    if z == 3:
        x += 1
        z = 0


# fig2 = plt.figure()
# plt.plot(temperature, means_asac)
# plt.xlabel('temperature(K)')
# plt.savefig('eta_Ci_temp.png', dpi=300)
plt.show()
quit()