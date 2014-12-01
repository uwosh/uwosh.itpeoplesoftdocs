from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

from AccessControl import Unauthorized
from mechanize._mechanize import LinkNotFoundError

#from smtplib import SMTPRecipientsRefused
from Products.validation import validation

import uwosh.itdocs

@onsetup
def setup_uwosh_itdocs():
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', uwosh.itdocs)
    fiveconfigure.debug_mode = False
    
    ztc.installPackage('uwosh.itdocs')
    
setup_uwosh_itdocs()
ptc.setupPloneSite(products=['uwosh.itdocs'])

class TestCase(ptc.PloneTestCase):
    """A base class for all the tests in this package."""
    
    def _setup(self):
        ptc.PloneTestCase._setup(self)
    
    def becomeManager(self):
        self.setRoles(['Authenticated', 'Member', 'Manager'])

    def createSetupDocument(self, folder, id='test-person'):
        folder.invokeFactory('SetupDocument', id)
        return folder[id]


class FunctionalTestCase(TestCase, ptc.FunctionalTestCase):
    pass
