'''
Created on 14 Aug 2014

@author: ankur
'''
from ondelabs.copilot.model.TestPrediction import TestPrediction


class TestResult:

    def __init__(self):
        self.__predictionResult = []
        self.__totalPredictions = 0

    def addPrediction(self, key, prediction):
        self.__predictionResult.append(TestPrediction(key, prediction))
        self.__totalPredictions = self.__totalPredictions + 1

    def getTotalPredictions(self):
        return self.__totalPredictions

    def getPredictionResults(self):
        return self.__predictionResult
