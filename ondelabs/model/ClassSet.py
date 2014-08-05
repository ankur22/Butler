'''
Created on 5 Aug 2014

@author: ankur
'''

class ClassSet:
    
    def __init__(self):
        self.__trainClassTypes = [];
        self.__valClassTypes = [];
        
    def addClassType(self, classType):
        if classType.isTrain():
            self.__trainClassTypes.append(classType)
        else:
            self.__valClassTypes.append(classType)
    
    def getTrainingClassTypes(self):
        result = ''
        for classType in self.__trainClassTypes:
            result = result + classType.getKeywordsAndClassType()
        return result
    
    def getValidationClassTypes(self):
        result = ''
        for classType in self.__valClassTypes:
            result = result + classType.getKeywordsAndClassType()
        return result
        