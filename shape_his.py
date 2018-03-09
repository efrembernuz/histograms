import matplotlib.pyplot as plt


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

fig1, axs = plt.subplots(2, 3, sharey=True)


molecule = 'p4'
# shape_measure = ['HP-6', 'PPY-6', 'OC-6', 'TPR-6', 'JPPY-6']
shape_measure = ['A', 'B']
kind = ['cartesian'] #, 'modes']
temperature = [400] #[100, 200, 300, 400]
files = []
steps = [10000, 15000, 20000, 25000, 30000, 35000]

for step in steps:
    for i in kind:
        files.append(molecule+'_400_'+str(step)+'_'+i+'_shape')
shape1 = [[] for i in range(len(files))]
shape2 = [[] for j in range(len(files))]
shape3 = [[] for k in range(len(files))]
shape4 = [[] for l in range(len(files))]
shape5 = [[] for m in range(len(files))]


for n, file in enumerate(files):
    with open('results/'+file+'.txt') as in_file:
        for line in nonblank_lines(in_file):
            if any(s in line for s in ['-', 'Shape', '#']):
                pass
            else:
                shape1[n].append(float(line.split()[1]))
                shape2[n].append(float(line.split()[2]))
                # shape3[n].append(float(line.split()[2]))
                # shape4[n].append(float(line.split()[3]))
                # shape5[n].append(float(line.split()[4]))

bins = 10
n_mostres = 2
x, z = 0, 0
for n in range(len(shape1)):
    print(shape1[n])
    axs[x, z].hist(shape1[n][int(len(shape1[n])/2):], bins, normed=True, label='cartesian', fc=(0, 0, 1, 0.5))

    z += 1
    if z == 3:
        x += 1
        z = 0

# plt.show()

plt.show()
quit()

x, y = 0, 0
fig1, axs1 = plt.subplots(2, 2, sharey=True)
for n in list(range(0, 8, 2)):
    axs1[x, y].hist(shape1[n][-n_mostres:], bins, normed=True, label='cartesian',fc=(0, 0, 1, 0.5))
    axs1[x, y].hist(shape1[n+1][-n_mostres:], bins, normed=True, label='modes', fc=(1, 0, 0, 0.5))
    axs1[x, y].set_title('Temperature: {} K'.format(temperature[int(n / 2)]), fontsize=10,
                        transform=axs1[x, y].transAxes, horizontalalignment='center')
    if y == 1:
        x = 1
        y = 0
    else:
        y = 1

x = 0
fig2, axs2 = plt.subplots(2, 2, sharey=True)
for n in list(range(0, 8, 2)):
    axs2[x, y].hist(shape2[n][-n_mostres:], bins, normed=True, label='cartesian',fc=(0, 0, 1, 0.5))
    axs2[x, y].hist(shape2[n+1][-n_mostres:], bins, normed=True, label='modes', fc=(1, 0, 0, 0.5))
    axs2[x, y].set_title('Temperature: {} K'.format(temperature[int(n / 2)]), fontsize=10,
                         transform=axs2[x, y].transAxes, horizontalalignment='center')

    if y == 1:
        x = 1
        y = 0
    else:
        y = 1

fig1.suptitle('Shape measure for '+shape_measure[0])
fig2.suptitle('Shape measure for '+shape_measure[1])

fig1.legend()
fig2.legend()
plt.show()
quit()
x = 0
fig3, axs3 = plt.subplots(2, 2, sharey=True)
for n in list(range(0, 8, 2)):
    axs3[x, y].hist(shape3[n][-n_mostres:], bins, normed=True, label='cartesian',fc=(0, 0, 1, 0.5))
    axs3[x, y].hist(shape3[n+1][-n_mostres:], bins, normed=True, label='modes', fc=(1, 0, 0, 0.5))
    axs3[x, y].set_title('Temperature: {} K'.format(temperature[int(n / 2)]), fontsize=10,
                         transform=axs3[x, y].transAxes, horizontalalignment='center')

    if y == 1:
        x = 1
        y = 0
    else:
        y = 1

x = 0
fig4, axs4 = plt.subplots(2, 2, sharey=True)
for n in list(range(0, 8, 2)):
    axs4[x, y].hist(shape4[n][-n_mostres:], bins, normed=True, label='cartesian',fc=(0, 0, 1, 0.5))
    axs4[x, y].hist(shape4[n+1][-n_mostres:], bins, normed=True, label='modes', fc=(1, 0, 0, 0.5))
    axs4[x, y].set_title('Temperature: {} K'.format(temperature[int(n / 2)]), fontsize=10,
                         transform=axs4[x, y].transAxes, horizontalalignment='center')

    if y == 1:
        x = 1
        y = 0
    else:
        y = 1

x = 0
fig5, axs5 = plt.subplots(2, 2, sharey=True)
for n in list(range(0, 8, 2)):
    axs5[x, y].hist(shape5[n][-n_mostres:], bins, normed=True, label='cartesian',fc=(0, 0, 1, 0.5))
    axs5[x, y].hist(shape5[n+1][-n_mostres:], bins, normed=True, label='modes', fc=(1, 0, 0, 0.5))
    axs5[x, y].set_title('Temperature: {} K'.format(temperature[int(n / 2)]), fontsize=10,
                         transform=axs5[x, y].transAxes, horizontalalignment='center')

    if y == 1:
        x = 1
        y = 0
    else:
        y = 1

fig1.suptitle('Shape measure for '+shape_measure[0])
fig2.suptitle('Shape measure for '+shape_measure[1])
# fig3.suptitle('Shape measure for '+shape_measure[2])
# fig4.suptitle('Shape measure for '+shape_measure[3])
# fig5.suptitle('Shape measure for '+shape_measure[4])

fig1.legend()
fig2.legend()
# fig3.legend()
# fig4.legend()
# fig5.legend()
plt.show()
# fig1.savefig(molecule+'_'+shape_measure[0]+'.png', dpi=300)
# fig2.savefig(molecule+'_'+shape_measure[1]+'.png', dpi=300)
