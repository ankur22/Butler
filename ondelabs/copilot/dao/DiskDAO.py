'''
Created on 3 Aug 2014

@author: ankur
'''
from ondelabs.copilot.dao.BaseDAO import BaseDAO


class DiskDAO(BaseDAO):
    
    def __init__(self, filename):
        self.__filename = filename
    
    def _getLinesFromFile(self):
        f = open(self.__filename)
        lines = f.readlines()
        f.close()
        return lines
    
    def _isInt(self, text):
        try:
            int(text)
            return True
        except ValueError:
            return False
    