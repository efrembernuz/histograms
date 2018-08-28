from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

np.set_printoptions(threshold=np.nan)
dir = 'results/phosphate/'
molecule = 'phosphate'
temperature = [50, 100, 150, 200, 250, 300, 350, 400]


# the histogram of the data
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
xmin = 0
xmax = 0.5
ymin = 25
ymax = 35
X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])
values = np.vstack([shape_Td[0], shape_D4h[0]])
kernel = stats.gaussian_kde(values)
Z = np.reshape(kernel(positions).T, X.shape)
plt.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r)
# plt.plot(shape_Td[0], shape_D4h[0], 'k.', markersize=2)
plt.xlim((0, 1))
plt.ylim((0, 35))
plt.show()
quit()
