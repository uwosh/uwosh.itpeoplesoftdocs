import unittest
from Testing import ZopeTestCase as ztc
from Products.CMFCore.utils import getToolByName

from base import TestCase

from DateTime import DateTime


class TestSetupDocument(TestCase):

    def afterSetUp(self):
        self.becomeManager()
        self.setupDocument = self.createSetupDocument(self.folder)

    def testAttributes(self):
        self.assertEqual(self.setupDocument.getPurpose(), '')
        self.setupDocument.setPurpose('To shed light on all things good')
        self.assertEqual(self.setupDocument.getPurpose(), 'To shed light on all things good')

        self.assertEqual(self.setupDocument.getAudience(), '')
        self.setupDocument.setAudience('Everyone please applaud')
        self.assertEqual(self.setupDocument.getAudience(), 'Everyone please applaud')

        self.assertEqual(self.setupDocument.getAppliesTo(), '')
        self.setupDocument.setAppliesTo('Work request X, business owner Letitia Quntina')
        self.assertEqual(self.setupDocument.getAppliesTo(), 'Work request X, business owner Letitia Quntina')

        self.assertEqual(self.setupDocument.getNavigations(), '')
        self.setupDocument.setNavigations('Page, component, who, navigation')
        self.assertEqual(self.setupDocument.getNavigations(), 'Page, component, who, navigation')

        self.assertEqual(self.setupDocument.getSetup(), '')
        self.setupDocument.setSetup('Many setup steps or requirements')
        self.assertEqual(self.setupDocument.getSetup(), 'Many setup steps or requirements')

        self.assertEqual(self.setupDocument.getFormattingKey(), '')
        self.setupDocument.setFormattingKey('Some notes, topic, and description')
        self.assertEqual(self.setupDocument.getFormattingKey(), 'Some notes, topic, and description')


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetupDocument))
    return suite
