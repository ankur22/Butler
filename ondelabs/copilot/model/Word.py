'''
Created on 3 Aug 2014

@author: ankur
'''

class Word:
    
    def __init__(self, text, classType):
        self.__text = text
        self.__probability = {}
        self.__totalOccurrence = 0
        self.__occurrenceInClassType = {}
        self.incrementOccurrence(classType)
    
    def incrementOccurrence(self, classType):
        self.__totalOccurrence = self.__totalOccurrence + 1
        
        if self.__occurrenceInClassType.has_key(classType):
            self.__occurrenceInClassType[classType] = self.__occurrenceInClassType[classType] + 1
        else:
            self.__occurrenceInClassType[classType] = 1
    
    def getOccurrenceInClass(self, classType):
        occurrenceInClass = self.__occurrenceInClassType.get(classType)
        if occurrenceInClass is None:
            return 0
        else:
            return occurrenceInClass
    
    def setConditionalProbability(self, classType, conProb):
        self.__probability[classType] = conProb
    
    def getConditionalProbability(self, classType):
        return self.__probability[classType]
    