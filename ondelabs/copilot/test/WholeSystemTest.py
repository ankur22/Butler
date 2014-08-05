'''
Created on 3 Aug 2014

@author: ankur
'''
import logging
import unittest

from ondelabs.copilot.dao.DiskTrainingDAO import DiskTrainingDAO
from ondelabs.copilot.dao.DiskValidationDAO import DiskValidationDAO
from ondelabs.copilot.model.TrainingData import TrainingData


class WholeSystemTest(unittest.TestCase):

    def testSystem(self):
        trainingDAO = DiskTrainingDAO('resource/training.txt')
        trainingData = trainingDAO.loadData()
        trainingData.train()
        trainingData.serialize()

        logging.info('Training has completed')

        validationDAO = DiskValidationDAO('resource/validation.txt')
        validationData = validationDAO.loadData()
        validationResult = validationData.validate(trainingData.getClasses(), trainingData.getLexicon())

        logging.info('Validation has completed')

        self.assertIsNotNone(validationResult, "validationResult should not be None")
        self.assertEqual(validationResult.getAccuracy(), 100, "Accuracy is incorrect")
        self.assertEqual(validationResult.getTotalPredictions(), validationData.getTotalValidationTestDataPoints(), "Number of predictions doe not equal number of validation tests")

    def testDeserializedModel(self):
        trainingData = TrainingData.deserialize()

        logging.info('Training data has been loaded')

        validationDAO = DiskValidationDAO('resource/validation.txt')
        validationData = validationDAO.loadData()
        validationResult = validationData.validate(trainingData.getClasses(), trainingData.getLexicon())

        logging.info('Validation has completed')

        self.assertIsNotNone(validationResult, "validationResult should not be None")
        self.assertEqual(validationResult.getAccuracy(), 100, "Accuracy is incorrect")
        self.assertEqual(validationResult.getTotalPredictions(), validationData.getTotalValidationTestDataPoints(), "Number of predictions doe not equal number of validation tests")
