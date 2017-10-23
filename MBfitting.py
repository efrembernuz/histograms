import scipy.stats as stats
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

alpha = 5
loc = 100.5
beta = 22
data = stats.gamma.rvs(alpha, loc=loc, scale=beta, size=10000)
print(data)

fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data)
print(fit_alpha, fit_loc, fit_beta)

print(alpha, loc, beta)
a, loc, scale = 3, 0, 2
size = 20000
y = stats.gamma.rvs(a, loc, scale, size=size)
print(y)
quit()

df = 20
data2 = stats.chi2.rvs(df, size=10000)
print(data)
fit_df = stats.chi2.fit(data2)
print(fit_df)
ax.hist(data2, normed=True, histtype='stepfilled', alpha=0.2)

plt.show()

# x = 2*np.sqrt((x)/np.pi)*np.sqrt(1/(k*T)**3)*np.exp(-(x)/(k*T))
