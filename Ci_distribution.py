import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import scipy.stats as stats
from scipy.optimize import curve_fit


# def func(x, a):
#     return 2*np.sqrt(1/np.pi)*np.sqrt(x)*np.exp(-x/a**2)/a**3
    # return np.log(a*np.sqrt(x)) - b*x


gamma = stats.gamma
chi2 = stats.chi2
maxwell = stats.maxwell

fig1, axs = plt.subplots(3, 3, sharex=True)

molecule = 'eta'
temperature = [10, 50, 100, 150, 200, 250, 300, 350, 400]
files = []

for temp in temperature:
    files.append(molecule+'_'+str(temp)+'_modes')
ci = [[] for i in range(len(files))]

n_eclipsed = [0 for i in range(len(files))]
n_staggered = [0 for i in range(len(files))]

for n, file in enumerate(files):
    with open('results/'+file+'.txt') as in_file:
        for line in in_file:
            if '#' in line:
                pass
            else:
                ci[n].append(float(line.split()[2]))
                if abs(float(line.split()[2]) - 9.89) <= 1e-2:
                    n_eclipsed[n] += 1
                elif abs(float(line.split()[2]) - 0) <= 1e-2:
                    n_staggered[n] += 1

mean_staggered = []
mean_eclipsed = []
print('Temperature mean_staggered')
for n in range(len(temperature)):
    mean_staggered.append(100*n_staggered[n] / len(ci[n]))
    print('{} {:.1f}'.format(temperature[n], mean_staggered[n]))
print('Temperature mean_eclipsed')
for n in range(len(temperature)):
    mean_eclipsed.append(100*n_eclipsed[n] / len(ci[n]))
    print('{} {:.1f}'.format(temperature[n], mean_eclipsed[n]))

# the histogram of the data
x, z = 0, 0
means = []
means_asac = []
calaixos = 100
for n in range(len(ci)):
    weights = np.ones_like(ci[n]) / float(len(ci[n]))
    ci[n] = ci[n][10000:30000]
    w, bins, patches = axs[x, z].hist(ci[n], calaixos, normed=True, label=str(temperature[n])+'º', fc=(0, 0, 1, 0.5))
    # w, bins, patches = plt.hist(ci[n], 100, normed=True, label=str(temperature[n]) + 'º', fc=(0, 0, 1, 0.5))
    print('mean1 {} = {}'.format(temperature[n], np.average(ci[n])))

    shape, loc, scale = stats.lognorm.fit(ci[n], floc=0)
    pdf = stats.lognorm.pdf(bins, shape, loc=loc, scale=scale)
    axs[x, z].plot(bins, pdf, 'k', linewidth=3.0, alpha=1)

    if max(pdf) > max(w):
        ymax = max(pdf)
    else:
        ymax = max(w)
    # axs[x, z].text(max(bins)*0.9, ymax*0.9, 'T = ' + str(temperature[n]) + 'º')
    axs[x, z].text(10, ymax*0.9, 'T = ' + str(temperature[n]) + 'K')
    axs[x, z].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    mean, var, skew, kurt = stats.lognorm.stats(shape, loc=loc, scale=scale, moments='mvsk')
    # print('Temperature = {}, mean1 = {}, mean2 = {}'.format(temperature[n], mean, np.mean(w)))
    # print(max(w))
    # print('Temperature = {}'.format(temperature[n]))
    # print('mean = {}, var = {}, skew = {}, kurt = {}'.format(mean, var, skew, kurt))
    # print('mean_real = {}, mode = {}'.format(np.mean(w), ci[n][np.argmax(w)]))
    # print('other_mean = {}'.format(np.mean(ci[n])))
    # print()
    means.append(np.average(ci[n]))

    z += 1
    if z == 3:
        x += 1
        z = 0

print('Temperature mean_Ci')
for n in range(len(temperature)):
    print('{} {:.2f}'.format(temperature[n], float(means[n])))
fig2 = plt.figure()
plt.plot(temperature, means)
plt.xlabel('temperature(K)')
plt.ylabel('Mean')
fig3 = plt.figure()
plt.plot(temperature, mean_staggered)
plt.xlabel('temperature(K)')
plt.ylabel('%')
fig4 = plt.figure()
plt.plot(temperature, mean_eclipsed)
plt.xlabel('temperature(K)')
plt.ylabel('%')
# plt.savefig('eta_Ci_temp.png', dpi=300)
plt.show()
