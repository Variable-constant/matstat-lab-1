import numpy as np
from scipy.stats import bernoulli

np.random.seed(0)

eps = 0.1
p = 0.4
size = 97

cnt = 0
for i in range(100):
    sample = bernoulli(p).rvs(size=size)
    avg = np.average(sample)
    if abs(avg - p) > eps:
        cnt += 1

print(f'Число выборок, для которых выборочное среднее отличается от теоретического математического ожидания более чем '
      f'на {eps}: {cnt}')
