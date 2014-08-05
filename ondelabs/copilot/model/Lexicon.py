'''
Created on 3 Aug 2014

@author: ankur
'''
from ondelabs.copilot.model.Word import Word


class Lexicon:
    
    def __init__(self):
        self.__words = {}
        self.__numUniqueWords = 0
    
    def addWords(self, words, classType):
        for text in words:
            self.__addWord(text, classType)
    
    def __addWord(self, text, classType):
        if self.__words.has_key(text):
            self.__words[text].incrementOccurrence(classType)
        else:
            self.__words[text] = Word(text, classType)
            self.__numUniqueWords = self.__numUniqueWords + 1
    
    def calculateConditionalProbability(self, classes):
        
        allClassTypes = classes.getAllClassTypes()
        for classTypeKey in allClassTypes:
            for word in self.__words.values():
                classType = classes.getClass(classTypeKey)
                # To eliminate zeros, we use add-one or Laplace smoothing, which simply adds one
                denominator = classType.getTotalNonUniqueWordsCountInClass() + self.__numUniqueWords
                numerator = word.getOccurrenceInClass(classType.getClassType()) + 1
                conProb = float(numerator) / float(denominator)
                word.setConditionalProbability(classType.getClassType(), conProb)
    
    def getConditionalProbability(self, text, classType):
        if self.__words.has_key(text):
            word = self.__words[text]
            conProb = word.getConditionalProbability(classType)
            if conProb is None:
                return 0
            else:
                return conProb
        else:
            return 0
    