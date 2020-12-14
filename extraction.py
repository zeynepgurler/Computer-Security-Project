import os
import numpy as np

def preprocess_data():
    data = np.empty((16, 1), dtype=float)
    temp = np.empty((16, 1), dtype=float)

    with open('data.txt', 'w+') as out:
        with open('kddcup.data_10_percent_corrected', 'r') as file:
            lines = file.readlines()
            x = 0
            list2 = []
            count2 = 0
            list3 = []
            count3 = 0
            list41 = []
            count41 = 0
            for line in lines:
                items = line.split(",")
                for i in range(42):
                    if i == 1:
                        # tcp or icmp or udp
                        if items[i] == "tcp":
                            out.write("0,")
                        elif items[i] == "udp":
                            out.write("1,")
                        else:
                            out.write("2,")
                    if i == 2:
                        if items[2] not in list2:
                            count2 = count2 + 1
                            list2.append(items[2])
                            out.write(str(count2))
                            out.write(",")
                        else:
                            out.write(str(count2))
                            out.write(",")
                    if i == 3:
                        if items[3] not in list3:
                            count3 = count3 + 1
                            list3.append(items[3])
                            out.write(str(count3))
                            out.write(",")
                        else:
                            out.write(str(count3))
                            out.write(",")
                    if(i == 4 or i == 5 or i == 11 or i == 22 or i == 23 or i == 28 or i == 29 or i == 31 or i == 32 or i == 33 or i == 34 or i == 35):
                        out.write(str(items[i]))
                        out.write(",")
                    if i == 41:
                        if items[41] not in list41:
                            print(items[41])
                            count41 = count41 + 1
                            list41.append(items[41])
                            out.write(str(count41))
                        else:
                            out.write(str(count41))
                out.write("\n")
                if x == 0:
                    print(x)
                    print(out)
                    x = 1
preprocess_data()


'''
def preprocess_data():
    data = np.empty((16, 1), dtype=float)
    temp = np.empty((16, 1), dtype=float)
    with open('kddcup.data_10_percent_corrected', 'r') as file:
        lines = file.readlines()
        x = 0
        list2 = []
        count2 = 0
        list3 = []
        count3 = 0
        list41 = []
        count41 = 0
        for line in lines:
            items = line.split(",")
            j = 0
            for i in range(42):
                if i == 1:
                    # tcp or icmp or udp
                    if items[i] == "tcp":
                        if x == 0:
                            data[j] = 0
                        else:
                            temp[i] = 0
                    elif items[i] == "udp":
                        if x == 0:
                            data[j] = 1
                        else:
                            temp[i] = 1
                    else:
                        if x == 0:
                            data[j] = 2
                        else:
                            temp[i] = 2
                    j = j + 1
                if i == 2:
                    if x == 0:
                        list2.append(items[2])
                        data[j] = count2
                    else:
                        if items[2] not in list:
                            count2 = count2 + 1
                            list2.append(items[2])
                            temp[j] = count2
                        else:
                            temp[j] = count2
                    j = j + 1
                if i == 3:
                    if x == 0:
                        list3.append(items[3])
                        data[j] = count3
                    else:
                        if items[3] not in list:
                            count3 = count3 + 1
                            list3.append(items[3])
                            temp[j] = count3
                        else:
                            temp[j] = count3
                    j = j + 1
                if(i == 4 or i == 5 or i == 11 or i == 22 or i == 23 or i == 28 or i == 29 or i == 31 or i == 32 or i == 33 or i == 34 or i == 35):
                    if x == 0:
                        data[j] = items[i]
                    else:
                        temp[j] = items[i]
                    j = j + 1
                if i == 41:
                    if x == 0:
                        list41.append(items[41])
                        data[j] = count41
                    else:
                        if items[41] not in list:
                            count41 = count41 + 1
                            list3.append(items[41])
                            temp[j] = count41
                        else:
                            temp[j] = count41
                    j = j + 1
            data = np.append(data, temp, axis=0)
    print(data)
preprocess_data()
'''