import time
import sqlite3
import os
import pickle
import math
import pandas

def getRMSE(list1,list2):
    error=0
    for i in range(len(list1)):
        error+=math.pow(list1[i]-list2[i],2)
    error=error/len(list1)
    error=math.sqrt(error)
    return error

def getTestScores():
    row = pandas.read_csv("test_data_500_KNN.csv",header= None)
    actual_50_500 = []
    actual_100_500 = []
    actual_250_500 = []
    actual_500_500 = []
    predicted_50_500 = []
    predicted_100_500 = []
    predicted_250_500 = []
    predicted_500_500 = []
    actual_50_1000 = []
    actual_100_1000 = []
    actual_250_1000 = []
    actual_500_1000 = []
    predicted_50_1000 = []
    predicted_100_1000 = []
    predicted_250_1000 = []
    predicted_500_1000 = []
    actual_50_5000 = []
    actual_100_5000 = []
    actual_250_5000 = []
    actual_500_5000 = []
    predicted_50_5000 = []
    predicted_100_5000 = []
    predicted_250_5000 = []
    predicted_500_5000 = []

    for i in range(len(row)):
        if row[5][i] == 50:
            if row[4][i] == 500:
                predicted_50_500.append(row[2][i])
                actual_50_500.append(row[3][i])
            elif row[4][i] == 1000:
                predicted_50_1000.append(row[2][i])
                actual_50_1000.append(row[3][i])
            else:
                predicted_50_5000.append(row[2][i])
                actual_50_5000.append(row[3][i])
        elif row[5][i] == 100:
            if row[4][i] == 500:
                predicted_100_500.append(row[2][i])
                actual_100_500.append(row[3][i])
            elif row[4][i] == 1000:
                predicted_100_1000.append(row[2][i])
                actual_100_1000.append(row[3][i])
            else:
                predicted_100_5000.append(row[2][i])
                actual_100_5000.append(row[3][i])
        elif row[5][i] == 250:
            if row[4][i] == 500:
                predicted_250_500.append(row[2][i])
                actual_250_500.append(row[3][i])
            elif row[4][i] == 1000:
                predicted_250_1000.append(row[2][i])
                actual_250_1000.append(row[3][i])
            else:
                predicted_250_5000.append(row[2][i])
                actual_250_5000.append(row[3][i])
        else:
            if row[4][i] == 500:
                predicted_500_500.append(row[2][i])
                actual_500_500.append(row[3][i])
            elif row[4][i] == 1000:
                predicted_500_1000.append(row[2][i])
                actual_500_1000.append(row[3][i])
            else:
                predicted_500_5000.append(row[2][i])
                actual_500_5000.append(row[3][i])
    with open("KNN_500_RMSE_result.txt","wt") as r:
        r.write("\nFor k=50\n")
        rmse = getRMSE(actual_50_500,predicted_50_500)
        r.write("\n\tFor 500dB, RMSE is  = " + str(rmse))
        rmse = getRMSE(actual_50_1000,predicted_50_1000)
        r.write("\n\tFor 1000dB, RMSE is  = " + str(rmse))
        # rmse = getRMSE(actual_50_5000,predicted_50_5000)
        # r.write("\n\tFor 5000dB, RMSE is  = " + str(rmse))
        r.write("\nFor k=100\n")
        rmse = getRMSE(actual_100_500,predicted_100_500)
        r.write("\n\tFor 500dB, RMSE is  = " + str(rmse))
        rmse = getRMSE(actual_100_1000,predicted_100_1000)
        r.write("\n\tFor 1000dB, RMSE is  = " + str(rmse))
        # rmse = getRMSE(actual_100_5000,predicted_100_5000)
        # r.write("\n\tFor 5000dB, RMSE is  = " + str(rmse))
        r.write("\nFor k=250\n")
        rmse = getRMSE(actual_250_500,predicted_250_500)
        r.write("\n\tFor 500dB, RMSE is  = " + str(rmse))
        rmse = getRMSE(actual_250_1000,predicted_250_1000)
        r.write("\n\tFor 1000dB, RMSE is  = " + str(rmse))
        # rmse = getRMSE(actual_250_5000,predicted_250_5000)
        # r.write("\n\tFor 5000dB, RMSE is  = " + str(rmse))
        r.write("\nFor k=500\n")
        rmse = getRMSE(actual_500_500,predicted_500_500)
        r.write("\n\tFor 500dB, RMSE is  = " + str(rmse))
        rmse = getRMSE(actual_500_1000,predicted_500_1000)
        r.write("\n\tFor 1000dB, RMSE is  = " + str(rmse))
        # rmse = getRMSE(actual_500_5000,predicted_500_5000)
        # r.write("\n\tFor 5000dB, RMSE is  = " + str(rmse))



