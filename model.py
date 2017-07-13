"""
    skeleton code
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import preprocessing


features_train, features_test, labels_train, labels_test = preprocessing.preprocess()

clf = DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)
predict = clf.predict(features_test)


accuracy = accuracy_score(labels_test, predict)
print(accuracy)
