'''
Created on 14 Aug 2014

@author: ankur
'''


class TestPrediction:

    def __init__(self, originalLine, prediction):
        self.__originalLine = originalLine
        self.__prediction = prediction

    def getOriginalLine(self):
        return self.__originalLine

    def getPrediction(self):
        return self.__prediction
