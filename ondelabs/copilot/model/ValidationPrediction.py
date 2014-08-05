'''
Created on 4 Aug 2014

@author: ankur
'''

class ValidationPrediction:
    
    def __init__(self, key, prediction, actual):
        self.__key = key
        self.__prediction = prediction
        self.__actual = actual
    
    def getKey(self):
        return self.__key
    
    def getPrediction(self):
        return self.__prediction
    
    def getActual(self):
        return self.__actual
    