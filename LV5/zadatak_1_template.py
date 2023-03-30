import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)


# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

plt.scatter(X_train[:,0], X_train[:,1], s=3, c=y_train,cmap = "bwr")
plt.scatter(X_test[:,0], X_test[:,1], c=y_test, marker="x", cmap="bwr")
plt.show()
