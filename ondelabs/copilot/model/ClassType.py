'''
Created on 3 Aug 2014

@author: ankur
'''

class ClassType:
    
    def __init__(self, classType, wordCount):
        self.__classType = classType
        self.__totalOccurrence = 0
        self.__totalWordCount = 0
        self.__prior = 0
        self.incrementOccurrence(wordCount)
    
    def incrementOccurrence(self, wordCount):
        self.__totalOccurrence = self.__totalOccurrence + 1
        self.__totalWordCount = self.__totalWordCount + wordCount
    
    def getTotalNonUniqueWordsCountInClass(self):
        return self.__totalWordCount
    
    def getClassType(self):
        return self.__classType
    
    def getTotalOccurrence(self):
        return self.__totalOccurrence
    
    def getPrior(self):
        return self.__prior
    
    def setPrior(self, prior):
        self.__prior = prior
    