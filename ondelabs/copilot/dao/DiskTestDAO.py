'''
Created on 3 Aug 2014

@author: ankur
'''

import logging

from ondelabs.copilot.dao.DiskDAO import DiskDAO
from ondelabs.copilot.model.TestData import TestData
from ondelabs.copilot.model.Text import Text


class DiskTestDAO(DiskDAO):
    
    def __init__(self, filename):
        super(DiskTestDAO, self).__init__(filename)
    
    def loadData(self):
        result = {}
        lines = self._getLinesFromFile()

        for line in lines:
            textClassType = self.__separateText(line)
            if textClassType is not None:
                result[line] = textClassType
        
        return TestData(result)
    
    def __separateText(self, line):
        return Text(self._removeNoiseFromText(line))

    def _removeNoiseFromText(self, text):
        # Override so that the text can be constructed in
        # a more preferable way e.g. remove new lines;
        # remove symbols; all lower case.
        return text
