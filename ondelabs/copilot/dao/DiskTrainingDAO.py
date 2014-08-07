'''
Created on 3 Aug 2014

@author: ankur
'''
import logging

from ondelabs.copilot.dao.DiskDAO import DiskDAO
from ondelabs.copilot.model.Classes import Classes
from ondelabs.copilot.model.Lexicon import Lexicon
from ondelabs.copilot.model.TextClassType import TextClassType
from ondelabs.copilot.model.TrainingData import TrainingData


class DiskTrainingDAO(DiskDAO):
    
    def __init__(self, filename):
        super(DiskTrainingDAO, self).__init__(filename)
    
    def loadData(self):
        lexicon = Lexicon()
        classes = Classes()
        numberOfLines = 0
        
        lines = self._getLinesFromFile()

        for line in lines:
            textClassType = self.__separateTextAndClassType(line)
            if textClassType is not None:
                classType = textClassType.getClassType()
                if self._isInt(classType) is False:
                    logging.warn('classType is not an int')
                    continue
                classType = int(classType)
                lexicon.addWords(textClassType.getWords(), classType)
                classes.addClass(classType, len(textClassType.getWords()))
                numberOfLines = numberOfLines + 1
        
        return TrainingData(lexicon, classes, numberOfLines)
    
    def __separateTextAndClassType(self, line):
        index = line.rfind(' ')
        if index is -1:
            logging.warn('Could not find valid class type in ' + line)
            return None
        else:
            return TextClassType(self._removeNoiseFromText(line[:index]), line[index:])

    def _removeNoiseFromText(self, text):
        # Override so that the text can be constructed in
        # a more preferable way e.g. remove new lines;
        # remove symbols; all lower case.
        return text
    