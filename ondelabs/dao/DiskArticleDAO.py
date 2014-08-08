'''
Created on 5 Aug 2014

@author: ankur
'''
import os

from ondelabs.model.ClassSet import ClassSet
from ondelabs.model.ClassType import ClassType


class DiskArticleDAO:
    
    def __init__(self):
        self.__rootDir = 'resource/'
        self.__trainingPath = 'resource/training.txt'
        self.__validationPath = 'resource/validation.txt'
    
    def loadArticles(self):
        return self.__scanForFolders(self.__rootDir)
    
    def __scanForFolders(self, directory):
        classSet = ClassSet()
        for root, subFolders, files in os.walk(directory):
            for folder in subFolders:
                classType = self.__scanForFiles(os.path.join(directory, folder), folder)
                classSet.addClassType(classType)
        return classSet
                
    def __scanForFiles(self, path, folderName):
        classType = ClassType(folderName)
        for root, subFolders, files in os.walk(path):
            for filename in files:
                if 'txt' in filename:
                    filepath = os.path.join(root, filename)
                    article = self.__readArticle(filepath)
                    classType.addDocument(article)
        return classType
    
    def __readArticle(self, filepath):
        f = open(filepath, 'r')
        article = f.read()
        f.close()
        return article
    
    def writeTrainingClassSet(self, classSet):
        f = open(self.__trainingPath, 'w')
        f.write(classSet.getTrainingClassTypes())
        f.close()
        
    def writeValidationClassSet(self, classSet):
        f = open(self.__validationPath, 'w')
        f.write(classSet.getValidationClassTypes())
        f.close()
    