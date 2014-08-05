'''
Created on 4 Aug 2014

@author: ankur
'''
from ondelabs.copilot.model.ValidationPrediction import ValidationPrediction


class ValidationResult:
    
    def __init__(self):
        self.__predictionResult = []
        self.__totalPredictions = 0
        self.__accuracy = 0
    
    def addPrediction(self, key, prediction, actual):
        self.__predictionResult.append(ValidationPrediction(key, prediction, actual))
        self.__totalPredictions = self.__totalPredictions + 1
        self.__accuracy
    
    def calculateAccuracy(self):
        correctPredictionCount = 0
        
        for prediction in self.__predictionResult:
            if prediction.getPrediction() == prediction.getActual():
                correctPredictionCount = correctPredictionCount + 1
        
        self.__accuracy = (float(correctPredictionCount) / float(self.__totalPredictions)) * 100

    def getAccuracy(self):
        return self.__accuracy

    def getTotalPredictions(self):
        return self.__totalPredictions
    