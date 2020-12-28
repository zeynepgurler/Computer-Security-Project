import numpy as np

def preprocess_data():
    with open('kddcup.data_10_percent_corrected', 'r') as file:
        lines = file.readlines()
        x = 0
        list = []
        for line in lines:
            items = line.split(",")
            if x == 0:
                list.append(items[41])
            else:
                if items[41] not in list:
                    list.append(items[41])
            x = x + 1
        print(len(list))
        print(list)


def count_attacks():
    with open('kddcup.data_10_percent_corrected', 'r') as file:
        lines = file.readlines()
        x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        list = ['normal.\n', 'buffer_overflow.\n', 'loadmodule.\n', 'perl.\n', 'neptune.\n', 'smurf.\n', 'guess_passwd.\n', 'pod.\n', 'teardrop.\n', 'portsweep.\n', 'ipsweep.\n', 'land.\n', 'ftp_write.\n', 'back.\n', 'imap.\n', 'satan.\n', 'phf.\n', 'nmap.\n', 'multihop.\n', 'warezmaster.\n', 'warezclient.\n', 'spy.\n', 'rootkit.\n']
        for line in lines:
            items = line.split(",")
            i = list.index(items[41])
            print(i)
            x[i] = x[i] + 1

        print(x)

count_attacks()

def process_data(f):
    x = 0
    with open(f, 'r') as file:
        list2 = []
        count2 = 0
        list3 = []
        count3 = 0
        list41 = []
        count41 = 0
        data = np.empty((1, 42))
        lines = file.readlines()
        for line in lines:
            if x % 10 == 0:
                line = line[:-1]
                items = line.split(',')
                if items[1] == "tcp":
                    items[1] = 1
                elif items[1] == "udp":
                    items[1] = 2
                elif items[1] == "icmp":
                    items[1] = 3

                if items[2] not in list2:
                    count2 = count2 + 1
                    list2.append(items[2])
                    items[2] = count2
                else:
                    items[2] = list2.index(items[2]) + 1

                if items[3] not in list3:
                    count3 = count3 + 1
                    list3.append(items[3])
                    items[3] = count3
                else:
                    items[3] = list3.index(items[3]) + 1

                if items[41] not in list41:
                    count41 = count41 + 1
                    list41.append(items[41])
                    items[41] = count41
                else:
                    items[41] = list41.index(items[41]) + 1

                if x == 0:
                    data[0, :] = items
                else:
                    data = np.concatenate((data, [items]), axis=0)

            x = x + 1
            # print(x)
    data = data.astype('float')

    return data


# read the whole data
whole_data = process_data('kddcup.data_10_percent_corrected')
print("reading done")
for i in range(41):
    print(np.std(whole_data[:, i]))
data = whole_data[:, :41]
# labels
labels = whole_data[:, 41]
# normal data
normal = data[labels == 1]
center = np.mean(normal, axis=0)
print(center)


def distance_normal(center):
    data = np.empty((39,1))
    with open('kddcup.data_10_percent_corrected', 'r') as file:
        lines = file.readlines()
        x = 0
        list2 = []
        count2 = 0
        list3 = []
        count3 = 0
        first = center
        count = np.zeros((41), dtype=float)
        for line in lines:
            line = line[:-1]
            items = line.split(',')
            #if x == 0:
            #    first = items
            for i in range(41):
                if items[1] == "tcp":
                    items[1] = 1
                elif items[1] == "udp":
                    items[1] = 2
                elif items[1] == "icmp":
                    items[1] = 3

                if items[2] not in list2:
                    count2 = count2 + 1
                    list2.append(items[2])
                    items[2] = count2
                else:
                    items[2] = list2.index(items[2]) + 1

                if items[3] not in list3:
                    count3 = count3 + 1
                    list3.append(items[3])
                    items[3] = count3
                else:
                    items[3] = list3.index(items[3]) + 1

                #if not i == 1 and not i == 2 and not i == 3:
                if first[i] - float(items[i]) < 0.05:
                    count[i] = count[i] + 1
            x = x + 1
    count = count / x
    for i in range(41):
        if float(count[i]) <= 0.80:
            print(i)
    print(count)

'''
center ofthe normal operations
center = [2.22968332e+02, 1.22331894e+00, 3.64085955e+00, 1.06343821e+00,
 1.18676547e+03, 3.61481925e+03, 1.02817191e-04, 0.00000000e+00,
 0.00000000e+00, 4.24634999e-02, 0.00000000e+00, 7.19103434e-01,
 3.49578450e-03, 0.00000000e+00, 1.02817191e-04, 3.47522106e-02,
 5.34649393e-03, 2.05634382e-04, 4.00987045e-03, 0.00000000e+00,
 0.00000000e+00, 4.31832202e-03, 8.11063130e+00, 1.09150730e+01,
 1.56179313e-03, 1.82294880e-03, 5.59880732e-02, 5.61340736e-02,
 9.85672424e-01, 1.78788813e-02, 1.29513675e-01, 1.48751696e+02,
 2.01397800e+02, 8.41841456e-01, 5.66831174e-02, 1.33553362e-01,
 2.43162657e-02, 2.12009048e-03, 1.13921448e-03, 5.80968538e-02,
 5.62811022e-02]
'''

distance_normal(center)


def vr_success():
    data = np.empty((39,1))
    with open('kddcup.data_10_percent_corrected', 'r') as file:
        lines = file.readlines()
        x = 0
        count = np.zeros((42), dtype=float)
        for line in lines:
            items = line.split(",")
            if x == 0:
                first = items
            for i in range(42):
                if first[i] == items[i]:
                    count[i] = count[i] + 1
            x = x + 1
    count = count / x
    for i in range(42):
        if float(count[i]) <= 0.80:
            print(i)
    print(count)

preprocess_data()
