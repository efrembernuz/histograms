import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import scipy.stats as stats

fig1, axs = plt.subplots(2, 3, sharex=True)

file = 'Td_po4'
files = []

# optimized_energy = -641.8011915
# ha2kcal_mol = 627.509



# for temp in temperature:
#     files.append(molecule+'_'+str(temp)+'_modes')
# ci = [[] for i in range(len(files))]

Td = []
# for n, file in enumerate(files):
with open('results/'+file+'.txt') as in_file:
    for line in in_file:
        # Td.append((float(line.split()[1])-optimized_energy)*ha2kcal_mol)
        Td.append(float(line.split()[1]))

# plt.hist(Td, bins=100)
# plt.xlabel('Energy (Kcal/mol)')
# plt.title('Energy difference of the experimental phosphates vs the optimized one')
# plt.show()
# quit()

calaixos = [25, 50, 75, 100, 125, 150]
x, z = 0, 0
for calaix in calaixos:
# weights = np.ones_like(ci[n]) / float(len(ci[n]))
# ci[n] = ci[n][10000:30000]
    w, bins, patches = axs[x, z].hist(Td, calaix, normed=True, fc=(0, 0, 1, 0.5))
# w, bins, patches = plt.hist(ci[n], 100, normed=True, label=str(temperature[n]) + 'º', fc=(0, 0, 1, 0.5))
# print('mean1 {} = {}'.format(temperature[n], np.average(ci[n])))
    shape, loc, scale = stats.lognorm.fit(Td, floc=0)
    pdf = stats.lognorm.pdf(bins, shape, loc=loc, scale=scale)
    axs[x, z].plot(bins, pdf, 'k', linewidth=3.0, alpha=1)

    axs[x, z].mean, var, skew, kurt = stats.lognorm.stats(shape, loc=loc, scale=scale, moments='mvsk')
    axs[x, z].set_xlabel('S(Td)')


    z += 1
    if z == 3:
        x += 1
        z = 0
# plt.ylabel('%')
# plt.savefig('eta_Ci_temp.png', dpi=300)
# plt.xlabel('S(Td)')
plt.show()
