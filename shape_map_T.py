import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

np.set_printoptions(threshold=np.nan)
dir = 'results/phosphate/'
molecule = 'phosphate'
temperature = [10, 50, 100, 150, 200, 250, 300, 350, 400]


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

shape_Baur_Td = []
shape_Baur_D4h = []
with open('shape_baur_structures.txt', 'r') as infile:
    for line in infile:
        if 'T' in line:
            pass
        else:
            shape_Baur_Td.append(float(line.split()[0].replace(',', '.')))
            shape_Baur_D4h.append(float(line.split()[1].replace(',', '.')))

shape_sym_Baur_Td = []
shape_sym_Baur_D4h = []
with open('shape_sym_baur_structures.txt', 'r') as infile:
    for line in infile:
        if 'T' in line:
            pass
        else:
            shape_sym_Baur_Td.append(float(line.split()[0].replace(',', '.')))
            shape_sym_Baur_D4h.append(float(line.split()[1].replace(',', '.')))

curves = [[], [], [], [], []]
curve_name = []
n = 0
with open('corves.txt', 'r') as infile:
    curve_name.append(infile.readline().rstrip('\n'))
    infile.readline()
    for line in infile:
        if line in ['\n', '\r\n']:
            n += 1
            curve_name.append(infile.readline().rstrip('\n'))
            infile.readline()
        else:
            x = line.split()[0]
            y = line.split()[1]
            curves[n].append([x.replace(',', '.'), y.replace(',', '.')])
# for idx, curve in enumerate(curves):
#     x_curve, y_curve = [], []
#     for xy in curve:
#         x_curve.append(float(xy[0]))
#         y_curve.append(float(xy[1]))
#     plt.plot(x_curve, y_curve, label=curve_name[idx])
# plt.scatter(shape_sym_Baur_Td, shape_sym_Baur_D4h, s=12, color='b')
# plt.xlim((0, 0.5))
# plt.ylim((25, 35))
# plt.legend(bbox_to_anchor=(1., 1), loc=2, borderaxespad=0., prop={'size': 12})
# plt.show()
# quit()

fig1, axs = plt.subplots(3, 3, sharex=True, sharey=True)
prec = 50
x_grid, r_x = np.linspace(0, 0.6, prec, retstep=True)
y_grid, r_y = np.linspace(26, 34, prec, retstep=True)
l, m = 0, 0
for n in range(len(shape_Td)):
    dens = np.zeros((prec, prec))
    for idn, point in enumerate(shape_Td[n]):
        for idx, x in enumerate(x_grid):
            if float(point) <= x-r_x:
                break
        for idy, y in enumerate(y_grid):
            if float(shape_D4h[n][idn]) <= y+r_y:
                break
        dens[idx][idy] += 1
    maxium = 0
    for row in dens:
        if max(row) >= maxium:
            maxium = max(row)

    for idx, curve in enumerate(curves):
            x_curve, y_curve = [], []
            for xy in curve:
                x_curve.append(float(xy[0]))
                y_curve.append(float(xy[1]))
            axs[l, m].plot(x_curve, y_curve, label=curve_name[idx])

    for idx, x in enumerate(x_grid):
        for idy, y in enumerate(y_grid):
            s = 0
            if dens[idx][idy] == 0:
                pass
            else:
                for max_value in np.linspace(0, maxium, prec):
                    if dens[idx][idy] >= max_value:
                        s += 1
                        axs[l, m].scatter(x, y, s=s)

    axs[l, m].set_xlim((0, 0.5))
    axs[l, m].set_ylim((25, 35))
    axs[l, m].title.set_text(str(temperature[n]) + 'K')
    m += 1
    if m == 3:
        l += 1
        m = 0
#
# for idx, curve in enumerate(curves):
#     x_curve, y_curve = [], []
#     for xy in curve:
#         x_curve.append(f loat(xy[0]))
#         y_curve.append(float(xy[1]))
#     plt.plot(x_curve, y_curve, label=curve_name[idx])


plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size': 10})
plt.show()
quit()

fig2, axs = plt.subplots(3, 3, sharex=True, sharey=True)
x, z = 0, 0
means = []
shape_n = shape_Td
for n in range(len(shape_n)):
    for idx, curve in enumerate(curves):
        x_curve, y_curve = [], []
        for xy in curve:
            x_curve.append(float(xy[0]))
            y_curve.append(float(xy[1]))
        axs[x, z].plot(x_curve, y_curve, label=curve_name[idx])

    axs[x, z].scatter(shape_Td[n], shape_D4h[n], s=10)
    axs[x, z].scatter(shape_Baur_Td, shape_Baur_D4h, s=12, color='y')
    axs[x, z].set_xlim((0, 0.5))
    axs[x, z].set_ylim((25, 35))
    axs[x, z].title.set_text(str(temperature[n])+'K')
    z += 1
    if z == 3:
        x += 1
        z = 0

# print(len(curves))
# quit()
# for idx, curve in enumerate(curves):
#     x_curve, y_curve = [], []
#     for xy in curve:
#         x_curve.append(float(xy[0]))
#         y_curve.append(float(xy[1]))
#     plt.plot(x_curve, y_curve, label=curve_name[idx])
# for idx, curve in enumerate(curves):
#     x_curve, y_curve = [], []
#     for xy in curve:
#         x_curve.append(float(xy[0]))
#         y_curve.append(float(xy[1]))
#     axs[x, z].plot(x_curve, y_curve, label=curve_name[idx])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size': 10})
plt.show()

