import os
import sklearn
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import pickle


class BGTs:
    @staticmethod
    def predict(listFeatures):
        BGTsModel = BGTs.loadBGTsModel()
        KNNModel = BGTs.loadKNNModel()
        RFModel = BGTs.loadRFModel()
        names = ["non-vpn", "vpn"]
        predicted1 = BGTsModel.predict(listFeatures)
        predicted2 = KNNModel.predict(listFeatures)
        predicted3 = RFModel.predict(listFeatures)
        # print(f'predicted1 :{names[predicted1[0]]} predicted2 :{names[predicted2[0]]} predicted3 :{names[predicted3[0]]}')
        if (predicted1[0] == 0 and predicted2[0] == 0 and predicted3[0] == 0):
            return names[0]
        elif (predicted1[0] == 0 and predicted2[0] == 0):
            return names[0]
        elif (predicted1[0] == 0 and predicted3[0] == 0):
            return names[0]
        elif (predicted2[0] == 0 and predicted3[0] == 0):
            return names[0]
        else:
            return names[1]

    @staticmethod
    def loadBGTsModel():
        filename = 'meetup/ML/models/BGTs_model.sav'
        BGTsModel = pickle.load(open(filename, 'rb'))
        return BGTsModel

    @staticmethod
    def loadKNNModel():
        filename = 'meetup/ML/models/KNN_model.sav'
        KNNModel = pickle.load(open(filename, 'rb'))
        return KNNModel

    @staticmethod
    def loadRFModel():
        filename = 'meetup/ML/models/RF_model.sav'
        RFModel = pickle.load(open(filename, 'rb'))
        return RFModel
