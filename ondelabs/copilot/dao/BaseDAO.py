'''
Created on 3 Aug 2014

@author: ankur
'''

class BaseDAO(object):
    
    def loadData(self):
        raise NotImplementedError( "Should implemented this" )
