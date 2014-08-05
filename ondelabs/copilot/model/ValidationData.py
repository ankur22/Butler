'''
Created on 3 Aug 2014

@author: ankur
'''
import math

from ondelabs.copilot.model.ValidationResult import ValidationResult


class ValidationData:
    
    def __init__(self, lines):
        self.__words = lines
    
    def validate(self, classes, lexicon):
        validationResult = ValidationResult()
        
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
            validationResult.addPrediction(key, prediction, validationText.getClassType())
        validationResult.calculateAccuracy()
        return validationResult
    
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
        
        