def getRoundedTestScores():
    row = pandas.read_csv("test_data_500_KNN.csv",header= None)
    actual_50_500 = []
    actual_100_500 = []
    actual_250_500 = []
    actual_500_500 = []
    predicted_50_500 = []
    predicted_100_500 = []
    predicted_250_500 = []
    predicted_500_500 = []
    actual_50_1000 = []
    actual_100_1000 = []
    actual_250_1000 = []
    actual_500_1000 = []
    predicted_50_1000 = []
    predicted_100_1000 = []
    predicted_250_1000 = []
    predicted_500_1000 = []
    actual_50_5000 = []
    actual_100_5000 = []
    actual_250_5000 = []
    actual_500_5000 = []
    predicted_50_5000 = []
    predicted_100_5000 = []
    predicted_250_5000 = []
    predicted_500_5000 = []

    for i in range(len(row)):
        if row[5][i] == 50:
            if row[4][i] == 500:
                predicted_50_500.append(round(row[2][i]))
                actual_50_500.append(row[3][i])
            elif row[4][i] == 1000:
                predicted_50_1000.append(round(row[2][i]))
                actual_50_1000.append(row[3][i])
            else:
                predicted_50_5000.append(round(row[2][i]))
                actual_50_5000.append(row[3][i])
        elif row[5][i] == 100:
            if row[4][i] == 500:
                predicted_100_500.append(round(row[2][i]))
                actual_100_500.append(row[3][i])
            elif row[4][i] == 1000:
                predicted_100_1000.append(round(row[2][i]))
                actual_100_1000.append(row[3][i])
            else:
                predicted_100_5000.append(round(row[2][i]))
                actual_100_5000.append(row[3][i])
        elif row[5][i] == 250:
            if row[4][i] == 500:
                predicted_250_500.append(round(row[2][i]))
                actual_250_500.append(row[3][i])
            elif row[4][i] == 1000:
                predicted_250_1000.append(round(row[2][i]))
                actual_250_1000.append(row[3][i])
            else:
                predicted_250_5000.append(round(row[2][i]))
                actual_250_5000.append(row[3][i])
        else:
            if row[4][i] == 500:
                predicted_500_500.append(round(row[2][i]))
                actual_500_500.append(row[3][i])
            elif row[4][i] == 1000:
                predicted_500_1000.append(round(row[2][i]))
                actual_500_1000.append(row[3][i])
            else:
                predicted_500_5000.append(round(row[2][i]))
                actual_500_5000.append(row[3][i])
    with open("KNN_500_Rounded_RMSE_result.txt","wt") as r:
        r.write("\nFor k=50\n")
        rmse = getRMSE(actual_50_500,predicted_50_500)
        r.write("\n\tFor 500dB, RMSE is  = " + str(rmse))
        rmse = getRMSE(actual_50_1000,predicted_50_1000)
        r.write("\n\tFor 1000dB, RMSE is  = " + str(rmse))
        # rmse = getRMSE(actual_50_5000,predicted_50_5000)
        # r.write("\n\tFor 5000dB, RMSE is  = " + str(rmse))
        r.write("\nFor k=100\n")
        rmse = getRMSE(actual_100_500,predicted_100_500)
        r.write("\n\tFor 500dB, RMSE is  = " + str(rmse))
        rmse = getRMSE(actual_100_1000,predicted_100_1000)
        r.write("\n\tFor 1000dB, RMSE is  = " + str(rmse))
        # rmse = getRMSE(actual_100_5000,predicted_100_5000)
        # r.write("\n\tFor 5000dB, RMSE is  = " + str(rmse))
        r.write("\nFor k=250\n")
        rmse = getRMSE(actual_250_500,predicted_250_500)
        r.write("\n\tFor 500dB, RMSE is  = " + str(rmse))
        rmse = getRMSE(actual_250_1000,predicted_250_1000)
        r.write("\n\tFor 1000dB, RMSE is  = " + str(rmse))
        # rmse = getRMSE(actual_250_5000,predicted_250_5000)
        # r.write("\n\tFor 5000dB, RMSE is  = " + str(rmse))
        r.write("\nFor k=500\n")
        rmse = getRMSE(actual_500_500,predicted_500_500)
        r.write("\n\tFor 500dB, RMSE is  = " + str(rmse))
        rmse = getRMSE(actual_500_1000,predicted_500_1000)
        r.write("\n\tFor 1000dB, RMSE is  = " + str(rmse))
        # rmse = getRMSE(actual_500_5000,predicted_500_5000)
        # r.write("\n\tFor 5000dB, RMSE is  = " + str(rmse))



# getTestScores()

getRoundedTestScores()