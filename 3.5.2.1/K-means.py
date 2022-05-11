import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


data_1 = np.random.randn(200, 2)+[1, 1]
data_2 = np.random.randn(200, 2)+[4, 4]
data_3 = np.random.randn(200, 2)+[7, 1]
data = np.concatenate((data_1, data_2, data_3), axis=0)
X_train, X_test = train_test_split(data, test_size=0.2)



def gen_center(X_train, k):
    n_sample = X_train.shape[0]
    n_feature = X_train.shape[1]


    f_mean = np.mean(X_train, axis=0).reshape((1, n_feature))
    f_std = np.std(X_train, axis=0).reshape((1, n_feature))
    centers = np.random.randn(k, n_feature)*f_std+f_mean
    return centers
k=3
centers = gen_center(X_train, k)


n_sample = X_train.shape[0]
clusters = np.zeros(n_sample)
dist = np.zeros((n_sample, k))
for i in range(k):
    dist[:, i] = np.linalg.norm(X_train-centers[i], axis=1)

clusters = np.argmin(dist, axis=1)
print(dist)
print(clusters)

for i in range(k):
    centers[i] = np.mean(X_train[clusters == i], axis=0)
print(clusters)


plt.clf()
plt.scatter(X_train[:, 0], X_train[:, 1], alpha=0.5, c=clusters)
plt.scatter(centers[:, 0], centers[:, 1], marker='*', c='k')
plt.show()





