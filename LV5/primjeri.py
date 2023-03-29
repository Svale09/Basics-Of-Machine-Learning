import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

yTrue = np.array([1,1,1,0,1,0,1,0,1])
yPred = np.array([0,1,1,1,1,0,1,0,0])

cm = confusion_matrix(yTrue, yPred)
print("Matrica zabune: ", cm)
disp = ConfusionMatrixDisplay(confusion_matrix(yTrue, yPred))
disp.plot()
plt.show()

print(classification_report(yTrue, yPred))