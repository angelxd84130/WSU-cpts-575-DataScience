from sklearn import svm
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])

clf = svm.SVC(kernel='rbf')
clf.fit(X, y)
print("prediction:", clf.predict([[0.8, -1]]))



