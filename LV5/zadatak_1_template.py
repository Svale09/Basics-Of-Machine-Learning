import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, classification_report


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)


# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

plt.scatter(X_train[:,0], X_train[:,1], s=3, c=y_train,cmap = "bwr")
plt.scatter(X_test[:,0], X_test[:,1], c=y_test, marker="x", cmap="bwr")


LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train,y_train)

y_test_p = LogRegression_model.predict(X_test)

print(LogRegression_model.intercept_)
print(LogRegression_model.coef_)

b = LogRegression_model.intercept_
w1, w2 = LogRegression_model.coef_.T

c = -b/w2
m = -w1/w2

xmin, xmax = -4, 4
ymin, ymax = -4, 4
xd = np.array([xmin, xmax])
yd = m*xd+c

plt.plot(xd, yd, "k", lw = 1, ls = "--")
plt.show()

cm = confusion_matrix(y_test, y_test_p)
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot()
plt.show()

print(classification_report(y_test, y_test_p))

#Prikažite skup za testiranje u ravnini x1−x2. Zelenom bojom oznacite dobro klasificirane
# primjere dok pogrešno klasificirane primjere oznacite crnom bojom.
y_color = (y_test == y_test_p)
plt.figure()
plt.scatter(X_test[:, 0], X_test[:, 1], marker="o", c=y_color, s=15, cmap=mcolors.ListedColormap(["black", "green"]))
print(y_color)
plt.show()