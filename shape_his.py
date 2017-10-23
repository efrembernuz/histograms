import matplotlib.pyplot as plt


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


fig1, axs1 = plt.subplots(2, 2, sharey=True)
fig2, axs2 = plt.subplots(2, 2, sharey=True)

molecule = 'b6h6'
shape_measure = ['OC-6', 'HP-6']
kind = ['cartesian', 'modes']
temperature = [100, 200, 300, 400]
files = []

for temp in temperature:
    for i in kind:
        files.append(molecule+'_'+str(temp)+'_'+i+'_shape')
shape1 = [[] for i in range(len(files))]
shape2 = [[] for j in range(len(files))]


for n, file in enumerate(files):
    with open('results/'+file+'.txt') as in_file:
        for line in nonblank_lines(in_file):
            if '-' in line or 'Shape' in line:
                pass
            else:
                shape1[n].append(float(line.split()[0]))
                shape2[n].append(float(line.split()[1]))

n_half = int(len(shape1[1])/2)
n_half_pere = int(len(shape2[0])/2)

x, y = 0, 0
for n in list(range(0, 8, 2)):
    w1, bins1, patches2 = axs1[x, y].hist(shape1[n][-5000:], 25, normed=True, label='cartesian',fc=(0, 0, 1, 0.5))
    w2, bins2, patchse2 = axs1[x, y].hist(shape1[n+1][-5000:], 25, normed=True, label='modes', fc=(1, 0, 0, 0.5))

    if y == 1:
        x = 1
        y = 0
    else:
        y = 1

x = 0
for n in list(range(0, 8, 2)):
    w3, bins3, patches3 = axs2[x, y].hist(shape2[n][-5000:], 25, normed=True, label='cartesian',fc=(0, 0, 1, 0.5))
    w4, bins4, patchse4 = axs2[x, y].hist(shape2[n+1][-5000:], 25, normed=True, label='modes', fc=(1, 0, 0, 0.5))

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
# fig1.savefig(molecule+'_'+shape_measure[0]+'.png', dpi=300)
# fig2.savefig(molecule+'_'+shape_measure[1]+'.png', dpi=300)
