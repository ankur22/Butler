'''
Created on 5 Aug 2014

@author: ankur
'''
import re

from topia.termextract import tag, extract
from topia.termextract.extract import TermExtractor, permissiveFilter


class ClassType:
    
    def __init__(self, classType):
        self.__isTrain = self.__isTrainingSet(classType)
        self.__classType = self.__getActualClassType(classType)
        self.__extractedKeyWords = []
    
    def __isTrainingSet(self, classType):
        if 'train' in classType:
            return True
        else:
            return False
    
    def __getActualClassType(self, classType):
        actualClassType = classType.replace('train', '')
        actualClassType = actualClassType.replace('val', '')
        return actualClassType
    
    def addDocument(self, document):
        noLinesDocument = self.__removeNewLines(document)
        noSymbolsDocument = self.__removeSymbols(noLinesDocument)
        self.__extractedKeyWords.append(self.__extractKeywords(noSymbolsDocument))
        self.__extractedKeyWords.append(noSymbolsDocument)
    
    def __extractKeywords(self, document):
        tagger = tag.Tagger()
        tagger.initialize()
        tokenisedText = tagger.tokenize(document)
        taggedText = tagger.tag(tokenisedText)
        extractor = TermExtractor(filter=permissiveFilter)
        extractedText = extractor.extract(taggedText)
        keywords = ''
        for text in extractedText:
            keywords = keywords + ' ' + text[0];
        return keywords
    
    def __removeNewLines(self, document):
        return document.replace("\n", " ")
    
    def __removeSymbols(self, document):
        return re.sub(r'[^\w ]', '', document)
    
    def getKeywordsAndClassType(self):
        result = ''
        for document in self.__extractedKeyWords:
            result = result + document + ' ' + self.__classType + '\n'
        return result
    
    def isTrain(self):
        return self.__isTrain
    
        