'''
Created on 5 Aug 2014

@author: ankur
'''
import logging

from ondelabs.copilot.dao.DiskTrainingDAO import DiskTrainingDAO
from ondelabs.copilot.dao.DiskValidationDAO import DiskValidationDAO
from ondelabs.dao.DiskArticleDAO import DiskArticleDAO


def trainAndValidate():
    trainingDAO = DiskTrainingDAO('resource/training.txt')
    trainingData = trainingDAO.loadData()
    trainingData.train()
    trainingData.serialize()

    logging.info('Training has completed')

    validationDAO = DiskValidationDAO('resource/validation.txt')
    validationData = validationDAO.loadData()
    validationResult = validationData.validate(trainingData.getClasses(), trainingData.getLexicon())

    logging.info('Validation has completed')

def main():
    diskArticleDAO = DiskArticleDAO()
    classSet = diskArticleDAO.loadArticles()
    diskArticleDAO.writeTrainingClassSet(classSet)
    diskArticleDAO.writeValidationClassSet(classSet)

main()
trainAndValidate()
