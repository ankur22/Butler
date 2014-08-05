'''
Created on 3 Aug 2014

@author: ankur
'''


class TextClassType:
    
    def __init__(self, text, classType):
        self.__classType = classType
        self.__separatedWords = self.__extractWords(text)
    
    def __extractWords(self, text):
        extractedText = text.split()
        textOnlyExtractWords = []
        
        for word in extractedText:
            if self.__isNumber(word) is False:
                textOnlyExtractWords.append(word)
                
        return textOnlyExtractWords
    
    def __isNumber(self, text):
        try:
            float(text)
            return True
        except ValueError:
            return False
    
    def getWords(self):
        return self.__separatedWords
    
    def getClassType(self):
        return self.__classType
    