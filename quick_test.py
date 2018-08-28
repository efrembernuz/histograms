import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import scipy.stats as stats

# fig1, axs = plt.subplots(3, 3, sharex=True)
molecule = 'eta'
temperature = [10, 50, 100, 150, 200, 250, 300, 350, 400]
files1, files2 = [], []

for temp in temperature:
    files1.append(molecule+'_'+str(temp))
ci_cartesian = [[] for i in range(len(files1))]

for temp in temperature:
    files2.append(molecule+'_'+str(temp)+'_modes')
ci_modes = [[] for i in range(len(files2))]

for n, file in enumerate(files1):
    with open('results/'+file+'.txt') as in_file:
        for line in in_file:
            if '#' in line:
                pass
            else:
                ci_cartesian[n].append(float(line.split()[2]))

for n, file in enumerate(files2):
    with open('results/'+file+'.txt') as in_file:
        for line in in_file:
            if '#' in line:
                pass
            else:
                ci_modes[n].append(float(line.split()[2]))

# the histogram of the data
means = []
means_asac = []
calaixos = 100
x, z = 0, 0
for n in range(len(ci_cartesian)):
    fig, axs = plt.subplots(1, 2, sharex=True, figsize=(15.0, 10.0))
    fig.suptitle('T = ' + str(temperature[n]) + 'K', fontsize=16)
    w1, bins1, patches1 = axs[x].hist(ci_cartesian[n], calaixos, normed=True, fc=(0, 0, 1, 0.5))
    w2, bins2, patches2 = axs[x+1].hist(ci_modes[n], calaixos, normed=True, fc=(0, 0, 1, 0.5))

    shape1, loc1, scale1 = stats.lognorm.fit(ci_cartesian[n], floc=0)
    pdf = stats.lognorm.pdf(bins1, shape1, loc=loc1, scale=scale1)
    axs[x].plot(bins1, pdf, 'k', linewidth=3.0, alpha=1, color='r')
    if max(pdf) > max(w1) and max(pdf) > max(w2):
        ymax = max(pdf)
    elif max(w1) > max(w2):
        ymax = max(w1)
    else:
        ymax = max(w2)
    # axs[x+1].text(10, ymax*0.9, 'T = ' + str(temperature[n]) + 'K')
    # axs[x+1].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    mean, var, skew, kurt = stats.lognorm.stats(shape1, loc=loc1, scale=scale1, moments='mvsk')
    axs[x].set_title('Cartesian')

    shape2, loc2, scale2 = stats.lognorm.fit(ci_modes[n], floc=0)
    pdf = stats.lognorm.pdf(bins2, shape2, loc=loc2, scale=scale2)
    axs[x+1].plot(bins2, pdf, 'k', linewidth=3.0, alpha=1, color='r')
    mean, var, skew, kurt = stats.lognorm.stats(shape2, loc=loc2, scale=scale2, moments='mvsk')
    axs[x+1].set_title('Modes')

    plt.savefig('/Users/efrem/Desktop/ethane_Pere/cartesian_modes_'+str(temperature[n])+'.png', dpi=300)
# plt.show()
