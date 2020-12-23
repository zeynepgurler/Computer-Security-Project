import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm


def process_data(f):
    x = 0
    with open(f, 'r') as file:
        data = np.empty((1, 16), dtype=float)
        lines = file.readlines()
        for line in lines:
            line = line[:-1]
            items = line.split(',')
            if x == 0:
                x = x + 1
                data[0, :] = items[:]
            else:
                data = np.concatenate((data, [items[:]]), axis=0)
    data = data.astype('float')

    return data


# read the whole data
whole_data = process_data('data.txt')
# only features
data = whole_data[:, :15]
# labels
labels = whole_data[:, 15]
# make the id of the whole type of attacks 0 and keep normal operations as 1
labels[labels != 1] = 0

# normalize data
for i in range(data.shape[1]):
    data[:, i] = data[:, i] / np.linalg.norm(data[:, i])

# split data into 2 as train and test
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.5, random_state=0)
# define the classifier as support vector machine
clf = svm.SVC()
# fit the training data and their labels to the classifier model
clf.fit(X_train, y_train)
# predict the labels of the test samples
y_pred = clf.predict(X_test)
print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
print("Classification accuracy: %f" % ((X_test.shape[0] - (y_test != y_pred).sum()) / X_test.shape[0] * 100.0))
