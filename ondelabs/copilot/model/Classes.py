'''
Created on 3 Aug 2014

@author: ankur
'''
from ondelabs.copilot.model.ClassType import ClassType


class Classes:
    
    def __init__(self):
        self.__classes = {}
        self.__totalNonUniqueClasses = 0
    
    def addClass(self, classType, wordCount):        
        if self.__classes.has_key(classType):
            self.__classes[classType].incrementOccurrence(wordCount)
        else:
            self.__classes[classType] = ClassType(classType, wordCount)
            
        self.__totalNonUniqueClasses = self.__totalNonUniqueClasses + 1
        
        return True
        
    def calculatePrior(self):
        for classType in self.__classes.values():
            classType.setPrior(float(classType.getTotalOccurrence()) / float(self.__totalNonUniqueClasses))
    
    def getAllClassTypes(self):
        return self.__classes.keys()
    
    def getClass(self, classType):
        return self.__classes[classType]
    
    def getPrior(self, classType):
        return self.__prior[classType]
    