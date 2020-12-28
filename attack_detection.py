import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm


def process_data(f, features):
    x = 0
    with open(f, 'r') as file:
        data = np.empty((1, features), dtype=float)
        lines = file.readlines()
        for line in lines:
            if x % 10 == 0:
                line = line[:-1]
                items = line.split(',')
                if x == 0:
                    data[0, :] = items[:]
                else:
                    data = np.concatenate((data, [items[:]]), axis=0)

            x = x + 1
    data = data.astype('float')

    return data


# number of features in the dataset
features = 16
# read the whole data
whole_data = process_data('data3.txt', features)
print("reading done")
# only features
data = whole_data[:, :features - 1]
# labels
labels = whole_data[:, features - 1]

for i in range(1, 10):
    print((labels == i).sum())

# make the id of the whole type of attacks 0 and keep normal operations as 1 if you want to only classify as attack, not attack
#labels[labels != 1] = 0

# normalize data
for i in range(data.shape[1]):
    data[:, i] = data[:, i] / np.linalg.norm(data[:, i])

# split data into 2 as train and test
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.35, random_state=0)
# define the classifier as support vector machine
clf = svm.SVC()
# fit the training data and their labels to the classifier model
print("training")
clf.fit(X_train, y_train)
# predict the labels of the test samples
y_pred = clf.predict(X_test)
# calculating misclassifications
mis = []
for x in range(1, 10):
    index = [i for i, j in enumerate(y_test) if j == x]
    print((y_test[index] != y_pred[index]).sum())
    print(len(y_test[index]))
    mis.append((y_test[index] != y_pred[index]).sum() / len(y_test[index]))

for i in range(9):
    print("Classification accuracy: %f" % (mis[i]))
print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
print("Classification accuracy: %f" % ((X_test.shape[0] - (y_test != y_pred).sum()) / X_test.shape[0] * 100.0))
