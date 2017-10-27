import matplotlib.pyplot as plt
import numpy as np


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


molecule = 'cyclohexane'
kind = ['cartesian', 'modes']
temperature = [400]
files = []
bins = 10
n_max = 5000

for temp in temperature:
    for i in kind:
        files.append(molecule+'_'+str(temp)+'_'+i+'_shape')
shape1 = [[] for i in range(len(files))]


for n, file in enumerate(files):
    with open('results/'+file+'.txt') as in_file:
        for line in nonblank_lines(in_file):
            if any(s in line for s in ['-', 'Shape', '#']):
                pass
            else:
                shape1[n].append(float(line.split()[1]))


n_mostres = np.linspace(1000, n_max, num=bins, dtype=int)
mean_square1 = []
mean_square2 = []
sub_mean_square1 = []
sub_mean_square2 = []
w1, bins = np.histogram(shape1[0][-n_max:], bins, normed=True)
w2, bins = np.histogram(shape1[1][-n_max:], bins, normed=True)

w = w1+w2
mean = w/2

for idx, number in enumerate(n_mostres):
    slices = int(n_max/number)
    sub_mean_square1 = []
    sub_mean_square2 = []
    for n in list(range(slices)):
        w1, bins2 = np.histogram(shape1[0][-number*(n+1):-(number*n + 1)],  bins, normed=True)
        w2, bins3 = np.histogram(shape1[1][-number*(n+1):-(number*n + 1)],  bins, normed=True)
        sub_mean_square1.append(np.sqrt(((w1-mean)**2).sum()/len(w1)))
        sub_mean_square2.append(np.sqrt(((w2-mean)**2).sum()/len(w2)))
    mean_square1.append(sum(sub_mean_square1)/slices)
    mean_square2.append(sum(sub_mean_square2)/slices)

plt.title('Temperature: {} K'.format(temperature[0]), fontsize=10, horizontalalignment='center')
plt.plot(n_mostres, mean_square1, label='cartesian')
plt.plot(n_mostres, mean_square2, label='modes')
plt.legend()
plt.show()