'''
Created on 14 Aug 2014

@author: ankur
'''
import math
from ondelabs.copilot.model.TestResult import TestResult


class TestData:

    def __init__(self, lines):
        self.__words = lines

    def test(self, classes, lexicon):
        testResult = TestResult()

        allClassTypes = classes.getAllClassTypes()

        for key in self.__words.keys():
            validationText = self.__words[key]
            classResult = {}
            for classTypeKey in allClassTypes:
                classType = classes.getClass(classTypeKey)
                words = validationText.getWords()
                prob = math.log(classType.getPrior())
                for word in words:
                    conProb = lexicon.getConditionalProbability(word, classTypeKey)
                    if conProb != 0:
                        prob = prob + math.log(conProb)
                classResult[classTypeKey] = prob
            prediction = self.__findClassTypeWithHighestProb(classResult)
            testResult.addPrediction(key, prediction)
        return testResult

    def __findClassTypeWithHighestProb(self, probs):
        bestClassType = -1
        highestProb = -9999999

        for key in probs.keys():
            if probs[key] > highestProb:
                highestProb = probs[key]
                bestClassType = key

        return bestClassType

    def getTotalValidationTestDataPoints(self):
        return len(self.__words)
