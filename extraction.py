import numpy as np


def preprocess_data_std():
    with open('data3.txt', 'w+') as out:
        with open('kddcup.data_10_percent_corrected', 'r') as file:
            lines = file.readlines()
            x = 0
            list2 = []
            count2 = 0
            list3 = []
            count3 = 0
            list41 = []
            count41 = 0
            list900 = ['normal.\n', 'neptune.\n',  'smurf.\n',  'teardrop.\n', 'portsweep.\n', 'ipsweep.\n', 'back.\n', 'satan.\n', 'warezclient.\n']
            for line in lines:
                items = line.split(",")
                if items[41] in list900:
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
                                out.write(str(list2.index(items[2]) + 1))
                                out.write(",")
                        if i == 3:
                            if items[3] not in list3:
                                count3 = count3 + 1
                                list3.append(items[3])
                                out.write(str(count3))
                                out.write(",")
                            else:
                                out.write(str(list3.index(items[3]) + 1))
                                out.write(",")
                        if i == 0 or i == 4 or i == 5 or i == 9 or i == 21 or i == 22 or i == 23 or i == 24 or i == 25 or i == 28 or i == 31 or i == 32 or i == 33 or i == 35 or i == 37 or i == 38:
                            out.write(str(items[i]))
                            out.write(",")
                        if i == 41:
                            if items[41] not in list41:
                                print(items[41])
                                count41 = count41 + 1
                                print(count41)
                                list41.append(items[41])
                                out.write(str(count41))
                            else:
                                out.write(str(list41.index(items[41]) + 1))
                    out.write("\n")
preprocess_data()


def preprocess_data_vr():
    with open('data3.txt', 'w+') as out:
        with open('kddcup.data_10_percent_corrected', 'r') as file:
            lines = file.readlines()
            x = 0
            list2 = []
            count2 = 0
            list3 = []
            count3 = 0
            list41 = []
            count41 = 0
            list900 = ['normal.\n', 'neptune.\n',  'smurf.\n',  'teardrop.\n', 'portsweep.\n', 'ipsweep.\n', 'back.\n', 'satan.\n', 'warezclient.\n']
            for line in lines:
                items = line.split(",")
                if items[41] in list900:
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
                                out.write(str(list2.index(items[2]) + 1))
                                out.write(",")
                        if i == 3:
                            if items[3] not in list3:
                                count3 = count3 + 1
                                list3.append(items[3])
                                out.write(str(count3))
                                out.write(",")
                            else:
                                out.write(str(list3.index(items[3]) + 1))
                                out.write(",")
                        if i == 4 or i == 5 or i == 11 or i == 22 or i == 23 or i == 28 or i == 29 or i == 31 or i == 32 or i == 33 or i == 34 or i == 35:
                            out.write(str(items[i]))
                            out.write(",")
                        if i == 41:
                            if items[41] not in list41:
                                print(items[41])
                                count41 = count41 + 1
                                print(count41)
                                list41.append(items[41])
                                out.write(str(count41))
                            else:
                                out.write(str(list41.index(items[41]) + 1))
                    out.write("\n")
preprocess_data_vr()

